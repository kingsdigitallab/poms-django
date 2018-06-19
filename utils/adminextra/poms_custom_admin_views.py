import re
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.utils.translation import ugettext as _

from pomsapp.models import *


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
                    'add': user.has_perm(
                        "add {}".format(model.__name__.lower())),
                    'change': user.has_perm(
                        "change {}".format(model.__name__.lower())),
                    'delete': user.has_perm(
                        "delete {}".format(model.__name__.lower())),
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
        app['models'].sort(key=lambda x: x['name'])
        # the list is sorted twice, so if there's no explicit order it falls
        #  back to the alphab. one
        app['models'].sort(key=lambda x: x['order'])
        app_list_final.append(app)
    context = {
        'title': _('%s administration') % capfirst(app_label),
        # 'app_list': [app_dict],
        'app_list': app_list_final,
        'root_path': admin.site.root_path,
    }
    context.update(extra_context or {})
    return render(
        request, 'admin/app_index.html', context
    )


from django.contrib.admin.models import LogEntry


# #####
#  VIEW of the recent contributors
# #####

@staff_member_required
def contributions(request, ):
    "The all-changes view for this application"
    my_data = []
    MAX_CHANGES = 1000
    logs = LogEntry.objects.all()[:MAX_CHANGES]
    # sometime the action_time method doesn't return a date, so let's make
    # sure...
    temp = list(set([x.action_time.date() for x in logs if
                     type(x.action_time) == type(
                         datetime.datetime(2010, 10, 28, 15, 40, 57))]))

    for d in sorted(temp, reverse=True):
        my_data.append((d, LogEntry.objects.filter(action_time__year=d.year,
                                                   action_time__month=d.month,
                                                   action_time__day=d.day).order_by(
            'user', 'action_time')))

    # print((my_data)

    return render(
        request,
        "admin/contributions.html",
        {'my_data': my_data},

    )


# #####
#  VIEW of orphan titles
# #####

@staff_member_required
def orphan_titles(request, ):
    "List all titles that are not attached to any person"
    return render(
        request,
        "admin/orphan_titles.html",
        {'list': TitleType.objects.filter(facttitle=None)},

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
    return render(
        request,
        "admin/orphan_places.html",
        {'list': ll},

    )


# from admin source / options.py

# def history_view(self, request, object_id, extra_context=None):
#	   "The 'history' admin view for this model."
#	   from django.contrib.admin.models import LogEntry
#	   model = self.model
#	   opts = model._meta
#	   app_label = opts.app_label
#	   action_list = LogEntry.objects.filter(
#		   object_id = object_id,
#		   content_type__id__exact = ContentType.objects.get_for_model(
# model).id
#	   ).select_related().order_by('action_time')
#	   # If no history was found, see whether this object even exists.
#	   obj = get_object_or_404(model, pk=object_id)
#	   context = {
#		   'title': _('Change history: %s') % force_unicode(obj),
#		   'action_list': action_list,
#		   'module_name': capfirst(force_unicode(opts.verbose_name_plural)),
#		   'object': obj,
#		   'root_path': self.admin_site.root_path,
#		   'app_label': app_label,
#	   }
#	   context.update(extra_context or {})
#	   return render(self.object_history_template or [
#		   "admin/%s/%s/object_history.html" % (opts.app_label,
# opts.object_name.lower()),
#		   "admin/%s/object_history.html" % opts.app_label,
#		   "admin/object_history.html"
#	   ], context, context_instance=template.RequestContext(request))


# #####
#  VIEW of orphan possessions
# /db/admin/orphan_possessions/
# #####

@staff_member_required
def orphan_possessions(request):
    "List all possessions that are not attached to any factoid"
    ll = []

    possessions_lists = [Privileges, Poss_Alms, Poss_Unfree_persons,
                         Poss_Revenues_silver,
                         Poss_Revenues_kind, Poss_Office, Poss_Objects,
                         Poss_Lands, Poss_General, ]

    for model in possessions_lists:
        res = model.objects.filter(factoid=None)
        if res:
            ll += res

    return render(
        request,
        "admin/orphan_possessions.html",
        {'list': ll},

    )


# #####
#  VIEW of orphan people
# #####

@staff_member_required
def orphan_people(request, ):
    "List all people that are not attached to factoids"
    ll = Person.objects.filter(assochelperperson=None)
    return render(
        request,
        "admin/orphan_people.html",
        {'list': ll},

    )


# 2012-04-03

@staff_member_required
def charterscirca(request, ):
    "List all charters that use 'before', 'after' or 'circa' "
    ll = []
    for x in Charter.objects.all():
        if (x.from_modifier in ['cir', 'aft', 'bef']) or (
                x.to_modifier in ['cir', 'aft', 'bef']):
            ll.append(x)
    return render(request, "admin/charters_circa.html", {'list': ll},
                  )


@staff_member_required
def previous_landholder(request, ):
    "List of 'previous landholder' role in possession factoid "
    ll = []
    for f in FactPossession.objects.all():
        for x in f.assocfactoidperson_set.all():
            if x.role and x.role.name in ["Previous landholder"]:
                ll.append(x)
    return render(request, "admin/previous_landholder.html", {'list': ll},
                  )


# #####
#  VIEW of factoids that are not 
# #####

@staff_member_required
def unmarked_factoids(request, ):
    """http://poms-stg.cch.kcl.ac.uk/db/helpdesk/tickets/42/
    factoids that used to be marked for review and saying.. ** Automatic
    date extraction results: I successfully extracted the years, but there
    might be other stuff **
    """
    return render(
        request,
        "admin/unmarked_factoids.html",
        {'list': []},

    )


# #####
#  VIEW reports for places bootstrapping
# #####

@staff_member_required
def created_docplaces(request, ):
    """
    Report on doc-places that have been matched up automatically
    """
    return render(
        request,
        "admin/created_docplaces.html",
        {'list': []},

    )


@staff_member_required
def missing_docplaces(request, ):
    """
    Report on doc-places that are not linked to Places
    """
    lista = Charter.objects.filter(placefk=None).exclude(
        placedatemodern="").order_by('id')
    return render(
        request,
        "admin/missing_docplaces.html",
        {'list': lista},

    )


# todo

@staff_member_required
def created_possplaces(request, ):
    """
    Report on doc-places that have been matched up automatically
    """
    return render(
        request,
        "admin/created_possplaces.html",
        {'list': []},

    )


@staff_member_required
def missing_possplaces(request, ):
    """
    Report on doc-places that are not linked to Places
    """
    lista = Poss_Lands.objects.filter(place=None).order_by('id')

    return render(
        request,
        "admin/missing_possplaces.html",
        {'list': lista},
    )
