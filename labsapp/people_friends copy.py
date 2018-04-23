# Create your test views here...
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext	#needed for passing the conf details

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
# - use the divs to build a better layout based on columns..
# - figure what to do with persons that have more than 500 factoids!!! 



# p1.get_commonFactoids(p2)

def index(request):
	"""
	The list of IDs is in normal order (=last one is more recent step in chain): 1, 2, 3
	Since we're using append (=appends at the end), the order is preserverd in the list of Person isntances
	
	persons = [[person, previous_person, TOT_commonFactoids], etc...]
	"""
	obj_id_list = request.GET.getlist('id') # getlist gets all parameters with same name!!!!
	persons = []
	
	if obj_id_list:
		for obj_id in obj_id_list:
			try:
				# print "Iteration: %s" % str(obj_id)
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
	else:
		p = Person.objects.get(pk=186)	#Glasgow Cathedral
		persons.append([p, None, None])
		p.url_stub = get_urlstub(persons)
	
	if not persons:
		raise Http404	

	last_person = persons[-1][0]
	connections = get_connections(last_person)

	experiment_description = """
				The PoMS database contains more than 80000 facts about 20000 people who lived in medieval Scotland. 
				<br />
				How were these people related? Can we explore these connections in a more interactive, game-like manner than the classic database-like structures? 
				<br /><br />
				This experimental app lets you browse incrementally the network of relationships linking
				persons to other persons or institutions. Click on an item to put it into the 'chain of connections', or to explore it further on the main PoMS database. 
				<br /><br />
				The size of the items at the bottom of the screen depends on the number of factoids two agents have in common."""
				
	# maybe: the poms database contains more that 500000 facts about the people o medieval scotlanf.
	# This experimental app lets you browse the network of connections among them in a playful and incremental manner
	# The size of the links depends on the number of factoids two agents have in common.


	# print "Final:" , persons
	
	context = { 'experiment_description' : experiment_description,
				'experiment_title' : 'Dynamic Connections Cloud',
				
				'persons_chain' :  persons,
				'persons_chain_ids' :  [p[0].id for p in persons if p], 
				'last_person' : last_person,
				'connections' : connections, 
				'MAX_URL_STUB' : get_urlstub(persons) }

	return render_to_response('labs/people_friends.html', 
								context,
								context_instance=RequestContext(request))



# 
# 
# def ____index(request):
#	"""
#	The list of IDs is in normal order (=last one is more recent step in chain): 1, 2, 3
#	Since we're using append (=appends at the end), the order is preserverd in the list of Person isntances
#	"""
#	obj_id_list = request.GET.getlist('id') # getlist gets all parameters with same name!!!!
#	persons = []
# 
#	if obj_id_list:
#		for obj_id in obj_id_list:
#			try:
#				p = Person.objects.get(pk=int(obj_id))
#				persons.append(p)
#				p.url_stub = get_urlstub(persons)
#			except:
#				pass
#	else:
#		p = Person.objects.get(pk=186)	#Glasgow Cathedral
#		persons.append(p)
#		p.url_stub = get_urlstub(persons)
# 
#	if not persons:
#		raise Http404	
#	last_person = persons[-1]
#	connections = get_connections(last_person)
# 
#	experiment_description = """How are people related? Do they knew each other? Is the 6 degrees of connection
#				theory valid in the world of POMS? This app lets you browse incrementally the network of relationships linking
#				a person to other persons. <br />
#				The size of the links depends on the number of factoids two agents have in common."""
#	
#	# maybe: the poms database contains more that 500000 facts about the people o medieval scotlanf.
#	# This experimental app lets you browse the network of connections among them in a playful and incremental manner
#	# The size of the links depends on the number of factoids two agents have in common.
# 
#	context = { 'experiment_description' : experiment_description,
#				'experiment_title' : 'Friend of a Friend',
# 
#				'persons_chain' :  persons,
#				'persons_chain_ids' :  [p.id for p in persons if p.0], 
#				'last_person' : persons[-1],
#				'connections' : connections, 
#				'MAX_URL_STUB' : get_urlstub(persons) }
# 
#	return render_to_response('labs/people_friends.html', 
#								context,
#								context_instance=RequestContext(request))
# 


def get_urlstub(person_list):
	"""
	"""
	exit = ""
	for p in person_list:
		exit += "id=%d&" % p[0].id
	return exit # mind that the initial ? is not included


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
			




