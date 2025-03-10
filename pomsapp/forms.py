from haystack.forms import FacetedSearchForm
import re

RESULT_TYPES = [
    ('factoid', 'Factoid'),
    ('person', 'Person'),
    ('source', 'Source'),
    ('place', 'Place'),
]


class PomsFacetedBrowseForm(FacetedSearchForm):
    DATE_MINIMUM = 1093
    DATE_MAXIMUM = 1371
    index_type_counts = {}
    index_type = 'person'

    min_date = 0

    max_date = 0

    def __init__(self, *args, **kwargs):
        super(PomsFacetedBrowseForm, self).__init__(*args, **kwargs)

    def no_query_found(self):
        """Determines the behaviour when no query was found; returns all the
        results."""
        return self.searchqueryset.all()

    def search(self):
        sqs = super(PomsFacetedBrowseForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        facet_counts = sqs.facet_counts()

        if self.is_bound:
            data = self.data

            if 'q' in data:
                q = data['q'].strip()

                if len(q) > 0:
                    m = re.search(r'(\d+/\d*/?\d*)', q)
                    if m:
                        hNumber = m.group(1)
                        q = q.replace(hNumber, r'"{}"'.format(hNumber))

                    # Force text search to an all keywords behaviour
                    q_query = ' AND '.join(q.split())
                    sqs = sqs.narrow('text:{}'.format(q_query))

            # Don't apply dating to place
            # if 'min_date' in data and self.index_type != 'place':
            #     # Don't apply if it's default dates
            #     if (int(data['min_date']) != self.DATE_MINIMUM or
            #             int(data['max_date']) != self.DATE_MAXIMUM):
            #         sqs = sqs.narrow('startdate:[{0} TO {1}]'.format(
            #             data['min_date'],
            #             data['max_date']
            #         ))

            facet_counts = sqs.facet_counts()

        # Get index counts for all types
        if 'fields' in facet_counts and 'index_type' in facet_counts['fields']:
            for type_count in facet_counts['fields']['index_type']:
                self.index_type_counts[type_count[0]] = type_count[1]

        # Narrow based on specific index type
        sqs = sqs.narrow('index_type:{}'.format(self.index_type))

        return sqs
