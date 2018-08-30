import pomsapp.views_map as views_map
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^/$', views_map.map_view, name='map_view'),
    url(r'^search/$', views_map.map_search, name='map_search'),
    url(r'^search-by-parent/$', views_map.map_search_by_parent, name='map_search_by_parent'),
    url(r'^hierarchy/$', views_map.hierarchy, name='hierarchy'),
    url(r'^map-image/$', views_map.map_image, name='map-image'),
    url(r'^$', TemplateView.as_view(template_name='preview_map.html')),
]
