# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from pomsapp.models import *
from utils.myutils import *
from utils.template import render_block_to_string


##################
#  Wed Oct 13 16:18:19 BST 2010
#  Record detail sections:
#
##################


# def index(request):
# 	# request.session['queryargs'] = []
# 	# request.session['activeIDs'] = []
# 	return redirect('basic_search')


def basic_record(request):
    """ view for the splash page with the people-cloud """

    MAX_FACTOIDS_PEOPLE = 80
    MAX_FACTOIDS_CHARTERS = 30

    def calc_size_people(n):
        n = n / 100
        if n < 10:
            return n + 10
        elif n < 20:
            return n + 10
        else:
            return n

    def calc_size_sources(n):
        # n = int(log(n*10)) + 10
        return n / 3

    people = Person.objects.filter(helper_totfactoids__gt=MAX_FACTOIDS_PEOPLE)
    people_for_cloud = [(p, calc_size_people(p.helper_totfactoids)) for p in
                        people]

    charters = Charter.objects.filter(
        helper_totfactoids__gt=MAX_FACTOIDS_CHARTERS)
    charters_for_cloud = [(p, calc_size_sources(p.helper_totfactoids)) for p in
                          charters]
    context = {
        'charters_for_cloud': charters_for_cloud,
        'people_for_cloud': people_for_cloud,
        'record_splash_page': True
    }

    return render(request, 'pomsapp/record/splash.html', context)


# --------
# PERSON
# --------


def person_detail(request, person_id):
    """ View for persons: check if it's a call for the entire page,
    or if it's an ajax call for updating the
        bottom part of the page only, where the related factoids are displayed.

    """
    # request.session['queryargs'] = []
    # request.session['activeIDs'] = []
    page = request.GET.get('page', False)
    tab = request.GET.get('tab', False)
    ordering = request.GET.get('ordering', False)
    preview = request.GET.get('preview', False)
    ajax_flag = False

    if page and tab:  # ==> then it's an ajax query
        ajax_flag = True
        try:
            page = int(page)
        except ValueError:
            page = 1
    else:
        page = 1
        tab = 1

    MAX_RESULTS_LENGTH = 50

    ordering_string, chosen_ordering, proanima_chosen_ordering = \
        determine_ordering(
            "person", ordering)

    person = get_object_or_404(Person, pk=person_id)

    if preview:  # in this case we're just returning a sub-template for
        # info, before the user clicks on the actual
        # page

        return_str = render_block_to_string(
            'pomsapp/record/record_person.html',
            'preview_contents',
            {'record': person, 'active_ordering': ordering_string,
             'preview': True})
        return HttpResponse(return_str)

    # ++++
    # now returns the items:  1st, via ajax
    # ++++

    if ajax_flag:
        items = None
        if tab == 'possessionFact':
            items = person.get_association_factoids('possession',
                                                    chosen_ordering)
        if tab == 'relationshipFact':
            items = person.get_association_factoids('relationship',
                                                    chosen_ordering)
        if tab == 'titleFact':
            items = person.get_association_factoids('title/occupation',
                                                    chosen_ordering)
        if tab == 'transactionFact':
            items = person.get_association_factoids('transaction',
                                                    chosen_ordering)
        if tab == 'proanimaFact':
            items = person.get_association_factoids('proanima',
                                                    proanima_chosen_ordering)
        if tab == 'witnessFact':
            items = person.get_association_factoids('witness', chosen_ordering)

        if items:
            paginator = Paginator(items, MAX_RESULTS_LENGTH)
            tot = len(items)
            try:
                items = paginator.page(page)
            except (EmptyPage, InvalidPage):
                # If page request is out of range, deliver last page of
                # results.
                items = paginator.page(paginator.num_pages)
            items.extrastuff = paginator_helper(page,
                                                paginator.num_pages)  # add
            # other useful paginator data to the object
            items.ordering = ordering
            items.tot = tot
            items.type = tab  # a string repr of the type, eg 'possessionFact'

            return_str = render(request, 'pomsapp/includes/person_tabs.html',
                                {'record': person,
                                 'active_ordering': ordering_string,
                                 tab: items, })
            return HttpResponse(return_str)

    # ++++
    # Standard call (non ajax): returns the entire page
    # ++++
    else:

        vals = {}

        vals['possessionFact'] = person.get_association_factoids('possession',
                                                                 chosen_ordering)
        vals['relationshipFact'] = person.get_association_factoids(
            'relationship', chosen_ordering)
        vals['titleFact'] = person.get_association_factoids('title/occupation',
                                                            chosen_ordering)
        vals['transactionFact'] = person.get_association_factoids(
            'transaction', chosen_ordering)
        vals['proanimaFact'] = person.get_association_factoids('proanima',
                                                               proanima_chosen_ordering)
        vals['witnessFact'] = person.get_association_factoids('witness',
                                                              chosen_ordering)

        # substitute the contents of the dict with the paginated values
        for k in vals.keys():
            paginator = Paginator(vals[k], MAX_RESULTS_LENGTH)
            tot = len(vals[k])
            try:
                vals[k] = paginator.page(page)
            except (EmptyPage, InvalidPage):
                # If page request is out of range, deliver last page of
                # results.
                vals[k] = paginator.page(paginator.num_pages)
            vals[k].extrastuff = paginator_helper(page,
                                                  paginator.num_pages)  #
            # add other useful paginator data to the object
            vals[k].ordering = ordering
            vals[k].tot = tot
            vals[k].type = k  # a string repr of the type, eg 'possessionFact'

        context = {'record': person,
                   'possessionFact': vals['possessionFact'],
                   'preview': preview,
                   'relationshipFact': vals['relationshipFact'],
                   'titleFact': vals['titleFact'],
                   'transactionFact': vals['transactionFact'],
                   'proanimaFact': vals['proanimaFact'],
                   'witnessFact': vals['witnessFact'],
                   'active_ordering': ordering_string,
                   'permalink': request.get_host() + request.path,
                   }
        return render(request, 'pomsapp/record/record_person.html', context)


# --------
# SOURCE
# --------


def source_detail(request, source_id):
    """
    View that shows a source record, and the related factoids.
    """
    # request.session['queryargs'] = []
    # request.session['activeIDs'] = []
    page = request.GET.get('page', False)
    tab = request.GET.get('tab',
                          False)  # I put it here, but it's not necessary yet
    ordering = request.GET.get('ordering', False)
    preview = request.GET.get('preview', False)
    ajax_flag = False
    MAX_RESULTS_LENGTH = 50

    if page and tab:  # ==> then it's an ajax query
        ajax_flag = True
        try:
            page = int(page)
        except ValueError:
            page = 1
    else:
        page = 1
        tab = 1

    ordering_string, chosen_ordering, proanima_chosen_ordering = \
        determine_ordering(
            "source", ordering)

    father_source = get_object_or_404(Source, pk=source_id)
    source_tuple = father_source.get_right_subclass()
    if source_tuple is None:
        raise Http404
    source = source_tuple[1]

    if preview:  # in this case we're just returning a sub-template for
        # info, before the user clicks on the actual
        # page

        return_str = render_block_to_string(
            'pomsapp/record/record_source.html',
            'preview_contents',
            {'record': source, 'active_ordering': ordering_string, })
        return HttpResponse(return_str)

    # ++++
    # now returns the items:
    # ++++
    if ajax_flag:
        items = None
        if tab == 'possessionFact':
            items = source.get_factoids('possession', chosen_ordering)
        if tab == 'relationshipFact':
            items = source.get_factoids('relationship', chosen_ordering)
        if tab == 'titleFact':
            items = source.get_factoids('title/occupation', chosen_ordering)
        if tab == 'transactionFact':
            items = source.get_factoids('transaction', chosen_ordering)

        if items:
            paginator = Paginator(items, MAX_RESULTS_LENGTH)
            tot = len(items)
            try:
                items = paginator.page(page)
            except (EmptyPage, InvalidPage):
                # If page request is out of range, deliver last page of
                # results.
                items = paginator.page(paginator.num_pages)
            items.extrastuff = paginator_helper(page,
                                                paginator.num_pages)  # add
            # other useful paginator data to the object
            items.ordering = ordering
            items.tot = tot
            items.type = tab  # a string repr of the type, eg 'possessionFact'

            return_str = render(request,
                                'pomsapp/includes/source_tabs.html',
                                {'record': source,
                                 'active_ordering': ordering_string,
                                 tab: items, })
            return HttpResponse(return_str)

    # IF NOT AJAX

    vals = {}

    vals['possessionFact'] = source.get_factoids('possession', chosen_ordering)
    vals['relationshipFact'] = source.get_factoids('relationship',
                                                   chosen_ordering)
    vals['titleFact'] = source.get_factoids('title/occupation',
                                            chosen_ordering)
    vals['transactionFact'] = source.get_factoids('transaction',
                                                  chosen_ordering)

    # substitute the contents of the dict with the paginated values
    for k in vals.keys():
        paginator = Paginator(vals[k], MAX_RESULTS_LENGTH)
        tot = len(vals[k])
        try:
            vals[k] = paginator.page(page)
        except (EmptyPage, InvalidPage):
            # If page request is out of range, deliver last page of results.
            vals[k] = paginator.page(paginator.num_pages)
        vals[k].extrastuff = paginator_helper(page,
                                              paginator.num_pages)  # add
        # other useful paginator data to the object
        vals[k].ordering = ordering
        vals[k].tot = tot
        vals[k].type = k  # a string repr of the type, eg 'possessionFact'

    return render(request,
                  'pomsapp/record/record_source.html',
                  {'record': source,
                   'possessionFact': vals['possessionFact'],
                   'relationshipFact': vals['relationshipFact'],
                   'titleFact': vals['titleFact'],
                   'transactionFact': vals['transactionFact'],
                   'active_ordering': ordering_string,
                   'permalink': request.get_host() + request.path,
                   }
                  )


# --------
# FACTOID
# --------


def factoid_detail(request, factoid_id):
    """
    View that shows a Factoid record, and the related people and
    possessions, organized by type.

    No need for pagination here, because:
    Factoids with more than 50 assocPeople: 24840, 47541, 27209, 10341,
    47325  (max 80)
    Factoids with more than 50 witnesses: None
    Factoids with more than 50 proanima people: None

    Factoids with more than 50 possesssions: haven't checked, but presumably
    None..

    <helper_inferred> is used on possessions associations to make sure we
    filter out the ones 'exploded',
    ie inherited, so to
    speed up searches on hiearchical relations.


    """

    page = request.GET.get('page', False)
    tab = request.GET.get('tab',
                          False)  # I put it here, but it's not necessary yet
    ordering = request.GET.get('ordering', False)
    preview = request.GET.get('preview', False)
    #
    map = request.GET.get('map', False)
    ajax_flag = False
    MAX_RESULTS_LENGTH = 50

    if page and tab:  # ==> then it's an ajax query
        ajax_flag = True
        try:
            page = int(page)
        except ValueError:
            page = 1
    else:
        page = 1
        tab = 1

    ordering_string, chosen_ordering, proanima_chosen_ordering = \
        determine_ordering(
            "factoid", ordering)

    f = get_object_or_404(Factoid, pk=factoid_id)
    real_f = f.get_right_subclass()
    if real_f is None:
        raise Http404

    factoid = real_f[1]

    if preview:  # in this case we're just returning a sub-template for
        # info, before the user clicks on the actual
        # page

        return_str = render_block_to_string(
            'pomsapp/record/record_factoid.html',
            'preview_contents',
            {'preview': preview, 'record': factoid,
             'active_ordering': ordering_string,
             'recordsubtype': real_f[0], })
        return HttpResponse(return_str)

    if ajax_flag:
        items = None
        if tab == 'assocfactoidperson_set':
            items = AssocFactoidPerson.objects.filter(
                factoid=factoid).order_by(*chosen_ordering)
        if tab == 'assocfactoidwitness_set':
            items = AssocFactoidWitness.objects.filter(
                factoid=factoid).order_by(*chosen_ordering)
        if tab == 'assocfactoidproanima_set':
            items = factoid.assocfactoidproanima_set.all().order_by(
                *chosen_ordering)
        # NOTE: no ordering for possessions as it'd require ad hoc field-choice
        if tab == 'assocfactoidposs_lands_set':
            items = factoid.assocfactoidposs_lands_set.filter(
                helper_inferred=False)
        if tab == 'assocfactoidposs_alms_set':
            items = factoid.assocfactoidposs_alms_set.filter(
                helper_inferred=False)
        if tab == 'assocfactoidposs_objects_set':
            items = factoid.assocfactoidposs_objects_set.filter(
                helper_inferred=False)
        if tab == 'assocfactoidposs_office':
            items = factoid.assocfactoidposs_office.filter(
                helper_inferred=False)
        if tab == 'assocfactoidposs_pgeneral_set':
            items = factoid.assocfactoidposs_pgeneral_set.filter(
                helper_inferred=False)
        if tab == 'assocfactoidposs_revenuekind_set':
            items = factoid.assocfactoidposs_revenuekind_set.filter(
                helper_inferred=False)
        if tab == 'assocfactoidposs_revenuesilver_set':
            items = factoid.assocfactoidposs_revenuesilver_set.filter(
                helper_inferred=False)
        if tab == 'assocfactoidposs_unfreep_set':
            items = factoid.assocfactoidposs_unfreep_set.filter(
                helper_inferred=False)
        if tab == 'assocfactoidprivileges_set':
            items = factoid.assocfactoidprivileges_set.filter(
                helper_inferred=False)

        if items:
            paginator = Paginator(items, MAX_RESULTS_LENGTH)
            tot = len(items)
            try:
                items = paginator.page(page)
            except (EmptyPage, InvalidPage):
                # If page request is out of range, deliver last page of
                # results.
                items = paginator.page(paginator.num_pages)
            items.extrastuff = paginator_helper(page,
                                                paginator.num_pages)  # add
            # other useful paginator data to the object
            items.ordering = ordering
            items.tot = tot
            items.type = tab  # a string repr of the type, eg 'possessionFact'

            return_str = render(request,
                                'pomsapp/includes/factoid_tabs.html',
                                tab,
                                {'record': factoid,
                                 'active_ordering': ordering_string,
                                 tab: items, })
            return HttpResponse(return_str)

    vals = {}

    # vals['possessionFact'] = source.get_factoids('possession',
    # chosen_ordering)
    # and the ORDERING?
    vals['assocfactoidperson_set'] = AssocFactoidPerson.objects.filter(
        factoid=factoid).order_by(*chosen_ordering)
    vals['assocfactoidwitness_set'] = AssocFactoidWitness.objects.filter(
        factoid=factoid).order_by(*chosen_ordering)
    vals[
        'assocfactoidproanima_set'] = factoid.assocfactoidproanima_set.all(

    ).order_by(
        *chosen_ordering)

    if real_f[0] in ['transaction', 'possession']:
        vals[
            'assocfactoidposs_lands_set'] = \
            factoid.assocfactoidposs_lands_set.filter(
                helper_inferred=False)
        vals[
            'assocfactoidposs_alms_set'] = \
            factoid.assocfactoidposs_alms_set.filter(
                helper_inferred=False)
        vals[
            'assocfactoidposs_objects_set'] = \
            factoid.assocfactoidposs_objects_set.filter(
                helper_inferred=False)
        vals[
            'assocfactoidposs_office'] = factoid.assocfactoidpossoffice.filter(
            helper_inferred=False)
        vals[
            'assocfactoidposs_pgeneral_set'] = \
            factoid.assocfactoidposs_pgeneral_set.filter(
                helper_inferred=False)
        vals[
            'assocfactoidposs_revenuekind_set'] = \
            factoid.assocfactoidposs_revenuekind_set.filter(
                helper_inferred=False)
        vals[
            'assocfactoidposs_revenuesilver_set'] = \
            factoid.assocfactoidposs_revenuesilver_set.filter(
                helper_inferred=False)
        vals[
            'assocfactoidposs_unfreep_set'] = \
            factoid.assocfactoidposs_unfreep_set.filter(
                helper_inferred=False)
        vals[
            'assocfactoidprivileges_set'] = \
            factoid.assocfactoidprivileges_set.filter(
                helper_inferred=False)

    # substitute the contents of the dict with the paginated values
    for k in vals.keys():
        paginator = Paginator(vals[k], MAX_RESULTS_LENGTH)
        tot = len(vals[k])
        try:
            vals[k] = paginator.page(page)
        except (EmptyPage, InvalidPage):
            # If page request is out of range, deliver last page of results.
            vals[k] = paginator.page(paginator.num_pages)
        vals[k].extrastuff = paginator_helper(page,
                                              paginator.num_pages)  # add
        # other useful paginator data to the object
        vals[k].ordering = ordering
        vals[k].tot = tot
        vals[k].type = k  # a string repr of the type, eg 'possessionFact'

    return render(request, 'pomsapp/record/record_factoid.html',
                  {'record': factoid,
                   'permalink': request.get_host() + request.path,
                   'preview': preview,
                   'recordsubtype': real_f[0],
                   'assocfactoidperson_set': vals.get('assocfactoidperson_set',
                                                      None),
                   'assocfactoidwitness_set': vals.get(
                       'assocfactoidwitness_set', None),
                   'assocfactoidproanima_set': vals.get(
                       'assocfactoidproanima_set', None),
                   'assocfactoidposs_lands_set': vals.get(
                       'assocfactoidposs_lands_set', None),
                   'assocfactoidposs_alms_set': vals.get(
                       'assocfactoidposs_alms_set', None),
                   'assocfactoidposs_objects_set': vals.get(
                       'assocfactoidposs_objects_set', None),
                   'assocfactoidposs_office': vals.get(
                       'assocfactoidposs_office', None),
                   'assocfactoidposs_pgeneral_set': vals.get(
                       'assocfactoidposs_pgeneral_set', None),
                   'assocfactoidposs_revenuekind_set': vals.get(
                       'assocfactoidposs_revenuekind_set', None),
                   'assocfactoidposs_revenuesilver_set': vals.get(
                       'assocfactoidposs_revenuesilver_set',
                       None),
                   'assocfactoidposs_unfreep_set': vals.get(
                       'assocfactoidposs_unfreep_set', None),
                   'assocfactoidprivileges_set': vals.get(
                       'assocfactoidprivileges_set', None),
                   }
                  )


# --------
# PLACE
# --------


def place_detail(request, place_id):
    """
    View that shows a place record
    """
    page = request.GET.get('page', False)
    tab = request.GET.get('tab',
                          False)  # I put it here, but it's not necessary yet
    ordering = request.GET.get('ordering', False)
    preview = request.GET.get('preview', False)
    ajax_flag = False
    MAX_RESULTS_LENGTH = 50

    if page and tab:  # ==> then it's an ajax query
        ajax_flag = True
        try:
            page = int(page)
        except ValueError:
            page = 1
    else:
        page = 1
        tab = 1

    ordering_string, chosen_ordering, proanima_chosen_ordering = \
        determine_ordering(
            "place", ordering)

    obj = get_object_or_404(Place, pk=place_id)

    if preview:  # in this case we're just returning a sub-template for
        # info, before the user clicks on the actual
        # page
        return_str = render_block_to_string('pomsapp/record/record_place.html',
                                            'preview_contents',
                                            {'preview': preview, 'record': obj,
                                             'active_ordering':
                                                 ordering_string, })
        return HttpResponse(return_str)

    # ++++
    # now returns the items:
    # ++++
    if ajax_flag:
        items = None
        if tab == 'peopleAssoc':
            items = obj.person_set.all()
        if tab == 'documentAssoc':
            items = obj.charter_set.all()
        # if tab ==  'possessionFact':
        #	items = [x.factpossession for x in obj.helper_factoids.all() if
        # x.inferred_type == "possession"]
        # This function is returning invalid relations
        if tab == 'possessionFact':
            items = [x.factpossession for x in obj.assoc_factoids() if
                     x.inferred_type == "possession"]
        if tab == 'relationshipFact':
            items = obj.factrelationship_set.all()  # in this case the rel
            # to places is another FK
        # if tab ==  'transactionFact':
        #	items = [x.facttransaction for x in obj.helper_factoids.all() if
        # x.inferred_type == "transaction"]
        # This function is returning invalid relations
        if tab == 'transactionFact':
            items = [x.facttransaction for x in obj.assoc_factoids() if
                     x.inferred_type == "transaction"]

        if items:
            paginator = Paginator(items, MAX_RESULTS_LENGTH)
            tot = len(items)
            try:
                items = paginator.page(page)
            except (EmptyPage, InvalidPage):
                # If page request is out of range, deliver last page of
                # results.
                items = paginator.page(paginator.num_pages)
            items.extrastuff = paginator_helper(page,
                                                paginator.num_pages)  # add
            # other useful paginator data to the object
            items.ordering = ordering
            items.tot = tot
            items.type = tab  # a string repr of the type, eg 'possessionFact'
            context = {'record': obj, 'active_ordering': ordering_string,
                       tab: items, }
            return_str = render(
                request,
                'pomsapp/includes/place_tabs.html',
                context)
            return HttpResponse(return_str)

    # IF NOT AJAX

    vals = {}

    # TODO: ordering??? ADD API AS WITH SOURCES?
    vals['peopleAssoc'] = obj.person_set.all()
    vals['documentAssoc'] = obj.charter_set.all()
    # vals['possessionFact'] = [x.factpossession for x in
    # obj.helper_factoids.all() if x.inferred_type == "possession"]
    vals['possessionFact'] = [x.factpossession for x in obj.assoc_factoids() if
                              x.inferred_type == "possession"]
    vals[
        'relationshipFact'] = obj.factrelationship_set.all()  # in this case
    #  the rel to places is another FK
    # vals['transactionFact'] = [x.facttransaction for x in
    # obj.helper_factoids.all() if x.inferred_type ==
    # "transaction"]
    vals['transactionFact'] = [x.facttransaction for x in obj.assoc_factoids()
                               if x.inferred_type == "transaction"]

    if vals['peopleAssoc'] or vals['documentAssoc'] or vals[
            'possessionFact'] or vals['relationshipFact'] or vals[
            'transactionFact']:
        someRelatedValues = True  # flag for template
    else:
        someRelatedValues = False

    # substitute the contents of the dict with the paginated values
    for k in vals.keys():
        paginator = Paginator(vals[k], MAX_RESULTS_LENGTH)
        tot = len(vals[k])
        try:
            vals[k] = paginator.page(page)
        except (EmptyPage, InvalidPage):
            # If page request is out of range, deliver last page of results.
            vals[k] = paginator.page(paginator.num_pages)
        vals[k].extrastuff = paginator_helper(page,
                                              paginator.num_pages)  # add
        # other useful paginator data to the object
        vals[k].ordering = ordering
        vals[k].tot = tot
        vals[k].type = k  # a string repr of the type, eg 'possessionFact'

    return render(request,
                  'pomsapp/record/record_place.html',
                  {'record': obj,
                   'preview': preview,
                   'peopleAssoc': vals['peopleAssoc'],
                   'documentAssoc': vals['documentAssoc'],
                   'possessionFact': vals['possessionFact'],
                   'relationshipFact': vals['relationshipFact'],
                   'transactionFact': vals['transactionFact'],
                   'active_ordering': ordering_string,
                   'someRelatedValues': someRelatedValues,
                   'permalink': request.get_host() + request.path,
                   }
                  )


# --------
# MATRIX
# --------


def matrix_detail(request, matrix_id):
    """
    View that shows a seal-matrix record
    """
    # request.session['queryargs'] = []
    # request.session['activeIDs'] = []
    page = request.GET.get('page', False)

    obj = get_object_or_404(Matrix, pk=matrix_id)

    return render(request,
                  'pomsapp/record/record_matrix.html',
                  {'record': obj,
                   'permalink': request.get_host() + request.path,
                   }
                  )


# --------
# UTILS
# --------


def determine_ordering(objtype, ordering_string, reverse_flag=False,
                       facttype=""):
    """
    From a keyword, returns a list of model-attributes usable for ordering a
    resultsset
    """

    if objtype == "person":
        ORDERINGS = {'date1': ['factoid__from_year', 'factoid__from_month',
                               'factoid__from_day', 'factoid__to_year'],
                     'summary': ['factoid__shortdesc'],
                     'role': ['role__name'],
                     'source': ['factoid__sourcekey__hammondnumber',
                                'factoid__sourcekey__hammondnumb2',
                                'factoid__sourcekey__hammondnumb3'],
                     }
        DEFAULT_ORDERING = "date1"
    elif objtype == "source":
        ORDERINGS = {'primary': ['facttransaction__isprimary', ],
                     'date1': ['from_year', 'from_month', 'from_day',
                               'to_year'],
                     'summary': ['shortdesc'],
                     'titleholder': [
                         'assocfactoidperson__person__persondisplayname', ],
                     }
        DEFAULT_ORDERING = "date1"

    elif objtype == "factoid":
        ORDERINGS = {'personame': ['person__persondisplayname', ],
                     'personrole': ['role__name', ],
                     'orderno': ['orderno', ],
                     # 'posstype' : ['orderno', ] , NO ORDERING FOR
                     # POSSESSIONS AT THE MOMENT
                     # 'possname' : ['orderno', ] ,
                     }
        DEFAULT_ORDERING = "orderno"

    elif objtype == "place":
        ORDERINGS = {'id': ['id', ],
                     }
        DEFAULT_ORDERING = "id"

    if ordering_string and ordering_string.startswith('-'):
        reverse_flag = True
        ordering_string = ordering_string[1:]

    try:
        chosen_ordering = ORDERINGS[ordering_string]
    except BaseException:
        ordering_string = DEFAULT_ORDERING  # by default
        chosen_ordering = ORDERINGS[ordering_string]
    # ProAnima FACTOIDS:
    # the exception!  'assocfactoidproanima_set' uses the property
    # 'factoidtrans'...
    proanima_chosen_ordering = [x.replace('factoid', 'factoidtrans') for x in
                                chosen_ordering]

    if reverse_flag:
        chosen_ordering = ["-" + x for x in chosen_ordering]
        proanima_chosen_ordering = ["-" + x for x in proanima_chosen_ordering]
        return "-" + ordering_string, chosen_ordering, proanima_chosen_ordering
    else:
        return ordering_string, chosen_ordering, proanima_chosen_ordering
