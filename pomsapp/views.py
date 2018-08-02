# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from haystack.generic_views import FacetedSearchView
from haystack.query import SearchQuerySet

from pomsapp.forms import PomsFacetedSearchForm, PomsFacetedBrowseForm


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
    return render_to_response(request, 'pomsapp/admin_overview.html',
                              context)


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

        max = SearchQuerySet().all().order_by('-startdate')[0]
        max_date = max.startdate
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
            if 'min_date' in form.cleaned_data:
                querystring += '&min_date={}'.format(
                    form.data['min_date']
                )

            if 'max_date' in form.cleaned_data:
                querystring += '&max_date={}'.format(
                    form.cleaned_data['max_date']
                )

            if 'q' in form.cleaned_data:
                querystring += '&q={}'.format(
                    form.cleaned_data['q']
                )
            context['querystring'] = querystring
            context['form'] = form
        context['min_date'] = PomsFacetedSearchForm.DATE_MINIMUM
        context['max_date'] = max_date
        if 'order_by' in self.request.GET:
            context['order_by'] = self.request.GET['order_by']
        return context


class PomsFacetedBrowse(FacetedSearchView):
    """The full faceted view, with all categories
    Is configured in browse urls to pass ajax snippets as well
    """
    form_class = PomsFacetedBrowseForm
    queryset = SearchQuerySet()
    load_all = True
    template_name = 'pomsapp/browse/browse_main.html'
    ajax = False
    facet_fields = ['index_type']
    index_type = 'person'

    facet_group_fields = {
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
            "language",
            'sourcesfeatures'
        ],
        "relationship": [
            "relationshiptypes",
            "roles",
            "spiritualbenefits"
        ],
        "transaction": [
            "transactiontypes",
            "transfeatures",
            "possoffice",
            "possunfreepersons",
            'posslands',
            'possrevkind',
            'possrevsilver',
            'privileges',
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
            "commonburdens",
            "legalpertinents"
        ]

    }

    result_types = [{'label': 'Factoids',
                     'uniquename': 'factoid',
                     },
                    {'label': 'Sources',
                     'uniquename': 'source',
                     # at the moment the name can't be changed cause the js
                     # uses iT!
                     },
                    {'label': 'People and Institutions',
                     'uniquename': 'person',
                     },
                    {'label': 'Places',
                     'uniquename': 'place',
                     }
                    ]

    def __init__(self, *args, **kwargs):
        super(PomsFacetedBrowse, self).__init__(*args, **kwargs)
        if 'facet_group' in kwargs:
            self.facet_group = kwargs['facet_group']
        if 'facet_name' in kwargs:
            self.facet_name = kwargs['facet_name']

        # if self.ajax and self.ajax_facet is not None:
        #     self.facet_fields = self.facet_fields + self.facet_group_fields[
        #         self.ajax_facet
        #     ]

    @staticmethod
    def __facet_by_group(queryset, group):
        """Apply a list of fields as facets to queryset"""
        for field_name in group:
            queryset = queryset.facet(
                field_name, sort='index', limit=-1, mincount=1
            )
        return queryset

    def get_queryset(self):
        """Add facets to queryset
        all if not ajax, or only one facet group if ajax"""
        queryset = super(PomsFacetedBrowse, self).get_queryset()
        if self.ajax and 'facet_group' in self.kwargs:
            queryset = self.__facet_by_group(
                queryset,
                self.facet_group_fields[self.kwargs['facet_group']]
            )
        else:
            for facet_group_name, facet_fields in self.facet_group_fields.items():
                queryset = self.__facet_by_group(
                    queryset,
                    facet_fields
                )

                # Narrow by index type
        if 'selected_facets' in self.request.GET:
            for facet in self.request.GET.getlist('selected_facets'):
                if 'index_type' in facet:
                    self.index_type = facet.replace('index_type_exact:','')
        else:
            self.index_type = 'person'
        queryset = queryset.narrow(
            'index_type:{}'.format(
                self.index_type
            )
        )
        # todo add view's order as well?
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(
            PomsFacetedBrowse, self
        ).get_context_data(*args, **kwargs)
        qs = self.request.GET.copy()
        context['index_type'] = self.index_type
        if self.request.GET.getlist('selected_facets'):
            context['selected_facets'] = qs.getlist('selected_facets')
        if 'facet_group' in self.kwargs:
            context[
                'facet_group'] = self.kwargs['facet_group']
        if 'facet_name' in self.kwargs:
            context[
                'facet_name'] = self.kwargs['facet_name']
            context[
                'facet_group_fields'] = [self.kwargs['facet_name']]
        else:
            context[
                'facet_group_fields'] = self.facet_group_fields

        context['querydict'] = qs.copy()
        context['result_types'] = self.result_types

        return context
