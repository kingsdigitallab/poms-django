from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render

from pomsapp.models import *
from utils.myutils import *


# 2012-06-15: commented this as it's not needed!
# RESULT_TYPES	 = [{	'label' : 'Factoids', 
# 						'uniquename' : 'factoid', 
# 						'infospace' : Factoid	},
# 						
# 					 {	'label' : 'Sources', 
# 						'uniquename' : 'source',  
# 						'infospace' : Source	},
# 						
# 					 {	'label' : 'People and Institutions', 
# 						'uniquename' : 'people', 
# 						'infospace' : Person ,  }
# 						
# 					{	'label' : 'Places', 
# 						'uniquename' : 'place', 
# 						'infospace' : Place ,  }
# 					]


##################
#  Wed Oct 13 16:18:19 BST 2010
#  Basic Search:
#
##################	


def basic_search(request):
    # request.session['queryargs'] = []   WHY DO WE NEED TO ZERO THEM? CAUSES INCONSISTENCIES.. DBCHECK
    # request.session['activeIDs'] = []
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    query = request.GET.get('query', False)
    show_all = request.GET.get('show_all', "false")
    basic_search_type = request.GET.get('basic_search_type', 'people')
    ordering = request.GET.get('ordering', '')
    years = request.GET.get('years', '1093-1314')
    ALL_YEARS = '1093-1314'

    valid_restypes = {'people': Person, 'source': Charter, 'factoid': Factoid, 'place': Place}
    print("KEYWORD SEARCH: query= %s  basic_search_type= %s show_all= %s" % (query, basic_search_type, show_all))

    # launch the query [2011-05-27= if there's no query, show all results]
    if basic_search_type and (basic_search_type in valid_restypes) and (query or (show_all == "true")):
        # ---1: set ordering : if not provided in GET, keep track of the default value
        new_ordering_string, chosen_ordering = determine_ordering(basic_search_type, ordering)

        # ---2: set dates
        if years != ALL_YEARS:
            try:
                year1 = int(years.split('-')[0])
                year2 = int(years.split('-')[1])
                if basic_search_type == 'people':
                    items_list = valid_restypes[basic_search_type].objects.filter(floruitstartyr__gte=year1,
                                                                                  floruitendyr__lte=year2)
                elif basic_search_type == 'place':
                    items_list = valid_restypes[basic_search_type].objects.all()
                else:
                    items_list = valid_restypes[basic_search_type].objects.filter(from_year__gte=year1,
                                                                                  from_year__lte=year2)
            except:
                print("BASIC_SEARCH: exception with years.. can't parse..")
                years = ALL_YEARS
                items_list = valid_restypes[basic_search_type].objects.all()
        else:
            items_list = valid_restypes[basic_search_type].objects.all()

        # ---3: set query string
        if query:
            query_split = query.split()  # search for individual components using AND ++> more results!
            for x in query_split:
                items_list = items_list.filter(helper_keywordsearch__icontains=x)
        else:
            query = ""

        if items_list:
            items_list = items_list.order_by(*chosen_ordering)
            # PAGINATION
            paginator = Paginator(items_list, 50)  # Show 15 contacts per page

            try:
                items = paginator.page(page)
            except (EmptyPage, InvalidPage):  # If page request is out of range, deliver last page of results.
                items = paginator.page(paginator.num_pages)
            # add other useful paginator data to the object
            items.extrastuff = paginator_helper(page, paginator.num_pages)

            ordering = ordering or new_ordering_string
            context = {
                'items': items,
                'totitems': len(items_list),
                'query': query,
                'show_all': show_all,
                'active_result_type': basic_search_type,  # make sure we're showing the people result box
                'active_ordering': ordering,
                'active_years': years,
                'user_is_logged_in': request.user.is_authenticated(),
            }
        else:
            # if we have no results:
            context = {
                'items': None,
                'totitems': 0,
                'query': query,
                'show_all': show_all,
                'active_result_type': basic_search_type,  # make sure we're showing the people result box
                'active_ordering': ordering,
                'active_years': years,
                'user_is_logged_in': request.user.is_authenticated(),
            }


    else:  # if the query parameters passed are wrong....
        context = {
            'items': None,
            'query': '',
            'show_all': show_all,
            'active_result_type': None,  # make sure we're showing the people result box
            'active_ordering': ordering,
            'active_years': years,
            'user_is_logged_in': request.user.is_authenticated(),
        }

    return render('pomsapp/search/search.html',
                  context
                  )


def determine_ordering(result_type, ordering, reverse_flag=False):
    """
    From a keyword, returns a list of model-attributes usable for ordering a resultsset
    """

    ORDERINGS = {'sourcehammond': ['hammondnumber', 'hammondnumb2', 'hammondnumb3'],
                 'sourcedate': ['from_year', 'from_month', 'from_day', 'to_year'],
                 'sourcedesc': ['description'],
                 'personfull': ['persondisplayname'],
                 'personfore': ['forename'],
                 'personsur': ['helper_searchbigsur'],
                 'personmedieval': ['standardmedievalname'],
                 'persongaelic': ['moderngaelicname'],
                 'persondate': ['floruitstartyr', 'floruitendyr'],
                 'factoiddesc': ['shortdesc'],
                 'factoidtype': ['inferred_type'],
                 'factoidsource': ['sourcekey__helper_hammond'],
                 'factoiddate': ['from_year', 'from_month', 'from_day', 'to_year'],
                 'placename': ['name'],
                 'placeparent': ['parent__name'],
                 }
    DEFAULT_ORDERINGS = {'people': 'personfull',
                         'source': 'sourcehammond',
                         'factoid': 'factoidtype',
                         'place': 'placename'}

    if ordering.startswith('-'):
        reverse_flag = True
        ordering = ordering[1:]

    try:
        chosen_ordering = ORDERINGS[ordering]
    # new_ordering = None
    except:
        ordering = DEFAULT_ORDERINGS[result_type]  # by default
        chosen_ordering = ORDERINGS[ordering]

    # in these cases, also order by date!
    if ordering in ['factoidtype', 'factoidsource']:
        chosen_ordering += ORDERINGS['sourcedate']

    if reverse_flag:
        chosen_ordering = ["-" + x for x in chosen_ordering]
        return "-" + ordering, chosen_ordering
    else:
        return ordering, chosen_ordering
