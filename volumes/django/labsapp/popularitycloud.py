# Create your test views here...
from __future__ import division

from django.http import HttpResponse
from django.shortcuts import render_to_response
# needed for passing the conf details
from django.template import RequestContext
from utils.template import render_block_to_string

import datetime

from pomsapp.models import *
from utils import myutils


def pop_cloud(request):
    option = request.GET.get('option', 'default')
    maxsize = int(request.GET.get('maxsize', 800))

    experiment_description = """
	The PoMS database presents a considerable amount of variation in terms of the quantity of information available for each recorded historical person (or institution). Based on the evidence found in charters, some individuals ended up having a lot of associated information, while others almost none.
	<br />
	In these experiment we attempt to represent visually and interactively this aspect of the data, that is, the 'popularity' of agents.
	<br /><br />
	This visualization creates a 'vertical' tag-cloud based on names of individuals and on the amount of information ('factoids') associated to each of them. The size of the names increases the more items of information about this person or institution is available in the database. <br />This provides the user with an immediate feeling for the varying degrees of 'popularity' of these individuals.
	"""

    people = Person.objects.exclude(helper_totfactoids=None)  # [:1000]

    # constant: the person which has more factoids associated, used for the
    # visualization
    MAX_FACTOIDS = 2936

    def calc(person):
        if option == 'default':
            FACTOIDS = person.helper_totfactoids
            num = FACTOIDS * (maxsize / MAX_FACTOIDS)

            # if FACTOIDS < 2:
            #		FACTOIDS = 2
            if FACTOIDS < 500:
                num = float("%.1f" % num)
                num = num + 3  # we make it a bit bigger

            if FACTOIDS >= 500 and FACTOIDS < 600:
                num = 140 + ((num / 10) / 2)

            if FACTOIDS >= 600 and FACTOIDS < 700:
                num = 160 + ((num / 10) / 2)

            if FACTOIDS >= 700 and FACTOIDS < 900:
                num = 180 + ((num / 10) / 2)

            if FACTOIDS >= 900 and FACTOIDS < 1300:
                num = 220 + ((num / 10) / 2)

            if FACTOIDS >= 1300 and FACTOIDS < 2000:
                num = 270 + ((num / 10) / 2)

            if FACTOIDS >= 2000 and FACTOIDS < 4000:
                num = 340 + ((num / 10) / 2)

        if option == 'default1':  # not used
            FACTOIDS = person.how_many_factoids()
            num = FACTOIDS

        return num

    mylist = []
    for p in people:
        mylist.append((calc(p), p, p.helper_totfactoids))

    return render_to_response('labs/popularitycloud.html',
                              {	'peoplelist': mylist,
                                'experiment_description': experiment_description,
                                'experiment_title': 'Popularity Tag Cloud',
                                },
                              context_instance=RequestContext(request))


def personinfo(request):
    """ ajax call
            only for persons
    """
    item_id = request.GET.get(
        'item')  # item we want info about: Person or Transaction
    if item_id:
        try:
            x = Person.objects.get(pk=int(item_id))
        except BaseException:
            raise Http404
    else:
        raise Http404

    return_str = render_block_to_string('labs/components/snippet_person.html',
                                        'infobox',
                                        {'record': x, })

    return HttpResponse(return_str)
