from django.conf.urls import url

from pomsapp.views import PomsFacetedBrowse

urlpatterns = [
    url(r'^$', PomsFacetedBrowse.as_view(), name='browse'),
    url(r'(?P<facet_group>\w+)/(?P<facet_name>\w+)/$', PomsFacetedBrowse.as_view(
        template_name='pomsapp/browse/facet_group.html',
        ajax=True,
    ), name='facet_group'),

]
