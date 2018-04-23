# Create your test views here...
from __future__ import division

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext	#needed for passing the conf details

import datetime

from pomsapp.models import *
from utils import myutils



# shows a visualization of people's lives(length)
# todo: add born-date ranges as a way to filter people

def lives(request):
	surname = request.GET.get( 'surname', None)
	forename = request.GET.get( 'forename', None)
	date = request.GET.get( 'date', None)
	dateage = request.GET.get( 'age', None)
	RANGESPAN = 10  # constant
	
	experiment_description = """
	The large number of factoids included in the PoMS database allow us to deduce information circa the active years of a person or institution, that is, the period of time during which they were active (also known as floruit dates). 
	From this data, could we get more insight into the average lifespan of (for example) a female person in medieval Scotland? Or of all individuals born within a specific time frame?
		<br /><br />
		This app aims at letting you explore this king of questions by providing mechanisms for querying and visualising the known active years of the individuals mentioned in the database.
		<br /><br />
 		Click on any item to find out more information about it, or to use it as the starting point for other visualizations.
	"""

	# get persons based on filter selected - surname by default: 	
	if not (surname or forename or date):
		surname = 'a'

	if surname:
		if surname == 'none': 
			searchsurname = ''
		else:
			searchsurname = surname
		pp = Person.objects.filter(surname__istartswith=searchsurname)
	if forename:
		if forename == 'none': 
			searchforename = ''
		else:
			searchforename = forename
		pp = Person.objects.filter(forename__istartswith=searchforename)
	if date:
		searchdate = (int(date), int(date) + RANGESPAN)
		pp = Person.objects.filter(floruitstartyr__gte=searchdate[0], floruitstartyr__lt=searchdate[1] )

	def get_person_of_age(dateage):
		x = []
		# 2010-10-20: changed to this to make it faster: not checked yet!
		for p in Person.objects.exclude(floruitstartyr__isnull=True, floruitendyr__isnull=True):
			if p.floruitstartyr and p.floruitendyr: #double checking here...
				age = (p.floruitendyr - p.floruitstartyr)
				if dateage == 'more':
					if age >= 100:
						x.append(p)
				else:
					if age < int(dateage) and age >= (int(dateage) - 10):
						x.append(p)
		return x

	if dateage:
		pp = get_person_of_age(dateage)

	
	# create items for selection bar
	alpha = list("abcdefghilmnopqrstuvz")
	alpha.append('none')
	rangelist = myutils.buildranges(1090, 1330, RANGESPAN) #[('990-1020', (990, 1020))]
	agerange = range(10, 150, 10)
	agerange.append('more')
	
	# generate html, persons are sorted by highest range first
	l = []
	for p in pp:
		if p.floruitstartyr and p.floruitendyr:
			age = (p.floruitendyr - p.floruitstartyr)
			agestars = "*" * age
			l.append((p, agestars, age))
	l = sorted(l, key = lambda p: -(p[0].floruitendyr - p[0].floruitstartyr)) 
	return render_to_response('labs/lives.html', 
								{'peoplelist': l, 
								 'alpha': alpha , 
								 'datesrange' : rangelist,
								 'agerange' : agerange,
								    # the active values, for highlighting on UI
								 'surname' : surname,
								 'forename' : forename,									
								 'activedate' : date,									
								 'activeage' : dateage,	
								 'experiment_description' : experiment_description,
								 'experiment_title' : 'People active years',								
								  } , 
								context_instance=RequestContext(request))
								
					
				
def ajax_lives1(request):								
	obj_id = request.GET.get( 'obj', None)
	
	p = Person.objects.get(pk=obj_id)
	
	stringa = """%s<br /><br />Available factoids: %d<br />Related sources: %d<br />
             	<a target=\"_blank\" href=\"/record/person/%d/\">show on website</a>"""   % (p, p.helper_totfactoids, p.how_many_sources(), p.id)
	
	if obj_id:
		return HttpResponse(stringa)
	else:
		return HttpResponse("not available")							






