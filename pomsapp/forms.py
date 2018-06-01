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
    DATE_MINIMUM = 1000
    DATE_MAXIMUM = 1300



    index_type = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=RESULT_TYPES
    )

    def __init__(self, *args, **kwargs):
        super(PomsFacetedSearchForm, self).__init__(*args, **kwargs)
        # get the earliest and latest dates in the whole record set
        min = SearchQuerySet().all().order_by('startdate')[0]
        max = SearchQuerySet().all().order_by('-startdate')[0]
        self.DATE_MINIMUM = min.startdate
        self.DATE_MAXIMUM = max.startdate


    date_range = forms.CharField(
        required=True
    )

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
            if data['index_type']:
                sqs = sqs.narrow(
                    'index_type:{}'.format(
                        data['index_type']
                    )
                )
            # split the character date range into two integers
            # apply to start date
            if data['date_range']:
                if '-' in data['date_range']:
                    # todo not working because not facet?
                    start_date, end_date = data['date_range'].split('-')
                    # sqs = sqs.narrow('startdate:[{0} TO {0}]'.format(
                    #     start_date,
                    #     end_date
                    # ))


        return sqs

class PomsFacetedBrowseForm(FacetedSearchForm):

    def no_query_found(self):
        """Determines the behaviour when no query was found; returns all the
        results."""
        return self.searchqueryset.all()

    def search(self):
        sqs = super(PomsFacetedBrowseForm, self).search()
        if not self.is_valid():
            return self.no_query_found()
        return sqs