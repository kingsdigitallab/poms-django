# Create your views here.
from pomsapp.models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def sna_all(request,id):
    from sna.models import GephiVis
    context = {}
    context['visualisations'] =  GephiVis.objects.all()
    context['viz'] =  GephiVis.objects.get(pk=id)    
    return render_to_response('sna_all.html',context,context_instance=RequestContext(request))
    
def sna_default(request):
    from sna.models import GephiVis
    context = {}
    context['visualisations'] =  GephiVis.objects.all()
    context['viz'] =  GephiVis.objects.all()[0]   
    return render_to_response('sna_all.html',context,context_instance=RequestContext(request))    
    
def sna_js(request,id,style):
    from sna.models import GephiVis
    context = {}
    context['viz'] =  GephiVis.objects.get(pk=id)    
    if style == 'curvy':
        return render_to_response('config_curvy.js',context,context_instance=RequestContext(request),mimetype='application/json')    
    if style == 'straight':
        return render_to_response('config_straight.js',context,context_instance=RequestContext(request),mimetype='application/json')            
        
    
def sna_person(request,id):
    # Very simple view to render SNA page with a tiny snippet of 'doc ready'
    # in order to focus the gephi graph on an individual
    context = {}
    context['person_id'] =  id
    context['type'] = 'family'
    return render_to_response('sna_person.html',context,context_instance=RequestContext(request))

def sna_person_base(request):
    context = {}
    context['type'] = 'family'    
    return render_to_response('sna.html',context,context_instance=RequestContext(request))
    

def sna_grantor(request,id):
    # Very simple view to render SNA page with a tiny snippet of 'doc ready'
    # in order to focus the gephi graph on an individual
    context = {}
    context['person_id'] =  id
    context['type'] = 'grantor'    
    return render_to_response('sna_grantor_person.html',context,context_instance=RequestContext(request))

def sna_grantor_base(request):
    context = {}
    context['type'] = 'grantor'    
    return render_to_response('sna_grantor.html',context,context_instance=RequestContext(request))
