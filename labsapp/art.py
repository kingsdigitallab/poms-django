# Create your test views here...
from __future__ import division

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext	#needed for passing the conf details

import datetime

from pomsapp.models import *
from utils import myutils





