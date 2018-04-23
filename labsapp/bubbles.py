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
def index(request):
	""" 
	Experiment with http://moochart.coneri.se/#demo
	"""
	ex = range(1, 200, 10)
	nums = range(choice(ex))
	context = { 'nums' : nums }

	return render_to_response('labs/bubbles.html', 
								context,
								context_instance=RequestContext(request))








