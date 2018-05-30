from django.conf.urls import url

from pomsapp.views import PomsFacetedBrowse

urlpatterns = [
    url(r'^$', PomsFacetedBrowse.as_view(), name='browse'),
    url(r'person/$', PomsFacetedBrowse.as_view(
        template_name='pomsapp/browse/facet_person.html',
        ajax=True,
        ajax_facet='person'
    ), name='person_facet_group'),
    url(r'source/$', PomsFacetedBrowse.as_view(
        template_name='pomsapp/browse/facet_source.html',
        ajax=True,
        ajax_facet='source'
    ), name='source_facet_group'),
    url(r'relationship/$', PomsFacetedBrowse.as_view(
        template_name='pomsapp/browse/facet_relationship.html',
        ajax=True,
        ajax_facet='relationship'
    ), name='relationship_facet_group'),
    url(r'transaction/$', PomsFacetedBrowse.as_view(
        template_name='pomsapp/browse/facet_transaction.html',
        ajax=True,
        ajax_facet='transaction'
    ), name='transaction_facet_group'),
    url(r'termsoftenure/$', PomsFacetedBrowse.as_view(
        template_name='pomsapp/browse/facet_termsoftenure.html',
        ajax=True,
        ajax_facet='termsoftenure'
    ), name='termsoftenure_facet_group'),
]
