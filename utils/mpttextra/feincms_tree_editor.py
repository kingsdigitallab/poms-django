# this file has been taken from the FEINCMS project
# [http://www.feinheit.ch/media/labs/feincms/]
# it provides functionalities for managing trees in django's admin
# requires the FEINCMS admin media anyways! they can be specified using the
# MPTTEXTRA_ADMIN_MEDIA var in settings.py
# I extracted it and put it here for easier integration

# also, remember that this stuff is loaded in
# /util/adminextra/autocomplete_tree_admin

#  MPTT is required, and MPTTMEDIA folder in /media too


import functools
from django.conf import settings as django_settings
from django.contrib import admin
from django.contrib.admin.views import main
from django.db.models import Q
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden, HttpResponseNotFound,
                         HttpResponseServerError)
import json
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.auth import get_permission_codename

from mptt.exceptions import InvalidMove

import logging

# from feincms import settings


# Admin settings
FEINCMS_ADMIN_MEDIA = getattr(
    django_settings,
    'MPTTEXTRA_ADMIN_MEDIA',
    '/media/sys/feincms/')
# Link to google APIs instead of using local copy of JS libraries
FEINCMS_ADMIN_MEDIA_HOTLINKING = getattr(
    django_settings, 'FEINCMS_ADMIN_MEDIA_HOTLINKING', False)


# ------------------------------------------------------------------------
def django_boolean_icon(field_val, alt_text=None, title=None):
    """
    Return HTML code for a nice representation of true/false.
    """

    # Origin: contrib/admin/templatetags/admin_list.py
    BOOLEAN_MAPPING = {True: 'yes', False: 'no', None: 'unknown'}
    alt_text = alt_text or BOOLEAN_MAPPING[field_val]
    if title is not None:
        title = 'title="%s" ' % title
    else:
        title = ''
    return mark_safe(u'<img src="%simg/admin/icon-%s.gif" alt="%s" %s/>' %
                     (django_settings.ADMIN_MEDIA_PREFIX,
                      BOOLEAN_MAPPING[field_val], alt_text, title))


def _build_tree_structure(cls):
    """
    Build an in-memory representation of the item tree, trying to keep
    database accesses down to a minimum. The returned dictionary looks like
    this (as json dump):

        {"6": [7, 8, 10]
         "7": [12],
         "8": [],
         ...
         }
    """
    all_nodes = {}

    # for p_id, parent_id in cls.objects.order_by(cls._meta.tree_id_attr,
    # cls._meta.left_attr).values_list("pk", "%s_id" % cls._meta.parent_attr):
    if hasattr(cls, '_mptt_meta'):  # New-style MPTT
        mptt_opts = cls._mptt_meta
    else:
        mptt_opts = cls._meta

    for p_id, parent_id in cls.objects.order_by(
            mptt_opts.tree_id_attr, mptt_opts.left_attr).values_list(
                "pk", "%s_id" % mptt_opts.parent_attr):
        all_nodes[p_id] = []

        if parent_id:
            if parent_id not in all_nodes:
                # This happens very rarely, but protect against parents that
                # we have yet to iteratove over.
                all_nodes[parent_id] = []
            all_nodes[parent_id].append(p_id)

    return all_nodes


# ------------------------------------------------------------------------
def ajax_editable_boolean_cell(item, attr, text='', override=None):
    """
    Generate a html snippet for showing a boolean value on the admin page.
    Item is an object, attr is the attribute name we should display. Text
    is an optional explanatory text to be included in the output.

    This function will emit code to produce a checkbox input with its state
    corresponding to the item.attr attribute if no override value is passed.
    This input is wired to run a JS ajax updater to toggle the value.

    If override is passed in, ignores the attr attribute and returns a
    static image for the override boolean with no user interaction possible
    (useful for "disabled and you can't change it" situations).
    """
    if text:
        text = '&nbsp;(%s)' % text

    if override is not None:
        a = [django_boolean_icon(override, text), text]
    else:
        value = getattr(item, attr)
        a = [
            '<input type="checkbox"',
            value and ' checked="checked"' or '',
            ' onclick="return inplace_toggle_boolean(%d, \'%s\')";' % (
                item.id, attr),
            ' />',
            text,
        ]

    a.insert(0, '<div id="wrap_%s_%d">' % (attr, item.id))
    a.append('</div>')
    # print a
    return ''.join(a)

# ------------------------------------------------------------------------


def ajax_editable_boolean(attr, short_description):
    """
    Convenience function: Assign the return value of this method to a variable
    of your ModelAdmin class and put the variable name into list_display.

    Example::

        class MyTreeEditor(TreeEditor):
            list_display = ('__unicode__', 'active_toggle')

            active_toggle = ajax_editable_boolean('active', _('is active'))
    """

    def _fn(self, item):
        return ajax_editable_boolean_cell(item, attr)
    _fn.allow_tags = True
    _fn.short_description = short_description
    _fn.editable_boolean_field = attr
    return _fn


# ------------------------------------------------------------------------
class ChangeList(main.ChangeList):
    """
    Custom ``ChangeList`` class which ensures that the tree entries are always
    ordered in depth-first order (order by ``tree_id``, ``lft``).
    """

    def __init__(self, request, *args, **kwargs):
        self.user = request.user
        super(ChangeList, self).__init__(request, *args, **kwargs)

    def get_query_set(self):
        return super(ChangeList, self).get_queryset().order_by(
            'tree_id', 'lft')

    def get_results(self, request):
        # if settings.FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS:
        if True:
            clauses = [Q(
                tree_id=tree_id,
                lft__lte=lft,
                rght__gte=rght,
            ) for lft, rght, tree_id in
                self.queryset.values_list('lft', 'rght', 'tree_id')]
            if clauses:
                self.queryset = self.model._default_manager.filter(
                    functools.reduce(lambda p, q: p | q, clauses))

        super(ChangeList, self).get_results(request)

        for item in self.result_list:
            # if settings.FEINCMS_TREE_EDITOR_OBJECT_PERMISSIONS:
            if False:
                item.feincms_editable = self.model_admin.has_change_permission(
                    request, item)
            else:
                item.feincms_editable = True

# ------------------------------------------------------------------------
# MARK: -
# ------------------------------------------------------------------------


class TreeEditor(admin.ModelAdmin):
    """
    The ``TreeEditor`` modifies the standard Django administration change list
    to a drag-drop enabled interface for django-mptt_-managed Django models.

    .. _django-mptt: http://github.com/mptt/django-mptt/
    """

    # if settings.FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS:
    if True:
        # Make sure that no pagination is displayed.
        # Slicing is disabled anyway,
        # therefore this value does not have an influence on the queryset
        list_per_page = 999999999

    def __init__(self, *args, **kwargs):
        super(TreeEditor, self).__init__(*args, **kwargs)

        self.list_display = list(self.list_display)

        if 'indented_short_title' not in self.list_display:
            if self.list_display[0] == 'action_checkbox':
                self.list_display[1] = 'indented_short_title'
            else:
                self.list_display[0] = 'indented_short_title'
        self.list_display_links = ('indented_short_title',)

        opts = self.model._meta
        self.change_list_template = [
            'admin/feincms/%s/%s/tree_editor.html' % (
                opts.app_label, opts.object_name.lower()),
            'admin/feincms/%s/tree_editor.html' % opts.app_label,
            'admin/feincms/tree_editor.html',
            'admin/tree_editor.html',
            'tree_editor.html'
        ]

    def editable(self, item):
        return getattr(item, 'feincms_editable', True)

    def indented_short_title(self, item):
        """
        Generate a short title for an object, indent it depending on
        the object's depth in the hierarchy.
        """
        r = ''
        if hasattr(item, 'get_absolute_url'):
            r = '<input type="hidden" class="medialibrary_file_path"\
                value="%s" />' % item.get_absolute_url()

        editable_class = ''
        if not getattr(item, 'feincms_editable', True):
            editable_class = ' tree-item-not-editable'

        r += '<span id="page_marker-%d" class="page_marker%s"\
            style="width: %dpx;">&nbsp;</span>&nbsp;' % (
            item.id, editable_class, 14 + item.level * 18)
#        r += '<span tabindex="0">'
        if hasattr(item, 'short_title'):
            r += '{}'.format(item.short_title())
        else:
            r += '{}'.format(item)
#        r += '</span>'
        return mark_safe(r)
    indented_short_title.short_description = _('title')
    indented_short_title.allow_tags = True

    def _collect_editable_booleans(self):
        """
        Collect all fields marked as editable booleans. We do not
        want the user to be able to edit arbitrary fields by crafting
        an AJAX request by hand.
        """
        if hasattr(self, '_ajax_editable_booleans'):
            return

        self._ajax_editable_booleans = {}

        for field in self.list_display:
            # The ajax_editable_boolean return value has to be assigned
            # to the ModelAdmin class
            try:
                item = getattr(self.__class__, field)
            except (AttributeError, TypeError) as e:
                continue

            attr = getattr(item, 'editable_boolean_field', None)
            if attr:
                def _fn(self, instance):
                    return [ajax_editable_boolean_cell(instance, _fn.attr)]
                _fn.attr = attr
                result_func = getattr(item, 'editable_boolean_result', _fn)
                self._ajax_editable_booleans[attr] = result_func

    def _refresh_changelist_caches(self):
        """
        Refresh information used to show the changelist tree structure such as
        inherited active/inactive states etc.

        XXX: This is somewhat hacky, but since it's an
        internal method, so be it.
        """

        pass

    def _toggle_boolean(self, request):
        """
        Handle an AJAX toggle_boolean request
        """
        try:
            item_id = int(request.POST.get('item_id', None))
            attr = str(request.POST.get('attr', None))
        except BaseException:
            return HttpResponseBadRequest("Malformed request")

        if not request.user.is_staff:
            logging.warning(
                "Denied AJAX request by non-staff %s to\
                    toggle boolean %s for object #%s",
                request.user,
                attr,
                item_id)
            return HttpResponseForbidden(
                "You do not have permission to access this object")

        self._collect_editable_booleans()

        if attr not in self._ajax_editable_booleans:
            return HttpResponseBadRequest("not a valid attribute %s" % attr)

        try:
            obj = self.model._default_manager.get(pk=item_id)
        except self.model.DoesNotExist:
            return HttpResponseNotFound("Object does not exist")

        can_change = False

        if hasattr(obj, "user_can") and obj.user_can(
                request.user, change_page=True):
            # Was added in c7f04dfb5d, but I've no idea what user_can is about.
            can_change = True
        else:
            can_change = self.has_change_permission(request, obj=obj)

        if not can_change:
            logging.warning(
                "Denied AJAX request by %s to toggle boolean %s for object %s",
                request.user,
                attr,
                item_id)
            return HttpResponseForbidden(
                "You do not have permission to access this object")

        logging.info(
            "Processing request by %s to toggle %s on %s",
            request.user,
            attr,
            obj)

        try:
            before_data = self._ajax_editable_booleans[attr](self, obj)

            setattr(obj, attr, not getattr(obj, attr))
            obj.save()

            self._refresh_changelist_caches()

            # Construct html snippets to send back to client for status update
            data = self._ajax_editable_booleans[attr](self, obj)

        except Exception as e:
            logging.exception(
                "Unhandled exception while toggling %s on %s", attr, obj)
            return HttpResponseServerError(
                "Unable to toggle %s on %s" % (attr, obj))

        # Weed out unchanged cells to keep the updates small. This assumes
        # that the order a possible get_descendents() returns does not change
        # before and after toggling this attribute. Unlikely, but still...
        d = []
        for a, b in zip(before_data, data):
            if a != b:
                d.append(b)

        # TODO: Shorter: [ y for x,y in zip(a,b) if x!=y ]
        return HttpResponse(json.dumps(d), mimetype="application/json")

    def get_changelist(self, request, **kwargs):
        return ChangeList

    def changelist_view(self, request, extra_context=None, *args, **kwargs):
        """
        Handle the changelist view, the django view for the model instances
        change list/actions page.
        """

        if 'actions_column' not in self.list_display:
            self.list_display.append('actions_column')

        # handle common AJAX requests
        if request.is_ajax():
            cmd = request.POST.get('__cmd')
            if cmd == 'toggle_boolean':
                return self._toggle_boolean(request)
            elif cmd == 'move_node':
                return self._move_node(request)
            else:
                return HttpResponseBadRequest(
                    'Oops. AJAX request not understood.')

        self._refresh_changelist_caches()

        extra_context = extra_context or {}
        extra_context['FEINCMS_ADMIN_MEDIA'] = FEINCMS_ADMIN_MEDIA
        extra_context['FEINCMS_ADMIN_MEDIA_HOTLINKING'] =\
            FEINCMS_ADMIN_MEDIA_HOTLINKING
        extra_context['tree_structure'] = mark_safe(
            json.dumps(
                _build_tree_structure(self.model)))

        return super(TreeEditor, self).changelist_view(
            request, extra_context, *args, **kwargs)

    def has_change_permission(self, request, obj=None):
        """
        Implement a lookup for object level permissions. Basically the same as
        ModelAdmin.has_change_permission, but also passes the obj parameter in.
        """
        # if settings.FEINCMS_TREE_EDITOR_OBJECT_PERMISSIONS:
        if True:
            opts = self.opts
            r = request.user.has_perm(
                opts.app_label +
                '.' +
                get_permission_codename(
                    'change',
                    self.model._meta),
                obj)
        else:
            r = True

        return r and super(
            TreeEditor, self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Implement a lookup for object level permissions. Basically the same as
        ModelAdmin.has_delete_permission, but also passes the obj parameter in.
        """
        # if settings.FEINCMS_TREE_EDITOR_OBJECT_PERMISSIONS:
        if True:
            opts = self.opts
            r = request.user.has_perm(
                opts.app_label +
                '.' +
                get_permission_codename(
                    'delete',
                    self.model._meta),
                obj)
        else:
            r = True

        return r and super(
            TreeEditor, self).has_delete_permission(request, obj)

    def _move_node(self, request):
        cut_item = self.model._tree_manager.get(
            pk=request.POST.get('cut_item'))
        pasted_on = self.model._tree_manager.get(
            pk=request.POST.get('pasted_on'))
        position = request.POST.get('position')

        if position in ('last-child', 'left'):
            try:
                self.model._tree_manager.move_node(
                    cut_item, pasted_on, position)
            except InvalidMove as e:
                self.message_user(request, e)
                return HttpResponse('FAIL')

            # Ensure that model save has been run
            cut_item = self.model._tree_manager.get(pk=cut_item.pk)
            cut_item.save()

            self.message_user(
                request, ugettext('%s has been moved to a new position.') %
                cut_item)
            return HttpResponse('OK')

        self.message_user(request, ugettext(
            'Did not understand moving instruction.'))
        return HttpResponse('FAIL')

    def _actions_column(self, instance):
        return []

    def actions_column(self, instance):
        return u' '.join(self._actions_column(instance))
    actions_column.allow_tags = True
    actions_column.short_description = _('actions')
