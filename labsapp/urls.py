from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
	# root url and main STATIC windows:
	(r'^$', direct_to_template, {'template': 'labs/mainsite/indexLabs.html'}),
	(r'^connectionscloud$', direct_to_template, {'template': 'labs/mainsite/connectionscloud.html', 'extra_context': { 
	    'connectionscloud': True, 
	  }}),
	(r'^peoplelives$', direct_to_template, {'template': 'labs/mainsite/lives.html', 'extra_context': { 
	    'peoplelives': True, 
	  }}),
	(r'^peopleimportance$', direct_to_template, {'template': 'labs/mainsite/importance.html', 'extra_context': { 
	    'peopleimportance': True, 
	  }}),
	(r'^witnesses$', direct_to_template, {'template': 'labs/mainsite/witnesses.html', 'extra_context': { 
	    'witnesses': True, 
	  }}),

	# DYNAMIC stuff:

	# CONNECTIONSCLOUD
	# (r'^peoplenavigator$', 'labsapp.people_navigator.index' ),
	(r'^connectionscloud/go$', 'labsapp.connectionscloud.index' ),
	(r'^connectionscloud/ajax/getCommonConnections', 'labsapp.connectionscloud.getCommonConnections' ),
	url(r'^connectionscloud/autocomplete/$', 'labsapp.connectionscloud.autocomplete_people', name='autocomplete_people'),


	# IMPORTANCE
	(r'^popularitycloud/go$', 'labsapp.popularitycloud.pop_cloud' ),
	# ajax: used here and also in Lives and Longevity Chart - so careful when modifying 
	(r'^popularitycloud/ajax/personinfo', 'labsapp.popularitycloud.personinfo' ),
	
		
	# LIVES
	(r'^peoplelives/go$', 'labsapp.peoplelives.lives' ),
	(r'^peoplelives/ajax_lives1', 'labsapp.peoplelives.ajax_lives1' ),

	#LONGEVITY CHART
	(r'^longevitychart/go$', 'labsapp.highcharts_scatter.scatter_peopleage' ),
	(r'^longevitychart/ajax/iteminfo$', 'labsapp.highcharts_scatter.iteminfo' ),


	# RELATIONSHIPS : SANKEY version
	(r'^relationships/go$', 'labsapp.relationships.index' ),
	(r'^relationships/ajax/iteminfo', 'labsapp.relationships.iteminfo' ),
	

	# WITNESSES
	(r'^witnesses/go$', 'labsapp.witnessesRgraph.index' ),
	(r'^witnesses/go-halfsize$', 'labsapp.witnessesRgraph.index' , {'template': 'halfsize'}),
	(r'^witnesses/ajax/iteminfo', 'labsapp.witnessesRgraph.iteminfo' ),



	# --------
	# INTERNAL URLS - testing and backup
	# --------


	# PERSON 2 PERSON  [dismissed]
	(r'^person2person/go$', 'labsapp.person2person.index' ),
	(r'^person2person/go-halfsize$', 'labsapp.person2person.index' , {'template': 'halfsize'}),
	# (r'^person2person/ajax/iteminfo', 'labsapp.person2person.iteminfo' ),
				
	(r'^bubbles$', 'labsapp.bubbles.index' ),
	
	# highcharts	
	(r'^scatter$', 'labsapp.highcharts_scatter.scatter' ),
	(r'^scatter_example$', 'labsapp.highcharts_scatter.scatter_example' ),
	(r'^scatterpeople$', 'labsapp.highcharts_scatter.scatter_peopleage' ),
	
	
	# still in the making..
	
	(r'^tree$', 'labsapp.tree.tree1' ),


)

