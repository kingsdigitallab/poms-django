# Create your test views here...
from __future__ import division

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext	#needed for passing the conf details

import datetime

from pomsapp.models import *
from utils import myutils




# TODO : add dialogs when you click on an item / think of other features

def ajax_pop_cloud(request):
	obj_id = request.GET.get( 'obj', None)
	
	if obj_id:
		return HttpResponse(str(obj_id))
	else:
		return HttpResponse("not available")



def pop_cloud(request):
	option = request.GET.get( 'option', 'default')
	maxsize = int(request.GET.get( 'maxsize', 800))
	
	people = Person.objects.exclude(helper_totfactoids=None) #[:2000]
	
	MAX_FACTOIDS = 2936	 # constant: the person which has more factoids associated
	
	def calc(person):
		if option == 'default':
			FACTOIDS = person.helper_totfactoids
			num = FACTOIDS * (maxsize / MAX_FACTOIDS)
			
			# if FACTOIDS < 2:
			#		FACTOIDS = 2			
			if FACTOIDS < 500:				
				num = float("%.1f" % num)
				num = num + 3 # we make it a bit bigger
				
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
	
	return render_to_response('labs/importance1.html', 
								{'peoplelist': mylist,}, 
								context_instance=RequestContext(request))




