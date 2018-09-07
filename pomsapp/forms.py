from django import forms
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet

RESULT_TYPES = [
    ('factoid', 'Factoid'),
    ('person', 'Person'),
    ('source', 'Source'),
    ('place', 'Place'),
]


class PomsFacetedSearchForm(FacetedSearchForm):
    DATE_MINIMUM = 1093
    DATE_MAXIMUM = 1300

    # index_type = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=RESULT_TYPES
    # )

    min_date = forms.IntegerField(
        initial=DATE_MINIMUM
    )

    max_date = forms.IntegerField(
        initial=DATE_MAXIMUM
    )

    def __init__(self, *args, **kwargs):
        super(PomsFacetedSearchForm, self).__init__(*args, **kwargs)
        # get the earliest and latest dates in the whole record set
        min = SearchQuerySet().all().order_by('startdate')[0]
        max = SearchQuerySet().all().order_by('-startdate')[0]
        self.min_date = min.startdate
        self.max_date = max.startdate

    def no_query_found(self):
        """Determines the behaviour when no query was found; returns all the
        results."""
        return self.searchqueryset.all()

    def search(self):

        sqs = super(PomsFacetedSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        if self.is_bound:
            data = self.cleaned_data
            # if data['index_type']:
            #     sqs = sqs.narrow(
            #         'index_type_exact:{}'.format(
            #             data['index_type']
            #         )
            #     )
            # split the character date range into two integers
            # apply to start date
            if 'min_date' in data:
                sqs = sqs.narrow('startdate:[{0} TO {1}]'.format(
                    data['min_date'],
                    data['max_date']
                ))
                # if '-' in data['date_range']:
                #     # todo not working because not facet?
                #     start_date, end_date = data['date_range'].split('-')

        return sqs


class PomsFacetedBrowseForm(FacetedSearchForm):
    min_date = '0'
    max_date = '0'
    DATE_MINIMUM = 1093
    DATE_MAXIMUM = 1300
    index_type_counts = {}
    index_type = 'person'

    def __init__(self, *args, **kwargs):
        super(PomsFacetedBrowseForm, self).__init__(*args, **kwargs)
        # get the earliest and latest dates in the whole record set
        min = SearchQuerySet().filter(startdate__gt=0).order_by('startdate')[0]
        max = SearchQuerySet().all().order_by('-startdate')[0]
        self.DATE_MINIMUM = min.startdate
        self.DATE_MAXIMUM = max.startdate



    def no_query_found(self):
        """Determines the behaviour when no query was found; returns all the
        results."""
        return self.searchqueryset.all()

    def search(self):
        sqs = super(PomsFacetedBrowseForm, self).search()
        if not self.is_valid():
            return self.no_query_found()

        if self.is_bound:
            data = self.data
            if 'min_date' in data:
                sqs = sqs.narrow('startdate:[{0} TO {1}]'.format(
                    data['min_date'],
                    data['max_date']
                ))
        # Get index counts for all types
        if ('fields' in sqs.facet_counts()
                and 'index_type' in sqs.facet_counts()['fields']
        ):
            for type_count in sqs.facet_counts()['fields'][
                'index_type']:
                self.index_type_counts[type_count[0]] = type_count[1]
        # Narrow based on specific index type
        sqs = sqs.narrow(
            'index_type:{}'.format(
                self.index_type
            )
        )
        if ('fields' in sqs.facet_counts()
            and 'startdate' in sqs.facet_counts()['fields']
            and len(sqs.facet_counts()['fields']['startdate']) > 0
        ):
            min = sqs.facet_counts()['fields'][
                'startdate'][0]
            max = sqs.facet_counts()['fields'][
                'startdate'][-1]
            #self.DATE_MAXIMUM = max[0]
            #self.DATE_MINIMUM = min[0]
        return sqs

