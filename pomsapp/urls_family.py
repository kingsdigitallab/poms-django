from django.conf.urls import url

urlpatterns = [
    # root url:
    url(r'^$', 'familytrees_home', name='familytrees_home'),
    # url(r'^familytrees/$', 'familytrees_home', name='familytreeshome'),
    url(r'^(?P<image_id>\d+)/$', 'familytrees', name='familytrees'),
]
