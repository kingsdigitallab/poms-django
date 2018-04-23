from django.conf.urls import url



urlpatterns = [
	# root url:
	url(r'^$', 'basic_search', name='basic_search'),
	url(r'^', 'basic_search', name='basic_search'),

]

