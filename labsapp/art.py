# Create your test views here...
from __future__ import division

from django.http import HttpResponse
from django.shortcuts import render_to_response
# needed for passing the conf details
from django.template import RequestContext

import datetime

from pomsapp.models import *
from utils import myutils
