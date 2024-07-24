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
# use JIT to show person to person networks. What they will have in common
# is some factoid (transactions), what is highlighted is also the role the
# person plays in a factoid (reified as a node for now)


#
# problem: when there are lots of data the alignment isn't very good.....
# approaches:
# 1: use edges: http://tuohuang.thoughtworkers.org/?p=148 ?
# 2: fixed positioning of some nodes: is it possible?

# 2012-08-10: I dropped development on this graph library.. moved on to
# sankey graph for now


# DEFAULT JSON FOR TESTING THE APP
# ps: pay attention to the nodeTo / nodeFrom stuff!
to_json = [{"id": "graphnode0",
            "name": "graphnode0",
            "data": {
                  "$color": "#83548B",
                  "$type": "circle",
                "$dim": 10
            },
            "adjacencies": [{
                "nodeTo": "graphnode1",
                "nodeFrom": "graphnode0",
                "data": {"$color": "#557EAA"}
            }, {
                "nodeTo": "graphnode2",
                "nodeFrom": "graphnode0",
                "data": {"$color": "#909291"}
            },
            ],
            },

           {"id": "graphnode1",
            "name": "graphnode1",
            "data": {
                "$color": "#557EAA",
                "$type": "square",
                "$dim": 10
            },
            "adjacencies": [{
                "nodeTo": "graphnode2",
                "nodeFrom": "graphnode1",
                "data": {"$color": "#909291"}
            },
            ],
            },


           {"id": "graphnode2",
            "name": "graphnode2",
            "data": {
                "$color": "#67e061",
                "$type": "triangle",
                "$dim": 10
            },
            "adjacencies": [{
                "nodeTo": "graphnode3",
                "nodeFrom": "graphnode2",
                "data": {"$color": "#557EAA"}
            },
            ],
            },


           {"id": "graphnode3",
            "name": "graphnode3",
            "data": {
                "$color": "#e00909",
                "$type": "star",
                "$dim": 10
            },
            "adjacencies": [{
                "nodeTo": "graphnode4",
                "nodeFrom": "graphnode3",
                "data": {"$color": "#557EAA"}
            },
            ],
            },


           {"id": "graphnode4",
            "name": "graphnode4",
            "data": {
                "$color": "#557EAA",
                "$type": "circle",
                "$dim": 3
            },
            "adjacencies": [{
                "nodeTo": "graphnode1",
                "nodeFrom": "graphnode4",
                "data": {"$color": "#557EAA"}
            },
            ],
            }, ]


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
    except BaseException:  # default
        return HttpResponseRedirect("?id=41&id=7")  # default... try 2 too!
        # return HttpResponse("Error: can't parse IDs")

    common_factoids = p1.get_commonFactoids(p2)
    # return HttpResponse("<br />".join(["%s: <a href='%s' target='_blank'
    # title='Open in POMS'>%s</a>" % (x.inferred_type.upper(),
    # x.get_absolute_url(), x.shortdesc) for x in common_factoids]))

    def build_graph(p1, p2, factoids):

        stuff = []

        # factoids in the middle
        for f in factoids:
            d = {}
            d['id'] = "factoid_%d" % f.id
            d['name'] = f.shortdesc
            d['data'] = {"$color": "#557EAA", "$type": "square", "$dim": 10}
            stuff += [d]

            # >>> p1.get_factoidRole(f1)
            # [<Role: Sealer>]
            # >>> p2.get_factoidRole(f1)
            # [<Role: Party 1>]

        for p in [p1, p2]:
            d1 = {}
            d1['id'] = "agent_%d" % p.id
            d1['name'] = p.persondisplayname
            d1['data'] = {	"$color": "#e00909", "$type": "star", "$dim": 10}
            d1['adjacencies'] = []

            for f in factoids:
                roles = p.get_factoidRole(f)
                # create role nodes in the graph
                for r in roles:
                    r1 = {}
                    r1['id'] = "role_%d%d%d" % (
                        f.id, p.id, r.id)  # so to make it unique
                    r1['name'] = r.name
                    r1['data'] = {
                        "$color": "green",
                        "$type": "circle",
                        "$dim": 3}
                    r1['adjacencies'] = [{"nodeTo": "factoid_%d" % f.id, "nodeFrom": "role_%d%d%d" % (
                        f.id, p.id, r.id), "data": {"$color": "#557EAA"}}]
                    stuff += [r1]

                    # update the person 2 role link too
                    d1['adjacencies'] += [{"nodeTo": "role_%d%d%d" %
                                           (f.id, p.id, r.id), "nodeFrom": "agent_%d" %
                                           p.id, "data": {"$color": "#557EAA"}}]

            stuff += [d1]

        # for p in [p1, p2]:
        #	d1 = {}
        #	d1['id'] =	"agent_%d" % p.id
        #	d1['name'] = p.persondisplayname
        #	d1['data'] = {	"$color": "#e00909", "$type": "star", "$dim": 10}
        #	d1['adjacencies'] = [ {"nodeTo": "factoid_%d" % f.id, "nodeFrom": "agent_%d" % p.id, "data": { "$color": "#557EAA" }} for f in factoids]
        #	stuff += [d1]

        print stuff
        return stuff

    to_json = build_graph(p1, p2, common_factoids)

    context = {'experiment_description': experiment_description,
               'experiment_title': 'Person to Person Network',
               'json': simplejson.dumps(to_json),
               }

    if template == "halfsize":
        template = 'labs/person2person-halfsize.html'
    else:
        template = 'labs/person2person.html'
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))


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
