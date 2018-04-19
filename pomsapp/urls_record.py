from django.conf.urls.defaults import *



urlpatterns = patterns('pomsapp.views_record',
	# root url:
	url(r'^$', 'basic_record', name='basic_record'),
	# record detail views
	url(r'^person/(?P<person_id>\d+)/$', 'person_detail', name='person_detail'),
	url(r'^source/(?P<source_id>\d+)/$', 'source_detail', name='source_detail'),
	url(r'^factoid/(?P<factoid_id>\d+)/$', 'factoid_detail', name='factoid_detail'),
	url(r'^matrix/(?P<matrix_id>\d+)/$', 'matrix_detail', name='matrix_detail'),
	url(r'^place/(?P<place_id>\d+)/$', 'place_detail', name='place_detail'),

)


