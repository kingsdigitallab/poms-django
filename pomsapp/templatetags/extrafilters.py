from django.template import Library
import re
from django import template
from django.template.defaultfilters import stringfilter
import random
register = template.Library()


MONTHS_ABBREVIATIONS = {'January': 'Jan.', 'February': 'Feb.',
                        'March': 'Mar.',
                        'April': 'Apr.', 'May': 'May', 'June': 'Jun.',
                        'July': 'Jul.',
                        'August': 'Aug.', 'September': 'Sept.',
                        'October': 'Oct.',
                        'November': 'Nov.', 'December': 'Dec.'}


register = Library()


@register.filter(name='strip_empty_lines')
def strip_empty_lines(value):
    """Return the given HTML with empty and all-whitespace lines removed."""
    return re.sub(r'\r\n', '', value)


@register.filter(name='citation_format')
def citation_format(obj):
    """
    Outputs a string usable as a citation of a given poms record
    """
    if obj.__class__.__name__ == 'Person':
        return ", no. %d" % obj.id

    elif obj.__class__.__name__ in ('Charter'):		# 'Source',
        return ", H%d/%d/%d" % (obj.hammondnumber or 0,
                                obj.hammondnumb2 or 0, obj.hammondnumb3 or 0)

    elif obj.__class__.__name__ in ('Matrix'):		# 'Source',
        return " seal-matrix, no. %d" % obj.id

    elif obj.__class__.__name__ in ('FactTitle', 'FactPossession',
                                    'FactTransaction', 'FactRelationship',
                                    'FactReference'):
        return " %s factoid, no. %d" % (obj.inferred_type, obj.id)

    elif obj.__class__.__name__ in ('Place',):
        return " place, no. %d" % obj.id

    else:
        return "<not available>"


@register.filter(name='generate_labslinks')
def generate_labslinks(obj):
    """
    Generate links to the labs section from the records
    (depending on rec type)

    Omitted for now: 'Source', 'FactTitle', 'FactPossession',
    'FactTransaction', 'FactRelationship', 'FactReference'

    """
    if obj.__class__.__name__ == 'Person':
        return "<ul><li><a href='#'>Connections Cloud [%d]</a></li><li>\
            <a href='#'>Person Rels</a></li></ul>" % obj.id

    elif obj.__class__.__name__ in ('Charter'):		# 'Source',
        return ""

    elif obj.__class__.__name__ in ('FactTransaction',):
        return "<ul><li><a href='#'>link1 - %d</a></li><li>\
            <a href='#'>link2</a></li></ul>" % obj.id
    else:
        return ""


@register.filter(name='cleancss')
def cleancss(stringa):
    """
    Eliminates from a string the characters CSS don't like
    """
    return stringa.replace("/", "")


@register.filter(name='person_assocfactoids')
def person_assocfactoids(person, whattype=""):
    """
    From a person, return the association-factoids instances of given type,
    using the model method <get_association_factoids>
    """
    return person.get_association_factoids(whattype)


@register.filter(name='determinePersonIcon')
def determinePersonIcon(person, return_icon_file=False):
    """
    Determine the icon for records
    """
    if person.genderkey.id in [4, 3, 6]:  # 4=F, 3=M, 6=M/F
        if return_icon_file:
            return "person-icon.png"
        else:
            return "personicon"
    else:
        if return_icon_file:
            return "institution-icon.png"
        else:
            return "institutionicon"


@register.filter(name='determinePersonIcon2')
def determinePersonIcon2(person, return_icon_file=False):
    """
    Determine the icon for records: Females are separated too
    """
    if person.genderkey.id in [3, 6]:  # 3=M, 6=M/F
        if return_icon_file:
            return "person-icon.png"
        else:
            return "personicon"
    elif person.genderkey.id == 4:  # 4=F,
        if return_icon_file:
            return "woman-icon.jpg"
        else:
            return "femaleicon"
    else:
        if return_icon_file:
            return "institution-icon.png"
        else:
            return "institutionicon"


@register.filter(name='infer_class')
def infer_class(active_ordering, element):
    """
    In snippet_results.html: the columns can be ordered but
    depending on <active_ordering> and which element
    we're considering, the class changes, so that the up/down
    icon is shown accordingly.
    Note that we're allowing ordering on one column at a time only.
    """
    if active_ordering and active_ordering[0] == "-":
        if active_ordering[1:] == element:
            return "arrowDown"
    elif active_ordering and active_ordering == element:
        return "arrowUp"
    else:
        return ""


# 2010-06-24
@register.filter(name='format_dates')
def format_dates(stringa):
    if not stringa:  # fix if it's None
        stringa = ""
    if stringa:
        for month in MONTHS_ABBREVIATIONS.keys():
            if month in stringa:
                stringa = stringa.replace(month, MONTHS_ABBREVIATIONS[month])
    return stringa


@register.filter(name='cloudeffect1')
def cloudeffect1(arg):
    """ used in friend of a friend view"""
    CONSTANT = 10
    return CONSTANT + (int(arg) / 2)


# {{d.tot|multiply:'5'}}
@register.filter(name='multiply')
def multiply(value, arg):
    return int(value) * int(arg)


@register.filter(name='add')
def add(value, arg):
    return int(value) + int(arg)


@register.filter(name='randomnumber')
def randomnumber(value):
    return int(value) * (random.random() * 10)


@register.filter(name='cut')
@stringfilter
def cut(value, arg):
    return value.replace(arg, '')


# 2010-06-24
@register.filter(name='latest_updated')
def latest_updated(lst, object_label=None):
    e = []
    if lst:
        e = lst.order_by('-updated_at')
    return e


# older stuff:
# useful in expressing values from a M2M relation: returns all of them
# separated by ';'
@register.filter(name='printmany')
def printmany(lst, object_label=None):
    e = ""
    if lst:
        n = len(lst)
        if not object_label:
            for x in range(n - 1):
                e += "%s; " % (lst[x])
            e += "%s" % (lst[n - 1])
        else:
            for x in range(n - 1):
                label = getattr(lst[x], object_label) or getattr(lst[x], 'id')
                e += "%s; " % (label)
            label = getattr(lst[n - 1],
                            object_label) or getattr(lst[n - 1],
                                                     'id')
            e += "%s" % (getattr(lst[n - 1], object_label))
    return e


# as above, but also creates the link from the get_absolute_url method
# NEEDS THE SAFE filter too! >>>>>>>
# objects.all|printmany_withabsoluteurl|safe
@register.filter(name='printmany_withabsoluteurl')
def printmany_withabsoluteurl(lst, object_label=None):
    e = ""
    if lst:
        n = len(lst)
        if object_label:
            for x in range(n - 1):
                label = getattr(lst[x], object_label) or getattr(lst[x], 'id')
                e += "<a  href=\"%s\">%s</a>; " % (
                    lst[x].get_absolute_url(), label)
            label = getattr(
                lst[n - 1], object_label) or getattr(lst[n - 1], 'id')
            e += "<a  href=\"%s\">%s</a>" % (
                lst[n - 1].get_absolute_url(),
                getattr(lst[n - 1], object_label))
        else:
            for x in range(n - 1):
                e += "<a  href=\"%s\">%s</a>; " % (
                    lst[x].get_absolute_url(), lst[x])
            e += "<a  href=\"%s\">%s</a>" % (
                lst[n - 1].get_absolute_url(), lst[n - 1])
        # e += "%s" % (lst[n -1])
    return e


# {{d.document|make_absolute_url:'id'|safe}}
@register.filter(name='make_absolute_url')
def make_absolute_url(obj, object_label=None):
    e = ""
    if obj:
        if object_label:
            label = getattr(obj, object_label) or getattr(obj, 'id')
            e = "<a href=\"%s\">%s</a>" % (obj.get_absolute_url(), label)
        else:
            e = "<a href=\"%s\">%s</a>" % (obj.get_absolute_url(), obj)
    return e


# {{d.document|poms_italic:'id'|safe}}
@register.filter(name='poms_italic')
def poms_italic(stringa):
    """
    Manually replacing the first 3 appearances of poms-italic syntax
    Not very elegant, but it gets the job done
    """
    try:
        s = stringa.replace("_", "<em>", 1)
        s = s.replace("_", "</em>", 1)
        s = s.replace("_", "<em>", 1)
        s = s.replace("_", "</em>", 1)
        s = s.replace("_", "<em>", 1)
        s = s.replace("_", "</em>", 1)
    except BaseException:
        s = stringa.__unicode__()
        s = s.replace("_", "<em>", 1)
        s = s.replace("_", "</em>", 1)
        s = s.replace("_", "<em>", 1)
        s = s.replace("_", "</em>", 1)
        s = s.replace("_", "<em>", 1)
        s = s.replace("_", "</em>", 1)
    return s


# margin-left: {{forloop.counter0|peopletree_indent}}px;
@register.filter(name='peopletree_indent')
def peopletree_indent(n):
    return n * 20
