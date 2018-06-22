import re
from django import template
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.text import capfirst
from django.utils.translation import ugettext as _
from ltb.ltbapp.models import *


# #####
# HOME VIEW
# #####

@staff_member_required
def pomsapp(request, url):
    url = url.rstrip('/')  # Trim trailing slash, if it exists.
    admin.site.root_path = re.sub(re.escape(url) + '$', '', request.path)
    return app_index(request, url)


# This method is mostly copied from [
# PYTHON]\Lib\site-packages\django\contrib\admin\sites.py, app_index()
# It splits all the tables into groups, the name of the group they belong to
#  is determined by the "table_group" variable in the models
# It uses the existing application templates ([
# PYTHON]\Lib\site-packages\django\contrib\admin\templates\admin\app_index
# .html)
# No need to extend that template
def app_index(request, app_label, extra_context=None):
    user = request.user
    has_module_perms = user.has_module_perms(app_label)
    app_list = {}
    app_dict = {}
    for model, model_admin in admin.site._registry.items():
        if app_label == model._meta.app_label:
            if has_module_perms:
                perms = {
                    'add': user.has_perm("%s.%s" % (
                    app_label, model._meta.get_add_permission())),
                    'change': user.has_perm("%s.%s" % (
                    app_label, model._meta.get_change_permission())),
                    'delete': user.has_perm("%s.%s" % (
                    app_label, model._meta.get_delete_permission())),
                }
                # GN - use the table group as an index for the app
                try:
                    app_index = model.table_group
                except AttributeError:
                    app_index = ''
                # NEW michele: I added an extra property for ORDERING
				# manually the model list
                try:
                    app_order = model.table_order
                except AttributeError:
                    app_order = 0
                # Check whether user has any perm for this module.
                # If so, add the module to the model_list.
                if True in perms.values():
                    model_dict = {
                        'name': capfirst(model._meta.verbose_name_plural),
                        'admin_url': '%s/' % model.__name__.lower(),
                        'perms': perms,
                        'order': app_order,
                        # 'reference': model.reference_table,
                    }
                    if (app_index in app_list):
                        app_list[app_index]['models'].append(model_dict),
                    else:
                        # First time around, now that we know there's
                        # something to display, add in the necessary meta
                        # information.
                        app_list[app_index] = {
                            'name': app_label.title(),
                            'app_url': '',
                            'has_module_perms': has_module_perms,
                            'models': [model_dict],
                            'order': app_order,
                        }
                        if (app_index != ''):
                            app_list[app_index]['name'] += ' - ' + app_index
                # app_list.append(app_dict)
    # if not app_dict:
    #	 raise http.Http404('The requested admin page does not exist.')
    # Sort the models alphabetically within each app.
    app_list_final = []
    for group_name, app in app_list.items():
        app['models'].sort(lambda x, y: cmp(x['name'], y['name']))
        # the list is sorted twice, so if there's no explicit order it falls
		#  back to the alphab. one
        app['models'].sort(lambda x, y: cmp(x['order'], y['order']))
        app_list_final.append(app)
    context = {
        'title': _('%s administration') % capfirst(app_label),
        # 'app_list': [app_dict],
        'app_list': app_list_final,
        'root_path': admin.site.root_path,
    }
    context.update(extra_context or {})
    return render_to_response(
        admin.site.app_index_template or 'admin/app_index.html', context,
        context_instance=template.RequestContext(request)
        )


from django.contrib.admin.models import LogEntry


# #####
#  VIEW of the recent contributors
# #####

@staff_member_required
def contributions(request, ):
    "The all-changes view for this application"
    return render_to_response(
        "admin/contributions.html",
        {'list': LogEntry.objects.all()},
        RequestContext(request, {}),
    )


# #####
#  VIEW of orphan places
# #####

@staff_member_required
def orphan_places(request, ):
    "List all places that are not in a hierarchy"
    ll = []
    for x in Place.objects.all():
        if x.is_leaf_node() and x.is_root_node():
            ll.append(x)
    return render_to_response(
        "admin/orphan_places.html",
        {'list': ll},
        RequestContext(request, {}),
    )

# from admin source / options.py

# def history_view(self, request, object_id, extra_context=None):
#      "The 'history' admin view for this model."
#      from django.contrib.admin.models import LogEntry
#      model = self.model
#      opts = model._meta
#      app_label = opts.app_label
#      action_list = LogEntry.objects.filter(
#          object_id = object_id,
#          content_type__id__exact = ContentType.objects.get_for_model(
# model).id
#      ).select_related().order_by('action_time')
#      # If no history was found, see whether this object even exists.
#      obj = get_object_or_404(model, pk=object_id)
#      context = {
#          'title': _('Change history: %s') % force_unicode(obj),
#          'action_list': action_list,
#          'module_name': capfirst(force_unicode(opts.verbose_name_plural)),
#          'object': obj,
#          'root_path': self.admin_site.root_path,
#          'app_label': app_label,
#      }
#      context.update(extra_context or {})
#      return render_to_response(self.object_history_template or [
#          "admin/%s/%s/object_history.html" % (opts.app_label, opts.object_name.lower()),
#          "admin/%s/object_history.html" % opts.app_label,
#          "admin/object_history.html"
#      ], context, context_instance=template.RequestContext(request))
