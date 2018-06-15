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
    qd = qd.copy()
    #qd['page'] = 1
    # if 'printme' in qd:
    #     del qd['printme']
    facets = qd.getlist('selected_facets', [])
    if len(facet) > 0:
        for f in facets:
            facet_value = '{0}_exact:{1}'.format(
                facet, value)
            if facet in f:
                facets.remove(f)
            facets.append(facet_value)
    qd.setlist('selected_facets', facets)
    return '?{0}'.format(qd.urlencode())

@register.filter
def get_item(dictionary, key):
    if dictionary:
        return dictionary[key]

    return None