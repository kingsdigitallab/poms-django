from django.conf.urls.defaults import *



urlpatterns = patterns('pomsapp.views_family',
	# root url:
	url(r'^$', 'familytrees_home', name='familytrees_home'),
	# url(r'^familytrees/$', 'familytrees_home', name='familytreeshome'),
	url(r'^(?P<image_id>\d+)/$', 'familytrees', name='familytrees'),

)

