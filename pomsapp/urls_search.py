from django.conf.urls import url
from pomsapp.views import PomsFacetedSearchView

# todo will add once haystack conversion complete
urlpatterns = [

	# root url:
	url(r'^$', PomsFacetedSearchView.as_view(), name='basic_search'),

	# url(r'^', 'basic_search', name='basic_search'),

]

