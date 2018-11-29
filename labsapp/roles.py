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


# TODO:
# add ajax behaviour with more info on persons, factoids etc..
# add ability to select items


# DEFAULT JSON FOR TESTING THE APP
# note that when populating the graph, if the source and target are not
# objects, Sankey.js assumes they are indices.

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

    p1, p2 = None, None
    experiment_description = """
				This interactive tool lets you browse the relationships among two people.
				<br /><br />
				Each graph starts from .....
				<br /><br />
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
                   'experiment_title': 'Transaction Roles',
                   'p1_opts': p1_opts,
                   'p2_opts': p2_opts,
                   'p1': p1,
                   'p2': p2,
                   }

        template = 'labs/roles.html'
        return render_to_response(template,
                                  context,
                                  context_instance=RequestContext(request))

    common_factoids = p1.get_commonFactoids(p2)

    def build_graph(p1, p2, factoids):
        """
        find in list: [i for i,x in enumerate(testlist) if x == 1]
        approach:
        we put first all p1 roles, then p2 roles, so when we search for p1 indexs we get the fisrt item found. For p2, the second item
        """

        stuff = {"nodes": [], "links": []}
        to_json = []

        def indexes_in_list(testlist, item):
            return [i for i, x in enumerate(testlist) if x == {'name': item}]

        p1rols, p2rols = [], []
        for f in factoids:
            p1rols += p1.get_factoidRole(f)
            p2rols += p2.get_factoidRole(f)

        p1rols = list(set([r.name for r in p1rols]))
        p2rols = list(set([r.name for r in p2rols]))

        stuff["nodes"] += [{'name': x} for x in p1rols]
        stuff["nodes"] += [{'name': f.shortdesc} for f in factoids]
        stuff["nodes"] += [{'name': x} for x in p2rols]

        for factoid in factoids:
            factoidpos = indexes_in_list(stuff["nodes"], factoid.shortdesc)[0]

            for x in p1.get_factoidRole(factoid):
                rolpos = indexes_in_list(stuff["nodes"], x.name)[
                    0]  # first appearance
                # value fixed for now
                stuff["links"] += [{"source": rolpos,
                                    "target": factoidpos, "value": 10}]

            for x in p2.get_factoidRole(factoid):
                try:
                    # get the second appearance, if existing...
                    rolpos2 = indexes_in_list(stuff["nodes"], x.name)[1]
                except BaseException:
                    rolpos2 = indexes_in_list(stuff["nodes"], x.name)[0]

                # value fixed for now
                stuff["links"] += [{"source": factoidpos,
                                    "target": rolpos2, "value": 10}]

        # print stuff, "\n\n"
        return stuff

    if common_factoids:
        to_json = simplejson.dumps(build_graph(p1, p2, common_factoids))
    else:
        to_json = []

    context = {'experiment_description': experiment_description,
               'experiment_title': 'Transactions Roles',
               'json': to_json,
               'p1': p1,
               'p2': p2,
               }

    template = 'labs/roles.html'
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))


#
# FUNCTIONS COPIED/ADAPTED FROM PEOPLE_FRIENDS.PY
#


def get_connections_faster(person_obj):
    """
    Get all persons connected to a given person

    This is a simpler (and faster) version of the original one as it doesnt do any counting

    Mind that this returns a list, not a dictionary

    """
    MAX = 10000
    MINWEIGHT = 1  # other resizing happens in template

    people = []
    for f in person_obj.get_factoids()[:MAX]:
        people += [x.person for x in f.assochelperperson_set.all()
                   if x.person != person_obj]

    return sorted(list(set(people)), key=lambda x: x.persondisplayname)


def get_connections(person_obj):
    """
    Get all persons connected to a given person

    1: get all factoids connected to a person
    2: get all associations related to each factoid
    3: extract all persons mentioned in these associations
    4: aggregate, count and return a dict {personX: N, ..} where N is the number of times this person
    appears in the subset of factoids

    """
    MAX = 10000
    MINWEIGHT = 1  # other resizing happens in template

    associations = []
    for f in person_obj.get_factoids()[:MAX]:
        associations += list(f.assochelperperson_set.all())

    # another way is:
    # associations = []
    # for f in person_obj.get_factoids()[:MAX]:
    #	associations += list(f.assocfactoidperson_set.all()) + list(f.assocfactoidproanima_set.all()) + list(f.assocfactoidwitness_set.all())

    d = {}

    for a in associations:
        if a.person != person_obj:
            try:
                d[a.person] += 1
            except BaseException:
                d[a.person] = MINWEIGHT

    return d


##################
#
#  AJAX CALLS
#
##################


#
#
# def iteminfo(request):
#	""" ajax call
#		id has the form of either 'wi_40' or 'tr_9000'
#		main_transaction_id is used to remember the center of the visualization, and provide dynamic links to
#		change that to another transaction when needed
#	"""
#	item_id = request.GET.get('item') # item we want info about: Person or Transaction
#	main_transaction_id = request.GET.get('main_id')   # the transaction was originally constructed from
#	try:
#		main_transaction_id = int(main_transaction_id)
#	except:
#		pass
#	if item_id[:2] == "wi":
#		try:
#			x = Person.objects.get(pk=int(item_id[3:]))
#			x_type = 'witness'
#			ordering = ['factoid__from_year', 'factoid__from_month', 'factoid__from_day', 'factoid__to_year']
#			ass_factoids = x.get_association_factoids('witness', ordering)
#		except:
#			raise Http404
#	elif item_id[:2] == "tr":
#		try:
#			x = FactTransaction.objects.get(pk=int(item_id[3:]))
#			x_type = 'transaction'
#			ass_factoids = None
#		except:
#			raise Http404
#	else:
#		raise Http404
#
#	return_str = render_block_to_string('labs/components/snippet_witnesses.html',
#										'infobox',
#										{ 'x_type' : x_type, 'item' : x, 'ass_factoids' : ass_factoids,
#										 'main_transaction_id' : main_transaction_id})
#
#	return HttpResponse(return_str)
#
