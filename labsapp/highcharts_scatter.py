# Create your test views here...
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext	#needed for passing the conf details

from django.views.decorators.cache import cache_page

import datetime
from random import choice

from pomsapp.models import *
from utils import myutils







@cache_page(0)
def scatter_peopleage(request):
	""" 
	Applied experiment with http://www.highcharts.com/demo/scatter

	X: people's age
	Y: number of people with that age
	
	Mind that we're not showing people with age=0
	Also, I'm reversing the dict so to display age on the Y axis and NofPeople on X

	"""
	import json


	experiment_description = """
	
	The large number of factoids included in the PoMS database allow us to deduce information circa the active years of a person or institution, that is, the period of time during which they were active (also known as floruit dates). 
	From this data, could we get more insight into the average lifespan of (for example) a female person in medieval Scotland? Or of all individuals born within a specific time frame?
		<br /><br />
		This app aims at letting you explore this king of questions by providing mechanisms for querying and visualising the known active years of the individuals mentioned in the database.
		<br /><br />
 		Click on any item to find out more information about it, or to use it as the starting point for other visualizations.
	"""
	
	SCATTER_TITLE = "POMS Agents Active Years"
	SCATTER_SUBTITLE = "Calculated based on Floruits"
	SCATTER_xAxis_TITLE = "N of Agents"
	SCATTER_yAxis_TITLE = "Active Years"
	SCATTER_xAxis_VAL = "people"
	SCATTER_yAxis_VAL = "years"


	 # 4=F, 3=M, 6=M/F, 2=Other, 5=institutions
	
	females = Person.objects.filter(genderkey__id=4).exclude(floruitstartyr__isnull=True, floruitendyr__isnull=True)
	males = Person.objects.filter(genderkey__id=3).exclude(floruitstartyr__isnull=True, floruitendyr__isnull=True)
	unknown = Person.objects.filter(genderkey__id=6).exclude(floruitstartyr__isnull=True, floruitendyr__isnull=True)
	institutions = Person.objects.filter(genderkey__id__in=[2,5]).exclude(floruitstartyr__isnull=True, floruitendyr__isnull=True)
	
	
	def build_age_dict(person_list):
		age_dict = {}
		for p in person_list:
			if p.floruitstartyr and p.floruitendyr:
				age = (p.floruitendyr - p.floruitstartyr)
				if age: 
					try:
						age_dict[age] += 1
					except:
						age_dict[age] = 1
		return age_dict

	def list_from_dict(d, reverseit=False):
		if reverseit:
			return [[v,k] for k,v in d.iteritems()]
		else:
			return d.items()


	graph_data = []
	graph_data += [{'name': 'Females', 'color': 'pink', 
				'data': list_from_dict(build_age_dict(females), True)}]			
	graph_data += [{'name': 'Males', 'color': 'blue', 
				'data': list_from_dict(build_age_dict(males), True)}]
	graph_data += [{'name': 'Unknown', 'color': 'grey', 
				'data': list_from_dict(build_age_dict(unknown), True)}]			
	graph_data += [{'name': 'Institutions', 'color': 'green', 
				'data': list_from_dict(build_age_dict(institutions), True)}]				

	context = { 'series_data' : json.dumps(graph_data), 
				'SCATTER_TITLE' : SCATTER_TITLE,
				'SCATTER_SUBTITLE' : SCATTER_SUBTITLE,
				'SCATTER_xAxis_TITLE' : SCATTER_xAxis_TITLE,
				'SCATTER_yAxis_TITLE': SCATTER_yAxis_TITLE,
				'SCATTER_xAxis_VAL' : SCATTER_xAxis_VAL,
				'SCATTER_yAxis_VAL' : SCATTER_yAxis_VAL,	
				 'experiment_description' : experiment_description,
				 'experiment_title' : 'People active years chart',
	 			}

	return render_to_response('labs/highcharts/scatterpeople.html', 
								context,
								context_instance=RequestContext(request))










@cache_page(0)
def scatter(request):
	""" 
	Experiment with http://www.highcharts.com/demo/scatter
	
	Features: the size of the chart is assigned dynamically, 
	depending on the max/min values you pass!!!
	
	Nb: I have parametrized completely the visuization using tempaltes var
	All the series_data are created here, and passed back as json
	
	"""
	import json
	
	
	SCATTER_TITLE = "Ex"
	SCATTER_SUBTITLE = "Ex"
	SCATTER_xAxis_TITLE = "xAxis"
	SCATTER_yAxis_TITLE = "yAxis"
	SCATTER_xAxis_VAL = "xVal"
	SCATTER_yAxis_VAL = "yVal"
	

	
	data1 = [[300, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0], [155.8, 53.6], 
		[170.0, 59.0], [159.1, 47.6], [166.0, 69.8], [176.2, 66.8], [160.2, 75.2], 
		[172.5, 55.2], [170.9, 54.2], [172.9, 62.5], [153.4, 42.0], [160.0, 50.0], 
		[147.2, 49.8], [168.2, 49.2], [175.0, 73.2], [157.0, 47.8], [167.6, 68.8], 
		[159.5, 50.6], [175.0, 82.5], [166.8, 57.2], [176.5, 87.8], [170.2, 72.8], 
		]
	data2 =	[[161.2, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0], [155.8, 53.6], 
			[170.0, 59.0], [159.1, 47.6], [166.0, 69.8], [176.2, 66.8], [160.2, 75.2], 
			[172.5, 55.2], [170.9, 54.2], [172.9, 62.5], [153.4, 42.0], [160.0, 50.0], 
			[147.2, 49.8], [168.2, 49.2], [175.0, 73.2], [157.0, 47.8], [167.6, 68.8], 
			[159.5, 50.6], [175.0, 82.5], [166.8, 57.2], [176.5, 87.8], [170.2, 72.8], 
			[174.0, 54.5], [173.0, 59.8], [179.9, 67.3], [170.5, 67.8], [160.0, 47.0], ]
			
	data3 = [[174.0, 65.6], [175.3, 71.8], [193.5, 80.7], [186.5, 72.6], [187.2, 78.8], 
				[181.5, 74.8], [184.0, 86.4], [184.5, 78.4], [175.0, 62.0], [184.0, 81.6], 
				[180.0, 76.6], [177.8, 83.6], [192.0, 90.0], [176.0, 74.6], [174.0, 71.0], 
				[184.0, 79.6], [192.7, 93.8], [171.5, 70.0], [173.0, 72.4], [176.0, 85.9], 
				[176.0, 78.8], [180.5, 77.8], [172.7, 66.2], [176.0, 86.4], [173.5, 81.8], 
				[178.0, 89.6], [180.3, 82.8], [180.3, 76.4], [164.5, 63.2], [173.0, 60.9], ]


	data1 = {'name': 'Unknown', 'color': 'rgba(0, 10, 10, .5)', 'data': data1}			
	data2 = {'name': 'Female', 'color': 'rgba(223, 83, 83, .5)', 'data': data2}			
	data3 = {'name': 'Male', 'color': 'rgba(119, 152, 191, .5)', 'data': data3}			
				
	
	context = { 'series_data' : json.dumps([data1, data2, data3]), 
				'SCATTER_TITLE' : SCATTER_TITLE,
				'SCATTER_SUBTITLE' : SCATTER_SUBTITLE,
				'SCATTER_xAxis_TITLE' : SCATTER_xAxis_TITLE,
				'SCATTER_yAxis_TITLE': SCATTER_yAxis_TITLE,
				'SCATTER_xAxis_VAL' : SCATTER_xAxis_VAL,
				'SCATTER_yAxis_VAL' : SCATTER_yAxis_VAL,	
	 			}

	return render_to_response('labs/highcharts/scatter.html', 
								context,
								context_instance=RequestContext(request))







@cache_page(0)
def scatter_example(request):
	""" 
	Experiment with http://www.highcharts.com/demo/scatter

	Features: the size of the chart is assigned dynamically, 
	depending on the max/min values you pass!!!

	"""


	context = { }

	return render_to_response('labs/highcharts/_scatter_example.html', 
								context,
								context_instance=RequestContext(request))










##################
#  
#  AJAX CALLS
#
##################




def iteminfo(request):
	""" ajax call
		needs two args: agenttype, age
	"""
	agenttype = request.GET.get('agenttype') # Females, Males, Unknown or Institutions
	age = request.GET.get('age')   # the transaction was originally constructed from 

	try:
		age = int(age)
	except:
		return HttpResponse("Error with age [=%s]" % str(age))
		
	if agenttype ==  'Females':
		pset = Person.objects.filter(genderkey__id=4).exclude(floruitstartyr__isnull=True, floruitendyr__isnull=True)
	elif agenttype ==  'Males':
		pset = Person.objects.filter(genderkey__id=3).exclude(floruitstartyr__isnull=True, floruitendyr__isnull=True)	
	if agenttype ==  'Unknown':
		pset = Person.objects.filter(genderkey__id=6).exclude(floruitstartyr__isnull=True, floruitendyr__isnull=True)
	elif agenttype ==  'Institutions':
		pset = Person.objects.filter(genderkey__id__in=[2,5]).exclude(floruitstartyr__isnull=True, floruitendyr__isnull=True)	
		
	if agenttype not in ['Females', 'Males', 'Unknown', 'Institutions']:
		return HttpResponse("Error with agenttype [=%s]" % str(agenttype))

	exit = []
	for p in pset:
		if p.floruitstartyr and p.floruitendyr:
			if (p.floruitendyr - p.floruitstartyr) == age:
				exit.append(p)


	return HttpResponse("<br />".join(["<a target='_blank' name='/labs/popularitycloud/ajax/personinfo?item=%d' href='%s'>%s</a>" % (p.id, p.get_absolute_url(), p.persondisplayname) for p in exit]))













