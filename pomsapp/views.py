# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from haystack.generic_views import FacetedSearchView
from haystack.query import SearchQuerySet
from pomsapp.forms import PomsFacetedSearchForm


def admin_overview(request):
    from django.db.models import get_models, get_app
    app = get_app('pomsapp')
    mm = [(m._meta.verbose_name_plural.capitalize(), m.objects.count()) for m in
          sorted(get_models(app), key=lambda x: x.__name__)]

    try:
        from helpdesk.models import Ticket
        open_and_solved = Ticket.objects.filter(status__in=[1, 3]).order_by('-modified')
    except:
        open_and_solved = []

    context = {'variable': None,
               'models': mm,
               'open_and_solved': open_and_solved
               }
    return render_to_response('pomsapp/admin_overview.html',
                              context,
                              context_instance=RequestContext(request))



class PomsFacetedSearchView(FacetedSearchView):
    """
    Main faceted search for POMS
    """
    facet_fields = ['index_type']
    form_class = PomsFacetedSearchForm
    template_name = 'pomsapp/search/search.html'
    queryset = SearchQuerySet()
    load_all = True


    def get_queryset(self):
        queryset = super(
            PomsFacetedSearchView, self
        ).get_queryset()
        if 'order_by' in self.request.GET:
            return queryset.order_by(
                self.request.GET['order_by']
            )
        else:
            return queryset.order_by('startdate')

    def get_context_data(self, *args, **kwargs):
        context = super(
            PomsFacetedSearchView, self
        ).get_context_data(*args, **kwargs)
        if context['form']:
            form = context['form']
            querystring = ''
            if 'index_type' in form.cleaned_data:
                context['index_type'] = form.cleaned_data['index_type']
                querystring = 'index_type={}'.format(
                    form.cleaned_data['index_type']
                )
            else:
                context['index_type'] = 'person'
            if 'date_range' in form.cleaned_data:
                context['date_range'] = form.cleaned_data['date_range']
                querystring+='&date_range={}'.format(
                    form.cleaned_data['date_range']
                )
            else:
                context['date_range'] = '{}-{}'.format(
                    form.DATE_MINIMUM,
                    form.DATE_MAXIMUM
                )
            if 'q' in form.cleaned_data:
                querystring += '&q={}'.format(
                    form.cleaned_data['q']
                )
            context['querystring'] = querystring
        return context
