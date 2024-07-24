parseMapResults(
{"type":"FeatureCollection",
 "features":[
	{% for p in places %}
	{"type":"Feature",
	 "properties": 
	 { "name":"{{ p.name|safe }}",
           "id":"{{ p.id }}",
	   "parent":"{{ p.parent.name }}",
           "people":[{% for person in p.person_set.all %}  {"id":{{ person.pk}},"name":"{{ person.persondisplayname|safe }}" 
                     {% if not forloop.last%} }, {% else %} } {% endif %} {% endfor %} ] 
        ,
	    "charters": [{% for charter in p.charter_set.all %}  {"id":{{ charter.pk}},"name":"{{ charter.source_tradid|safe }}" {% if not forloop.last%} }, {% else %} } {% endif %} {% endfor %} ],
		"placetypes":[{% for type in p.place_types.all %}"{{ type }}"{% if forloop.last %}{% else %},{% endif %}{% endfor %}],
            "place_types":[{% for type in p.place_types.all %}"{{ type }}"{% if forloop.last %}{% else %},{% endif %}{% endfor %}],
     },
	{% if p.geom.geojson %} 
	"geometry" : {{ p.geom.geojson|safe }} 
        {% if not forloop.last %} },{% else%} }  {% endif %}
	{% else %}
        {% if not forloop.last %} },{% else%} }  {% endif %}	
	{% endif %}
	{% endfor %}
  ]
}
)
