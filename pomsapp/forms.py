from django import forms
from haystack.forms import FacetedSearchForm

RESULT_TYPES = [
    ('factoid', 'Factoid'),
    ('person', 'Person'),
    ('source', 'Source'),
    ('place', 'Place'),
]


class PomsFacetedSearchForm(FacetedSearchForm):
    #todo make this dynamic
    INITIAL_DATE_DISPLAY = '1000-1300'

    index_type = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=RESULT_TYPES
    )

    date_range = forms.CharField(
        required=True, initial=INITIAL_DATE_DISPLAY
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
