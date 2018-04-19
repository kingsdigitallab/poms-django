from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('pomsapp.views_map',
    url(r'^browse/$', 'map_view', name='map_view'),
    url(r'^search/$', 'map_search', name='map_search'),
    url(r'^search-by-parent/$', 'map_search_by_parent', name='map_search_by_parent'),	
    url(r'^hierarchy/$', 'hierarchy', name='hierarchy'),	
    url(r'^map-image/$', 'map_image', name='map-image'),    
    url(r'^$', direct_to_template,{'template': 'preview_map.html'}),
)
