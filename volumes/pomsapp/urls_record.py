from django.conf.urls import url
import pomsapp.views_record as views_record

urlpatterns = [
    # root url:
    url(r'^$', views_record.basic_record, name='basic_record'),
    # record detail views
    url(r'^person/(?P<person_id>\d+)/$',
        views_record.person_detail,
        name='person_detail'),
    url(r'^source/(?P<source_id>\d+)/$',
        views_record.source_detail,
        name='source_detail'),
    url(r'^factoid/(?P<factoid_id>\d+)/$',
        views_record.factoid_detail,
        name='factoid_detail'),
    url(r'^matrix/(?P<matrix_id>\d+)/$',
        views_record.matrix_detail,
        name='matrix_detail'),
    url(r'^place/(?P<place_id>\d+)/$',
        views_record.place_detail,
        name='place_detail'),
]
