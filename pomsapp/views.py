# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from haystack.generic_views import FacetedSearchView
from haystack.query import SearchQuerySet

from pomsapp.forms import PomsFacetedSearchForm
from pomsapp.search_indexes import PomsIndex


def admin_overview(request):
    from django.db.models import get_models, get_app
    app = get_app('pomsapp')
    mm = [(m._meta.verbose_name_plural.capitalize(), m.objects.count()) for m
          in
          sorted(get_models(app), key=lambda x: x.__name__)]

    try:
        from helpdesk.models import Ticket
        open_and_solved = Ticket.objects.filter(status__in=[1, 3]).order_by(
            '-modified')
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
    Main search for POMS
    """
    facet_fields = ['index_type']
    people_facet_Fields = [
        "surnames",
        "forenames",
        "gender",
        "titles",
        'institutions',
        'medievalgaelicforename',
        'medievalgaelicsurname',
        'moderngaelicforename',
        'moderngaelicsurname',
    ]
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
                querystring += '&date_range={}'.format(
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


class PomsFacetedBrowse(PomsFacetedSearchView):
    """The full faceted view, with all categories
    Is configured in browse urls to pass ajax snippets as well
    """
    template_name = 'pomsapp/browse/facetedbrowser.html'
    ajax = False
    ajax_facet = None

    facet_fields = {
        "person": [
            "surnames",
            "forenames",
            "gender",
            "titles",
            'institutions',
            'medievalgaelicforename',
            'medievalgaelicsurname',
            'moderngaelicforename',
            'moderngaelicsurname',
        ],
        "source": [
            "documenttype",
            "documentcategory",
            "grantorcategory",
            "placedatemodern",
            "language"
        ],
        "relationship": [
            "relationshiptypes",
            "roles",
            "spiritualbenefits"
        ],
        "transaction": [
            "transactiontypes",
            "offices",
            "possunfreepersons",
            'posslands',
            'possrevkind',
            'possrevsilver'
            'privileges'
            'places'
        ],
        'termsoftenure': [
            'tenendasoptions',
            "exemptionoptions",
            "sicutclause",
            "returnsrenders",
            "nominalrenders",
            "renderdates",
            "returnsmilitary",
            "commonburdens"
        ]

    }

    def get_queryset(self):
        """Add facets to queryset
        all if not ajax, or only one facet group if ajax"""
        queryset = super(PomsFacetedBrowse, self).get_queryset()
        if not self.ajax:
            for field_name, field in PomsIndex.fields.items():
                if field.faceted:
                    queryset = queryset.facet(
                        field_name, sort='index', limit=-1, mincount=1
                    )
        elif self.ajax and self.ajax_facet is not None:
            for field_name in self.facet_fields[self.ajax_facet]:
                queryset = queryset.facet(
                    field_name, sort='index', limit=-1, mincount=1
                )
            # todo add view's order as well?
        return queryset
