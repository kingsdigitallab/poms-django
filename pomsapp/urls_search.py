from django.conf.urls.defaults import *



urlpatterns = patterns('pomsapp.views_search',
	# root url:
	url(r'^$', 'basic_search', name='basic_search'),
	url(r'^', 'basic_search', name='basic_search'),

)

