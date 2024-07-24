# Create your test views here...
from django.http import HttpResponse, Http404
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
# use JIT to show transactions -- witnesses - transactions networks


# DEFAULT JSON FOR TESTING THE APP
to_json = {
    'id': "190_0",
    'name': "Pearl Jam",
    'children': [
            {
                'id': "306208_1",
                'name': "Pearl Jam &amp; Cypress Hill",
                'data': {
                        'relation': "<h4>Pearl Jam &amp; Cypress Hill</h4><b>Connections:</b><ul><h3>Pearl Jam <div>(relation: collaboration)</div></h3><h3>Cypress Hill <div>(relation: collaboration)</div></h3></ul>"
                }, },
            {	'id': "191_0",
                'name': "Pink Floyd",
                'children': [{
                        'id': "306209_1",
                        'name': "Guns and Roses",
                        'data': {
                            'relation': "<h4>Pearl Jam &amp; Cypress Hill</h4><b>Connections:</b><ul><h3>Pearl Jam <div>(relation: collaboration)</div></h3><h3>Cypress Hill <div>(relation: collaboration)</div></h3></ul>"
                        },
                }],

              }]}


def index(request, template=None):
    """
    """
    experiment_description = """
				This interactive tool lets you browse the intersections among transaction and witnesses in the PoMS database.
				<br /><br />
				Each graph starts from a transaction of choice (the 'focus point'), and displays two levels of information: (1) all the witnesses of the transaction (normally persons or institutions), and (2) for each of these agents, all the other transactions they have witnessed.
				<br /><br />
				Please note that due to the way the graph is built, the second-level transactions will often refer to witnesses that are not displayed in the graph (since only the first-level transaction has all of its witnesses displayed).
				<br /><br />
				In order to show all of the witnesses of a second-level transaction, you can just re-create the graph by clicking on the '&#164;' symbol (situated on the left of each second-level transaction title, in the info panel).
				"""
    obj_id = request.GET.get(
        'id')  # getlist gets all parameters with same name!!!!
    try:
        transaction = FactTransaction.objects.get(pk=int(obj_id))
    except BaseException:
        # raise Http404
        # t = FactTransaction.objects.exclude(witnesses=None)[1]
        # [1149L, 2360L, 4925L, 6234L, 8208L, 11207L, 15468L, 15650L, 16362L, 16433L]
        transaction = FactTransaction.objects.get(pk=8208)

    def build_tree(trans, level=0):
        d = {}
        d['id'] = "tr_%d" % trans.id
        d['name'] = trans.shortdesc
        d['data'] = {'date': trans.firmdate}
        d['children'] = []
        if level < 1:
            # 2012-07-18: ATTEMPT TO ADD GRANTORs Etc.
            # for assoc in trans.assocfactoidperson_set.filter(role__name__in=['Grantor', 'Beneficiary']):
            # 	sec_person = assoc.person
            # 	dp = {}
            # 	dp['id'] =	"pe_%d" % sec_person.id
            # 	dp['name'] = sec_person.persondisplayname
            # 	dp['data'] = {'secperson' : 1}
            # 	d['children'] += [dp]

            for assoc in trans.assocfactoidwitness_set.all():
                witness = assoc.person
                d1 = {}
                d1['id'] = "wi_%d" % witness.id
                d1['name'] = witness.persondisplayname
                d1['data'] = {}
                d1['children'] = [
                    build_tree(
                        a.factoid.facttransaction,
                        level +
                        1) for a in AssocFactoidWitness.objects.filter(
                        person=witness) if a.factoid.inferred_type == "transaction"]

                d['children'] += [d1]

        return d

    to_json = build_tree(transaction)

    context = {'experiment_description': experiment_description,
               'experiment_title': 'Witnesses Networks',
               'json': simplejson.dumps(to_json),
               'vis_main_transaction': transaction
               }

    if template == "halfsize":
        template = 'labs/witnessesRgraph-halfsize.html'
    else:
        template = 'labs/witnessesRgraph.html'
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))


##################
#
#  AJAX CALLS
#
##################


def iteminfo(request):
    """ ajax call
            id has the form of either 'wi_40' or 'tr_9000'
            main_transaction_id is used to remember the center of the visualization, and provide dynamic links to
            change that to another transaction when needed
    """
    item_id = request.GET.get(
        'item')  # item we want info about: Person or Transaction
    # the transaction was originally constructed from
    main_transaction_id = request.GET.get('main_id')
    try:
        main_transaction_id = int(main_transaction_id)
    except BaseException:
        pass
    if item_id[:2] == "wi":
        try:
            x = Person.objects.get(pk=int(item_id[3:]))
            x_type = 'witness'
            ordering = [
                'factoid__from_year',
                'factoid__from_month',
                'factoid__from_day',
                'factoid__to_year']
            ass_factoids = x.get_association_factoids('witness', ordering)
        except BaseException:
            raise Http404
    elif item_id[:2] == "tr":
        try:
            x = FactTransaction.objects.get(pk=int(item_id[3:]))
            x_type = 'transaction'
            ass_factoids = None
        except BaseException:
            raise Http404
    else:
        raise Http404

    return_str = render_block_to_string('labs/components/snippet_witnesses.html',
                                        'infobox',
                                        {'x_type': x_type, 'item': x, 'ass_factoids': ass_factoids,
                                         'main_transaction_id': main_transaction_id})

    return HttpResponse(return_str)
