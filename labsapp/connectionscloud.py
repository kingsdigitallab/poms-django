# Create your test views here...
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext	#needed for passing the conf details
from django.utils import simplejson

import datetime

from pomsapp.models import *
from utils import myutils



# Idea: 
# 
# - from two persons we could see how they are related
# 
# - from a person we can browse iteratively the related persons 
#	- the source of the inference should be made clear!

# TODO: 
# - figure what to do with persons that have more than 500 factoids!!! 
	# - thought about paginating.. but it can't be done cause 
		# 1. we still have to go through all factoids in a connection, to calc the weight
		# 2. the ordering of resulting people must be controlled  (this could be fixed easily though)



# p1.get_commonFactoids(p2)

def index(request):
	"""
	The list of IDs is in normal order (=last one is more recent step in chain): 1, 2, 3
	Since we're using append (=appends at the end), the order is preserverd in the list of Person isntances
	
	persons = [[person, previous_person, TOT_commonFactoids], etc...]
	"""
	obj_id_list = request.GET.getlist('id') # getlist gets all parameters with same name!!!!
	persons = []
	
	# maybe: the poms database contains more that 500000 facts about the people o medieval scotlanf.
	# This experimental app lets you browse the network of connections among them in a playful and incremental manner
	# The size of the links depends on the number of factoids two agents have in common.
	experiment_description = """
				The PoMS database contains more than 80000 facts about 20000 people/institutions active in medieval Scotland. How were these individuals connected? Can we explore this network in a more interactive, game-like manner than the classic database-like structures?
				<br /><br />
				This experimental app lets you browse incrementally the network of relationships linking persons/institutions to other persons/institutions. 
				Since each of them is normally participating in more than one event or situation (e.g., a transaction or a relationship factoid), we can attempt to reconstruct the network of interconnections by examining the appearance of individuals within the same event or situation.
				<br /><br />
				To this end, this tool lets you choose an individual and start building a 'chain of connections' departing from him/her/it. Each name in the resulting connections-cloud is rendered using a different font and color, depending on the sex and on the number of common factoids being shared with the previously selected items.

				At any time it is possible to go back to the main PoMS database pages in order to find out more about the individuals or factoids emerging from the connections-cloud exploration. Just click on the individual icons, or move the mouse over the links provided in order to discover more options."""
				

	
	if not obj_id_list:
		context = { 'experiment_description' : experiment_description,
					'experiment_title' : 'Dynamic Connections Cloud',

					'persons_chain' :  None,
					}

		return render_to_response('labs/connectionscloud.html', 
									context,
									context_instance=RequestContext(request))
	else:
		for obj_id in obj_id_list:
			try:
				if obj_id == "random--random":
					import random
					n = random.randrange(0, 22000)
					candidates = Person.objects.filter(id__gt=n, id__lt=n+500)
					p = candidates[random.randrange(0, len(candidates))]
				else:
					p = Person.objects.get(pk=int(obj_id))
				if len(persons) > 0:
					prev_person = persons[-1][0]
					cmonFactoids = len(p.get_commonFactoids(prev_person))
				else:
					prev_person, cmonFactoids = None, None
				# print [p, prev_person, cmonFactoids]
				persons.append([p, prev_person, cmonFactoids])
				p.url_stub = get_urlstub(persons)
			except:
				pass
	
	if not persons:
		raise Http404	

	last_person = persons[-1][0]
	connections = get_connections(last_person)

	# print "Final:" , persons
	
	context = { 'experiment_description' : experiment_description,
				'experiment_title' : 'Dynamic Connections Cloud',
				
				'persons_chain' :  persons,
				'persons_chain_ids' :  [p[0].id for p in persons if p], 
				'last_person' : last_person,
				'connections' : connections, 
				'MAX_URL_STUB' : get_urlstub(persons) }

	return render_to_response('labs/connectionscloud.html', 
								context,
								context_instance=RequestContext(request))



def get_urlstub(person_list):
	"""
	"""
	exit = ""
	for p in person_list:
		exit += "id=%d&" % p[0].id
	return exit # mind that the initial ? is not included





# 2012-08-17: new version that passes factoids lists rather than counts
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
			except:
				d[a.person] = [a.factoid]

	return d



# OLD VERSION 2012-08-17 removed
def __get_connections(person_obj):
	"""
	Get all persons connected to a given person
	
	1: get all factoids connected to a person
	2: get all associations related to each factoid
	3: extract all persons mentioned in these associations
	4: aggregate, count and return a dict {personX: N, ..} where N is the number of times this person 
	appears in the subset of factoids
	
	"""
	MAX = 10000
	MINWEIGHT = 1  #other resizing happens in template
	
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
			except:
				d[a.person] = MINWEIGHT

	return d







# AJAX view

def getCommonConnections(request):
	obj_id_list = request.GET.getlist('id') # getlist gets all parameters with same name!!!!
	persons = []
	
	if len(obj_id_list) >= 2:
		try:
			p1 = Person.objects.get(pk=int(obj_id_list[0]) )
			p2 = Person.objects.get(pk=int(obj_id_list[1]) )
		except:
			return HttpResponse("Error: can't parse IDs")
		
	else:
		return HttpResponse("Error: number of IDs < 2")

			 
		
	common_factoids = p1.get_commonFactoids(p2)
	return HttpResponse("<br />".join(["%s: <a href='%s' target='_blank' title='Open in POMS'>%s</a>" % (x.inferred_type.upper(), x.get_absolute_url(), x.shortdesc) for x in common_factoids]))
			




def autocomplete_people(request):
	""" view used to return a selection of people"""
	results = []
	if request.method == "GET":
		if request.GET.has_key(u'term'):
			value = request.GET[u'term']
			model_results = Person.objects.filter(persondisplayname__icontains=value)[:60]
			results = [ {'label':x.persondisplayname, 'value':x.id} for x in model_results ]	
			json = simplejson.dumps(results)
			return HttpResponse(json, mimetype='application/json')
	return HttpResponse("")

