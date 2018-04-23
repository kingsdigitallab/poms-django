from django.conf.urls import url
import pomsapp.views_family as views_family

urlpatterns = [
    # root url:
    url(r'^$', views_family.familytrees_home, name='familytrees_home'),
    # url(r'^familytrees/$', 'familytrees_home', name='familytreeshome'),
    url(r'^(?P<image_id>\d+)/$', views_family.familytrees, name='familytrees'),
]
