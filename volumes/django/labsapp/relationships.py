# Create your test views here...
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
# needed for passing the conf details
from django.template import RequestContext
from django.utils import simplejson

import datetime

from pomsapp.models import *
from utils import myutils
from utils.template import render_block_to_string


# Idea:
#
# use a Sankey diagram <http://bost.ocks.org/mike/sankey/> to show person
# to person networks. What they will have in common is some factoid
# (transactions), what is highlighted is also the role the person plays in
# a factoid (reified as a node for now)


# DEFAULT JSON FOR TESTING THE APP
# note that when populating the graph, if the source and target are not objects, Sankey.js assumes they are indices.
# the layout is completely automatic
# IMPORTANT: the way the links are structured, must have an implicit
# 'flow' orientation (= no symmetrical links)

to_json = {"nodes": [
    {"name": "Agricultural 'waste'"},
    {"name": "Bio-conversion"},
    {"name": "Liquid"},
    {"name": "Losses"},
    {"name": "Solid"},
    {"name": "Gas"},
    {"name": "Gas"},
    {"name": "Solid"},
],
    "links": [
        {"source": 0, "target": 1, "value": 124.729},
    # {"source":1,"target":0,"value":0.597},  ==> will fail!
        {"source": 1, "target": 2, "value": 26.862},
        {"source": 1, "target": 3, "value": 26.862},
        {"source": 1, "target": 4, "value": 280.322},
        {"source": 1, "target": 5, "value": 81.144},
        {"source": 6, "target": 5, "value": 81.144},
        {"source": 7, "target": 1, "value": 81.144},
    # {"source":5,"target":0,"value":81.144},  ==> will fail!
]}


def index(request, template=None):
    """
    Ex: use connections of http://127.0.0.1:8000/db/labs/connectionscloud/go?id=41
    [Arbroath Abbey (fd.1178)]	and Dunfermline Abbey (fd.1128) [id=7]

    >>> p1 = Person.objects.get(pk=41)
    >>> p2 = Person.objects.get(pk=7)
    >>> factoids = p1.get_commonFactoids(p2)
    >>> f1 =factoids[0]
    <FactTransaction: id[42197], from source [4/32/24  (_Dunf. Reg._, no. 211)] >
    >>> p1.get_factoidRole(f1)
    [<Role: Sealer>]
    >>> p2.get_factoidRole(f1)
    [<Role: Party 1>]

    """

    GRAPH_HEIGHT = 600  # default

    p1, p2 = None, None
    experiment_description = """
				The individuals and institutions in the PoMS database are often interconnected by participating to the same factoids (e.g. transactions). In particular, the database contains detailed information circa the specific 'roles' these individuals are playing within each factoid.
				<br /><br />
				This experimental interactive visualization allows you to compare the different roles two people/institutions play in the context of their common events. Can we discover any interesting pattern by examining these roles? For example, do individuals tend to appear always in the same role, of are there exceptions to this rule?
				<br /><br />
				Click on the agents names at the top of the page in order to find out more information about them, or to go back to the visualization start page.
				<br />Double click on the coloured boxes so to get more information about the events they represent. You can also drag them to a different position and experiment with alternative visualizations.
				"""

    # getlist gets all parameters with same name!!!!
    obj_id_list = request.GET.getlist('id')

    try:
        p1 = Person.objects.get(pk=int(obj_id_list[0]))
        p2 = Person.objects.get(pk=int(obj_id_list[1]))
    except BaseException:

        # OUTPUTS THE SELECT-PERSON FORM:

        if p1:
            p2_opts = get_connections(p1)
        else:
            p2_opts = []

        if p2:
            p1_opts = get_connections(p2)
        else:
            p1_opts = []

        context = {'experiment_description': experiment_description,
                   'experiment_title': 'Relationships Explorer',
                   'p1_opts': p1_opts,
                   'p2_opts': p2_opts,
                   'p1': p1,
                   'p2': p2,
                   }

        template = 'labs/relationships.html'
        return render_to_response(template,
                                  context,
                                  context_instance=RequestContext(request))

    common_factoids = p1.get_commonFactoids(p2)

    def build_graph(p1, p2, factoids):
        """
        approach:
        In the nodes list we put first all p1 roles, then factoids, then p2 roles.
        This way when we search for p1 indexes (so to build the json format wanted by sankey vis) we get the first items found.
        For p2, the second items.
        We pass id-s too, so to facilitate ajax-info calls.

        Tip:
        find in list: [i for i,x in enumerate(testlist) if x == 1]
        """

        stuff = {"nodes": [], "links": []}
        to_json = []

        def indexes_in_list(testlist, item, n='None'):
            return [i for i, x in enumerate(testlist) if x == {
                'name': item, 'id': n}]

        def factoid_id(f_id):
            return "fa_%s" % str(f_id)

        def role_id(r_id):
            return "ro_%s" % str(r_id)

        p1rols, p2rols = [], []
        for f in factoids:
            p1rols += p1.get_factoidRole(f)
            p2rols += p2.get_factoidRole(f)

        p1rols = list(set([(r.name, r.id) for r in p1rols]))
        p2rols = list(set([(r.name, r.id) for r in p2rols]))

        stuff["nodes"] += [{'name': x, 'id': role_id(y)} for x, y in p1rols]
        stuff["nodes"] += [{'name': f.shortdesc,
                            'id': factoid_id(f.id)} for f in factoids]
        stuff["nodes"] += [{'name': x, 'id': role_id(y)} for x, y in p2rols]

        for factoid in factoids:
            factoidpos = indexes_in_list(
                stuff["nodes"],
                factoid.shortdesc,
                factoid_id(
                    factoid.id))[0]

            for x in p1.get_factoidRole(factoid):
                rolpos = indexes_in_list(
                    stuff["nodes"], x.name, role_id(
                        x.id))[0]  # first appearance
                # value fixed for now
                stuff["links"] += [{"source": rolpos,
                                    "target": factoidpos, "value": 10}]

            for x in p2.get_factoidRole(factoid):
                try:
                    # get the second appearance, if existing...
                    rolpos2 = indexes_in_list(
                        stuff["nodes"], x.name, role_id(x.id))[1]
                except BaseException:
                    rolpos2 = indexes_in_list(
                        stuff["nodes"], x.name, role_id(x.id))[0]

                # value fixed for now
                stuff["links"] += [{"source": factoidpos,
                                    "target": rolpos2, "value": 10}]

        # print stuff, "\n\n"
        return stuff

    if common_factoids:
        to_json = simplejson.dumps(build_graph(p1, p2, common_factoids))
    else:
        to_json = []

    # calc dynamic graph height

    tot = len(common_factoids)

    if tot < 6:
        GRAPH_HEIGHT = 200
    elif tot >= 6 and tot < 50:
        GRAPH_HEIGHT = tot * 30
    else:
        GRAPH_HEIGHT = tot * 25

    context = {'experiment_description': experiment_description,
               'experiment_title': 'Relationships Explorer',
               'json': to_json,
               'p1': p1,
               'p2': p2,
               'graph_height': GRAPH_HEIGHT
               }

    template = 'labs/relationships.html'
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))


#
# FUNCTIONS COPIED/ADAPTED FROM PEOPLE_FRIENDS.PY
#


def get_connections(person_obj):
    """
    Get all persons connected to a given person

    1: get all factoids connected to a person
    2: get all associations related to each factoid
    3: extract all persons mentioned in these associations
    4: aggregate, and return a dict {personX: [f1, f2 etc], ..} where F[..] are the common factoids

    """
    MAX = 10000
    associations = []
    d = {}

    for f in person_obj.get_factoids()[:MAX]:
        associations += list(f.assochelperperson_set.all())

    for a in associations:
        if a.person != person_obj:
            try:
                if a.factoid not in d[a.person]:
                    d[a.person] += [a.factoid]
            except BaseException:
                d[a.person] = [a.factoid]

    return d


# NOT USED: testing revealed that the version above is much faster (2:1)
def __get_connections(person_obj):
    """
    Get all persons connected to a given person

    This is a simpler (and faster) version of the original one as it doesnt do any counting

    Mind that this returns a list, not a dictionary

    """
    MAX = 10000
    d = {}
    people = []

    for f in person_obj.get_factoids()[:MAX]:
        people += [x.person for x in f.assochelperperson_set.all()
                   if x.person != person_obj]

    people = sorted(list(set(people)), key=lambda x: x.persondisplayname)

    for p in people:
        if p != person_obj:
            try:
                d[p] = person_obj.get_commonFactoids(p, count_only=True)
            except BaseException:
                pass

    return d


##################
#
#  AJAX CALLS
#
##################


def iteminfo(request):
    """ ajax call
            id has the form of either 'ro_40' or 'fa_9000'
    """
    item_id = request.GET.get(
        'item')  # item we want info about: Role or Transaction
    if item_id[:2] == "ro":
        # it's a role
        try:
            x = Role.objects.get(pk=int(item_id[3:]))
            x_type = 'role'
        except BaseException:
            raise Http404

        return_str = """%s <a style="font-size:10px;text-transform: none;" href="/browse/?filter=roles_%s&resulttype=people" title="Search in PoMS" target="_blank">&rarr; Search for all People/Institutions with this role</a></span> """ % (
            x.name, x.name)

    elif item_id[:2] == "fa":
        # it's a factoid
        try:
            x = Factoid.objects.get(pk=int(item_id[3:]))
            x_type = 'factoid'
            ass_factoids = None
        except BaseException:
            raise Http404

        return_str = render_block_to_string('labs/components/snippet_factoid.html',
                                            'infobox',
                                            {'item': x, })
    else:
        raise Http404

    return HttpResponse(return_str)
