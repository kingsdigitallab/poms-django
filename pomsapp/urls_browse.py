from django.conf.urls import url

from pomsapp.views import PomsFacetedBrowse

urlpatterns = [
    url(r'^$', PomsFacetedBrowse.as_view(), name='search'),
    url(r'(?P<facet_group>\w+)/(?P<facet_name>\w+)/$',
        PomsFacetedBrowse.as_view(
            template_name='pomsapp/browse/facet_choices.html',
            ajax=True,
        ), name='facet_group'),

]
