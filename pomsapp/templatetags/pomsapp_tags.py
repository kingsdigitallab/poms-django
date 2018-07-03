from django import template

register = template.Library()

# From DPRR
@register.simple_tag
def add_facet_link(qd, facet, value):
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
    #qd['page'] = 1
    # if 'printme' in qd:
    #     del qd['printme']
    facets = q.getlist('selected_facets', [])
    if len(facet) > 0:
        facet_value = '{0}_exact:{1}'.format(
            facet, value)
        for f in facets:
            if facet in f:
                facets.remove(f)
        if len(value) > 0:
            facets.append(facet_value)
    q.setlist('selected_facets', facets)
    return '?{0}'.format(q.urlencode())

@register.simple_tag
def split_selected_facet(selected_facet):
    # surnames_exact%3AAbraham
    facet, value = selected_facet.split(':')
    facet=facet.replace('_exact','')
    return facet,value

@register.filter
def get_item(dictionary, key):
    if dictionary:
        return dictionary[key]

    return None

@register.filter
def facet_display_name(facet):
    facet_display_names = {
        'person':'People and Institutions',
        'source':'Sources',
        'termsoftenure': 'Terms of tenure',
        'gender':'gender/type',
        'titles':'Titles/occupations',
        'medievalgaelicforename': 'Medieval Gaelic forename',
        'medievalgaelicsurname': 'Medieval Gaelic surname',
        'moderngaelicforename': 'Modern Gaelic forename',
        'moderngaelicsurname': 'Modern Gaelic surame',
        'documenttype':'Document type',
        'documentcategory': 'Document category',
        'grantorcategory': 'Grantor category',
        'placedatemodern':'Place date modern',
        'relationshiptypes':'Relationship types',
        'spiritualbenefites':'Spiritual benefites',
        'transactiontypes':'Transaction types',
        'possoffice':'offices',
        'possunfreepersons': 'Unfree persons',
        'posslands':'Possession lands',
        'possrevkind': 'Revenues in kind',
        'possrevsilver': 'Revenues in silver',


    }
    if facet in facet_display_names:
        return facet_display_names[facet]
    else:
        return facet


