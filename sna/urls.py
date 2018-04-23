from django.conf.urls.defaults import *
from django.conf.urls import url
import sna.views as sna_views

urlpatterns = [
    url(r'grantor/(\d+)/$', sna_views.sna_grantor, name='sna_grantor'),
    url(r'grantor/$', sna_views.sna_grantor_base, name='sna_grantor_base'),
    url(r'family/(\d+)/$', sna_views.sna_person, name='sna_person'),
    url(r'family/$', sna_views.sna_person_base, name='sna_person_base'),
    url(r'all/(\d+)/$', sna_views.sna_all, name='sna_all'),
    url(r'all/$', sna_views.sna_default, name='sna_default'),
    url(r'js/(\d+)/(\w+).js', sna_views.sna_js ,name='sna_js'),
    url(r'(\d+)/$', sna_views.sna_person, name='sna_person'),
    url(r'^$', sna_views.sna_default, name='sna_default'),
]
