from django.conf.urls import url
from django.views.generic import TemplateView

import labsapp.connectionscloud as connectionscloud
import labsapp.highcharts_scatter as highcharts_scatter
import labsapp.peoplelives as peoplelives
import labsapp.popularitycloud as popularitycloud
import labsapp.relationships as relationships
import labsapp.witnessesRgraph as witnessesRgraph
import labsapp.person2person as person2person
import labsapp.bubbles as bubbles
from labsapp.tree import tree1

urlpatterns = [
    # root url and main STATIC windows:
    url(r'^$', TemplateView.as_view(template_name='labs/mainsite/indexLabs.html')),
    url(r'^connectionscloud$', TemplateView.as_view(
        template_name='labs/mainsite/connectionscloud.html', initkwargs={
            'connectionscloud': True,
        })),
    url(
        r'^peoplelives$', TemplateView.as_view(template_name='labs/mainsite/lives.html',
                                               initkwargs={
                                                   'peoplelives': True,
                                               })),
    url(r'^peopleimportance$',
        TemplateView.as_view(template_name='labs/mainsite/importance.html',
                             initkwargs={
                                 'peopleimportance': True,
                             })),
    url(r'^witnesses$', TemplateView.as_view(template_name='labs/mainsite/witnesses.html',
                                             initkwargs={
                                                 'witnesses': True,
                                             })),

    # DYNAMIC stuff:

    # CONNECTIONSCLOUD
    # (r'^peoplenavigator$', 'labsapp.people_navigator.index' ),
    url(r'^connectionscloud/go$', connectionscloud.index,
        name='labsapp.connectionscloud.index'),
    url(
        r'^connectionscloud/ajax/getCommonConnections',
        connectionscloud.getCommonConnections,
        name='labsapp.connectionscloud.getCommonConnections'),

    url(r'^connectionscloud/autocomplete/$',
        connectionscloud.autocomplete_people,
        name='autocomplete_people'),

    # IMPORTANCE
    url(r'^popularitycloud/go$',
        popularitycloud.pop_cloud,
        name='labsapp.popularitycloud.pop_cloud'),
    # ajax: used here and also in Lives and Longevity Chart - so careful when
    # modifying
    url(r'^popularitycloud/ajax/personinfo',
        popularitycloud.personinfo,
        name='labsapp.popularitycloud.personinfo'),

    # LIVES
    url(r'^peoplelives/go$',
        peoplelives.lives,
        name='labsapp.peoplelives.lives'),
    url(r'^peoplelives/ajax_lives1',
        peoplelives.ajax_lives1,
        'labsapp.peoplelives.ajax_lives1'),

    # LONGEVITY CHART
    url(r'^longevitychart/go$',
        highcharts_scatter.scatter_peopleage,
        name='labsapp.highcharts_scatter.scatter_peopleage'),
    url(r'^longevitychart/ajax/iteminfo$',
        highcharts_scatter.iteminfo,
        name='labsapp.highcharts_scatter.iteminfo'),

    # RELATIONSHIPS : SANKEY version
    url(r'^relationships/go$',
        relationships.index,
        name='labsapp.relationships.index'),
    url(r'^relationships/ajax/iteminfo',
        relationships.iteminfo,
        name='labsapp.relationships.iteminfo'),

    # WITNESSES
    url(r'^witnesses/go$',
        witnessesRgraph.index,
        name='labsapp.witnessesRgraph.index'),
    url(r'^witnesses/go-halfsize$', witnessesRgraph.index,
        name='labsapp.witnessesRgraph.index',
        kwargs={'template': 'halfsize'}),
    url(r'^witnesses/ajax/iteminfo', witnessesRgraph.iteminfo,
        'labsapp.witnessesRgraph.iteminfo'),

    # --------
    # INTERNAL URLS - testing and backup
    # --------


    # PERSON 2 PERSON  [dismissed]
    url(r'^person2person/go$', person2person.index,
        name='labsapp.person2person.index'),
    url(r'^person2person/go-halfsize$', person2person.index,
        name='labsapp.person2person.index', kwargs={'template': 'halfsize'}),
    # (r'^person2person/ajax/iteminfo', 'labsapp.person2person.iteminfo' ),

    url(r'^bubbles$',
        bubbles.index,
        name='labsapp.bubbles.index'),

    # highcharts
    url(r'^scatter$',
        highcharts_scatter.scatter,
        name='labsapp.highcharts_scatter.scatter'),
    url(r'^scatter_example$',
        highcharts_scatter.scatter_example,
        name='labsapp.highcharts_scatter.scatter_example'),
    url(r'^scatterpeople$',
        highcharts_scatter.scatter_peopleage,
        'labsapp.highcharts_scatter.scatter_peopleage'),

    # still in the making..

    url(r'^tree$',
        tree1,
        name='labsapp.tree.tree1'),

]
