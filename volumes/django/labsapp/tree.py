
from django.http import HttpResponse
from django.shortcuts import render_to_response
# needed for passing the conf details
from django.template import RequestContext

import datetime

from pomsapp.models import *
from utils import myutils


def tree1(request):
    """
    Experiment with trees
    """

    context = {'items': None}

    return render_to_response('labs/tree1.html',
                              context,
                              context_instance=RequestContext(request))
