from django import template

from pomsapp.models import AssocFactoidPoss_lands, AssocFactoidPerson
from pomsapp.models import Place, FactTransaction, FactPossession
from pomsapp_wagtail.models import HomePage

register = template.Library()

facet_display_names = {
    'person': 'People and Institutions',
    'source': 'Sources',
    'daterange' :'Date ranges',
    'termsoftenure': 'Terms of tenure',
    'gender': 'gender/type',
    'titles': 'Titles/occupations',
    'medievalgaelicforename': 'Medieval Gaelic forename',
    'medievalgaelicsurname': 'Medieval Gaelic surname',
    'moderngaelicforename': 'Modern Gaelic forename',
    'moderngaelicsurname': 'Modern Gaelic surame',
    'documenttype': 'Document type',
    'documentcategory': 'Document category',
    'grantorcategory': 'Grantor category',
    'placedatemodern': 'Place date modern',
    'relationshiptypes': 'Relationship types',
    'spiritualbenefits': 'Spiritual benefits',
    'transactiontypes': 'Transaction types',
    'possoffice': 'offices',
    'possunfreepersons': 'Unfree persons',
    'posslands': 'Possession lands',
    'possrevkind': 'Revenues in kind',
    'possrevsilver': 'Revenues in silver',
    'tenendasoptions': 'Tenendas options',
    'exemptionoptions': 'Exemption options',
    'sicutclause': 'Sicut clause',
    'returnsrenders': 'Returns/renders',
    'nominalrenders': 'Nominal renders',
    'renderdates ': 'Render dates',
    'returnsmilitary': 'Returns military',
    'commonburdens': 'Common burdens',
    'renderdates': 'Render dates',
    'index_type': 'Result type',
    "legalpertinents": "Legal Pertinents",
    "transfeatures": "Transaction Features",
    "sourcesfeatures": " Source Features"

}


# From DPRR
@register.simple_tag
def add_facet_link(qd, facet=None, value=None):
    q = filter_querystring(qd, facet, value)
    return '?{0}'.format(q.urlencode())


@register.simple_tag()
def filter_querystring(qd, facet=None, value=None):
    """Returns a URL with `facet` and its `value` added to the query
        parameters in `qd`.

        :param qd: query paramters to base URLs on
        :type qd: `django.http.QueryDict`pass
        :param facet: name of facet to add
        :type facet: `str`
        :param value: value of facet to add
        :type value: `str`
        :rtype: `str`

        """
    q = qd.copy()
    # qd['page'] = 1
    # if 'printme' in qd:
    #     del qd['printme']
    # if 'index_type' in facet:
    #
    # else:
    if 'order_by' in facet:
        if 'order_by' in q:
            del (q['order_by'])
        if 'page' in q:
            del (q['page'])
    elif 'page' in facet:
        q['page'] = value
    elif 'index_type' in facet:
        q['index_type'] = value
    elif 'clear_all' in facet:
        # Remove all selected facets
        del q['selected_facets']
    else:
        facets = q.getlist('selected_facets', [])
        if len(facet) > 0:
            facet_value = '{0}_exact:{1}'.format(
                facet, value)
            for f in facets:
                if facet in f:
                    facets.remove(f)
            if len(str(value)) > 0 and 'clear' not in str(value):
                facets.append(facet_value)
        q.setlist('selected_facets', facets)
    return q


@register.simple_tag
def add_reset_link(qd, facet=None, value=None):
    """ Filters out date and general query from get string
    to reset search at top"""
    q = qd.copy()
    if 'max_date' in q:
        del (q['max_date'])
    if 'min_date' in q:
        del (q['min_date'])
    if 'q' in q:
        del (q['q'])
    return '?{0}'.format(q.urlencode())


@register.simple_tag
def split_selected_facet(selected_facet):
    # surnames_exact%3AAbraham
    facet, value = selected_facet.split('_exact:')
    # facet=facet.replace('_exact','')
    return facet, value


@register.simple_tag(takes_context=True)
def get_order_by(context, order_by):
    field = 'order_by'

    if field in context:
        context_order_by = context[field][1:] if context[
                                                     field][0] == '-' else \
            context[field]

        if order_by == context_order_by:
            if context[field][0] != '-':
                order_by = '-{}'.format(order_by)

        # context[field] = order_by

    return order_by


@register.filter
def get_item(dictionary, key):
    if dictionary:
        return dictionary[key]

    return None


@register.inclusion_tag('pomsapp/tags/selected_facet.html', takes_context=True)
def selected_facet(context, selected_facet_string):
    facet = ''
    label = ''
    value = ''
    if selected_facet_string:
        facet, value = selected_facet_string.split(':', 1)
        label = facet.replace('_exact', '')
        if label in facet_display_names:
            label = facet_display_names[label]
    return {'label': label, 'facet': facet, 'value': value,
            'querydict': context['querydict']}


@register.filter
def facet_display_name(facet):
    if facet in facet_display_names:
        return facet_display_names[facet]
    else:
        return facet


@register.inclusion_tag('pomsapp/includes/db_navigation.html',
                        takes_context=True)
def local_menu(context, current_page=None):
    """Retrieves the secondary links for the 'also in this section' links -
    either the children or siblings of the current page."""
    menu_pages = []
    label = ''

    if current_page:
        label = current_page.title
        menu_pages = current_page.get_children().filter(
            live=True, show_in_menus=True)

        # if no children, get siblings instead
        if len(menu_pages) == 0:
            menu_pages = current_page.get_siblings().filter(
                live=True, show_in_menus=True)

        if current_page.get_children_count() == 0:
            if not isinstance(current_page.get_parent().specific, HomePage):
                label = current_page.get_parent().title

    # required by the pageurl tag that we want to use within this template
    return {'request': context['request'], 'current_page': current_page,
            'menu_pages': menu_pages, 'menu_label': label}


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.inclusion_tag('pomsapp/tags/breadcrumbs.html',
                        takes_context=True)
def breadcrumbs(context, current_page, extra=None):
    """Returns the pages that are part of the breadcrumb trail of the current
    page, up to the root page."""
    root = context['request'].site.root_page
    if current_page:
        pages = current_page.get_ancestors(
            inclusive=True).descendant_of(root).filter(live=True)
    else:
        pages = None

    return {'request': context['request'], 'root': root,
            'current_page': current_page, 'pages': pages, 'extra': extra}


@register.filter()
def citation_format(obj):
    """
    Outputs a string usable as a citation of a given poms record
    """
    if obj.__class__.__name__ == 'Person':
        return ", no. %d" % obj.id

    elif obj.__class__.__name__ in ('Charter'):  # 'Source',
        return ", H%d/%d/%d" % (
            obj.hammondnumber or 0, obj.hammondnumb2 or 0,
            obj.hammondnumb3 or 0)

    elif obj.__class__.__name__ in ('Matrix'):  # 'Source',
        return " seal-matrix, no. %d" % obj.id

    elif obj.__class__.__name__ in (
            'FactTitle', 'FactPossession', 'FactTransaction',
            'FactRelationship',
            'FactReference'):
        return " %s factoid, no. %d" % (obj.inferred_type, obj.id)

    elif obj.__class__.__name__ in ('Place',):
        return " place, no. %d" % obj.id

    else:
        return "<not available>"


"""
Take an object and make it into an index of places
for output on a map
"""


@register.inclusion_tag('pomsapp/tags/map_results.html',
                        takes_context=True)
def results_map(context, object_list, index_type):
    places = {}
    for result in object_list:
        # Places put in search indexes
        if result.places is not None:
            for p in result.places:
                if p not in places:
                    # Add a new index
                    place = Place.objects.filter(name=p)[0]
                    places[p] = {'place': place, 'people': [], "charters": [],
                                 "factoids": [], "placetypes": [],
                                 "place_types": []}
                    for type in place.place_types.all():
                        places[p]['place_types'].append(type)
                if 'person' in index_type:
                    # name and floruits
                    places[p]['people'].append(
                        {'id': result.object_id,
                         'name':
                             result.persondisplayname,
                         'floruit':
                             result.object.nice_floruits})
                if 'source' in index_type:
                    charter = result.object.charter
                    placedate = ''
                    if charter.placefk:
                        placedate = charter.placefk.name
                    places[p]['charters'].append(
                        {"id": charter.id,
                         #"firmdate": charter.firmdate,
                        "firmdate": placedate,
                         'hammondnumber': result.object.__str__(),
                         "source_tradid":
                             result.object.source_tradid})
                elif 'factoid' in index_type:
                    factoid = None
                    if 'transaction' in result.inferred_type:
                        factoid = FactTransaction.objects.get(
                            id=result.object_id)
                    elif 'possession' in result.inferred_type:
                        factoid = FactPossession.objects.get(
                            id=result.object_id)
                    if factoid:
                        source = result.object.sourcekey
                        charter = source.charter
                        land = ''
                        # result.object.assocfactoidperson_set.object_list
                        if AssocFactoidPoss_lands.objects.filter(
                                factoid=result.object).count() > 0:
                            pland = AssocFactoidPoss_lands.objects.filter(
                                factoid=result.object)[0]
                            land = pland.poss_land.name
                        if len(result.description) > 50:
                            description = result.description[0:48] + '...'
                        else:
                            description = result.description
                        assoc_persons = AssocFactoidPerson.objects.filter(
                            factoid=result.object
                        )
                        assoc_persons_array = []
                        for assoc_p in assoc_persons:
                            assoc_persons_array.append({
                                'person_id': assoc_p.person.id,
                                'role': assoc_p.role,
                                'person': assoc_p.person
                            })
                        places[p]['factoids'].append({"id": result.object_id,
                                                      'description':
                                                          description,
                                                      'inferred_type':
                                                          factoid.inferred_type,
                                                      # transactiontype
                                                      "name":
                                                          result.source_tradid,
                                                      "possland": land,
                                                      "firmdate":
                                                          charter.firmdate,
                                                      "charter_id": charter.id,
                                                      'hammondnumber':
                                                          result.source.__str__(),
                                                      "assoc_persons":
                                                          assoc_persons_array
                                                      }
                                                     )


                elif index_type is 'place':
                    for type in result.place_types:
                        places[p]['placetypes'].append(type)

                """
                "charters": [{% for charter in p.charter_set.all %}  {"id":{
                { charter.pk}},"name":"{{ charter.source_tradid|safe }}" {% 
                if not forloop.last%} }, {% else %} } {% endif %} {% endfor 
                %} ],
            "placetypes":[{% for type in p.place_types.all %}"{{ type }}"{% 
            if forloop.last %}{% else %},{% endif %}{% endfor %}],
                "place_types":[{% for type in p.place_types.all %}"{{ type 
                }}"{% if forloop.last %}{% else %},{% endif %}{% endfor %}],
                """
    return {'places': places}
