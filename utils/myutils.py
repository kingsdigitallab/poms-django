
##################
#  Mon Sep 20 12:59:39 BST 2010
#  just a bunch of utilities...
#  @ copyright michele pasin
##################


def best_encoding(x_to_encode):
    out = None
    if isinstance(x_to_encode, type(1)) or type(x_to_encode):
        out = str(x_to_encode)
    else:
        try:
            out = x_to_encode.encode('utf-8')
        except BaseException:
            try:
                out = x_to_encode.encode('iso-8859-1')
            except BaseException:
                raise Exception("** could not encode **")
                # out = "** could not encode **"
    return out


def blank_or_string(s):
    """If it's empty, output the string blank"""
    if not s.strip():
        return 'blank'
    return s


def preview_string(s, length):
    """If we have a value, returns the first [length] chars of the string.."""
    if s:
        if len(s) < length:
            result = s
        else:
            result = s[0:length] + "..."
        return result


def isint(s):
    """checks if a string is a number"""
    try:
        return int(s)
    except ValueError:
        return False


def findmin(rangen, n):
    e = 0
    while e < n:
        e += rangen
        # returns the one before
    return e - rangen


def findmax(rangen, n):
    e = 0
    while e < n:
        e += rangen
        # returns the one after
    return e


def buildranges(amin, amax, rangeval):
    """Retunrs a list of tuples, with the string-range first and then
     the numbers in a tuple: [('990-1020', (990, 1020)),
     ('1020-1050', (1020, 1050))]  """
    r = []
    allvalues = range(amin, amax, rangeval)
    for index, item in enumerate(allvalues):
        if (index + 1) < len(allvalues):
            a = "%d-%d" % (item, allvalues[index + 1])
            r.append((a, (item, allvalues[index + 1])))
    return r


def split_list_into_two(somelist):
    x = len(somelist)
    z = x / 2
    res1 = somelist[:(x - z)]
    res2 = somelist[(x - z):]
    return [res1, res2]


def group_list_items_by_two(lista, listaexit=None):
    lista_x = []
    listaexit = listaexit or []
    if lista:
        lista_x.extend(lista)
        lista_x.reverse()
        first_el = lista_x.pop()
        if len(lista_x) == 0:
            second_el = None
        else:
            second_el = lista_x.pop()
        listaexit.append([first_el, second_el])
        if lista[2:]:
            group_list_items_by_two(lista[2:], listaexit)
        # print(listaexit)
        return listaexit


filler = ["value_%s" % (i) for i in range(10)]


# given a center, returns a list of the neighbouring numbers according to
# the paramenters passed
def paginator_helper(center, max, howmany=5, interval=1, min=1, ):
    if center - howmany > min:
        min = center - howmany
    if center + howmany < max:
        max = center + howmany
    return range(min, (max + 1), interval)


#  helper for django models : NEVER USED
def get_or_new(model, somename):
    """helper method"""
    try:
        # if there's an object with same name, we keep that one!
        obj = model.objects.get(name=somename)
        print("++++++++++++++++++++++++++ found existing obj:	%s" % (obj))
    except BaseException:
        obj = model(name=somename)
        obj.save()
        print("======= created new obj:	  %s" % (obj))
    return obj
