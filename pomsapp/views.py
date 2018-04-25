# Create your views here.
from pomsapp.models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage




def admin_overview(request):
	from django.db.models import get_models, get_app
	app = get_app('pomsapp')
	mm = [(m._meta.verbose_name_plural.capitalize(), m.objects.count()) for m in sorted(get_models(app), key=lambda x: x.__name__)]
	
	try:
		from helpdesk.models import Ticket
		open_and_solved = Ticket.objects.filter(status__in=[1, 3]).order_by('-modified')		
	except:
		open_and_solved = []
	
	context = {'variable' : None,
				'models' : mm , 
				'open_and_solved' : open_and_solved
				}
	return render_to_response('pomsapp/admin_overview.html', 
							  context,
							  context_instance=RequestContext(request))



