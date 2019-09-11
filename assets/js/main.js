// Filter facet choices for quick searching
var filterFacets = function () {
    var value = $(this).val().toLowerCase();
    var facet = $(this).data('facet');
    $("ul." + facet + "_choices li").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
}

/** Record pagination
 *
 * Legacy From existing template, will need to be refactored...
 * */
jQuery.fn.simple_blink = function () {
    return this.fadeOut("fast").fadeIn("slow");
};
jQuery.fn.add_loading_icon = function () {
    loadingData = "<img src='/media/static/paul/i/g.gif' alt='loading data' />"
    return this.empty().append(loadingData);
};

/**
 * Update tables in detail pages for relevant result type
 * @param page
 * @param ordering order the results
 * @param tab tab to update
 */
function update_related_factoids(page, ordering, tab) {
    // EH: Not sure what this is, but will replace with proper ordering.
    var old_ordering = $("#" + tab + " .active_ordering").val();
    $("#" + tab).add_loading_icon();

    if (old_ordering == ordering) {
        ordering = "-" + ordering;
        // alert(ordering);
    }
    // ajax_update_tabs("#fragment-1", "", tab, page, ordering);
    ajax_update_tabs("#" + tab, "", tab, page, ordering);
}


// for the Source record-page :: USED?
function update_source_factoids(page, ordering, tab) {
    if (!tab) var tab = "fragment-1";   // we pass the tab-ids directly in the functions... might be done dynamically later..
    $("#" + tab).add_loading_icon();
    ajax_update_tabs("#" + tab, "", tab, page, ordering);
}


// name (= value in the facet), type(facet group), facet (the facet within a group) identify a value uniquely
function ajax_update_tabs(divname, ajaxcall, tab, page, ordering) {
    if (!page) var page = 1;   // if no page defaults to 1
    if (!tab) var tab = 1;   // if no page defaults to 1
    if (!ordering) var ordering = 'default';   // if no page defaults to 1person_detail

    $.get(ajaxcall,
        {tab: tab, page: page, ordering: ordering},
        function (data) {
            d = data;
            dname = divname;
            $(divname).empty().append($(data).find(divname).html());
            $(divname + ' a.paginate').on("click", paginate);
            // reload qtips
            qtip_previews();
        }
    );
}

/**
 * anchor function to advance pagination in detail pages
 * also used for ordering in column headings
 * @param e
 */
var paginate = function (e) {
    e.preventDefault();
    var page = $(this).data('page');
    var ordering = $(this).data('ordering');
    var tab = $(this).data('tab');
    update_related_factoids(page, ordering, tab);
}

/**
 * Swap the icon in the facet label if it's open/closed
 * @param target selector for label
 */
var toggle_facet_icon = function (target) {
    var closed_icon = '▸';
    var open_icon = '▾';
    if ($(target).html().indexOf(closed_icon) > -1) {
        $(target).html($(target).html().replace(closed_icon, open_icon));
    } else {
        $(target).html($(target).html().replace(open_icon, closed_icon));
    }


}
/* ******************* */

$(function () {


    // Loading facet categories via async
    $('a.async').click(function (e) {
        e.preventDefault();
        var facet_group = $(this).data('facet_group');
        var facet_name = $(this).data('facet_name');
        var label = $(this).children('strong');
        if ($(this).attr('class').indexOf('loaded') < 0) {
            // Load the facet choices
            var selected_facets = $(this).data('selected_facets');
            var title = this;
            var url = "/search/" + facet_group + "/" + facet_name + "/?"+$('#search_form').serialize();
            /*if (selected_facets && selected_facets.length > 0) {
                url += selected_facets;
            }*/


            if ($('div.' + facet_group + '__' + facet_name).html().length < 1) {
                $.get(url, function (data) {
                    var div = $('div.' + facet_group + '__' + facet_name);
                    //if (div.length > 0) {
                    var content = div[0];
                    $(content).append(data);
                    //}
                    $("#" + facet_name + "_facetfilter").on("keyup", filterFacets);
                    toggle_facet_icon(label);
                });
            }

            $(this).toggleClass('loaded');
            $(this).toggleClass('active');
        } else {
            toggle_facet_icon(label);
            $('div.' + facet_group + '__' + facet_name).slideToggle(400);
            $(this).toggleClass('active');
        }

    });

    // Ajax pagination for detail pages
    $('a.paginate').on("click", paginate);



    // This allows us to activate the first tab on the record pages:
    if($('.recordTabs input[name="tabs"]'.length))
    {
        $('.recordTabs input[name="tabs"]').first().attr("checked", "checked");
    }

    // Clear button on facets...
    $('body').on('click', '.clear-icon', function(event)
    {
        event.preventDefault();
        event.stopPropagation();
        $(this).siblings('input').val('').keyup();

    });

    //new gRanger('#range', '#min', '#max');
});


/***********************
 * Browse Map
 ***********************/

// Global vars
var geomQry = '';
var parentID = '';
var storedJSON;
var oms;
var personMarker;
var personCharterMarker;
var charterMarker;
var plainmarker;
var mapHeight;
var map;
var geoJSON;

function getBGSBedrock(e) {
    if (map.getZoom() >= 13) {
        map.spin(true)
        $.ajax('/bgs/WMSServer?version=1.3.0&request=GetFeatureInfo&layers=BGS.50k.Bedrock' +
            '&query_layers=BGS.50k.Bedrock&crs=CRS:84&info_format=text/html&i='
            + e.containerPoint.x + '&j='
            + e.containerPoint.y + '&radius=0'
            + 'SRS=EPSG:4326&BBOX='
            + map.getBounds()._southWest.lng
            + ','
            + map.getBounds()._southWest.lat
            + ','
            + map.getBounds()._northEast.lng
            + ','
            + map.getBounds()._northEast.lat
            + '&WIDTH='
            + map.getSize().x
            + '&HEIGHT=' + map.getSize().y
            + '&styles=default',
            {
                success: function (data) {
                    map.spin(false)
                    var popup = L.popup().setLatLng([e.latlng.lat, e.latlng.lng]).setContent(
                        '<h3>' + $(data).find('td:nth-child(5)').html() + '</h3><p>' + $(data).find('td:nth-child(22)').html() + '</p>').openOn(map);
                },
                type: 'html'
            })
    }
}

function getBGSSuperficial(e) {
    if (map.getZoom() >= 13) {
        map.spin(true)
        $.ajax('/bgs/WMSServer?version=1.3.0&request=GetFeatureInfo&layers=BGS.50k.Superficial.deposits' +
            '&query_layers=BGS.50k.Superficial.deposits&crs=CRS:84&info_format=text/html&i='
            + e.containerPoint.x + '&j='
            + e.containerPoint.y + '&radius=0'
            + 'SRS=EPSG:4326&BBOX='
            + map.getBounds()._southWest.lng
            + ','
            + map.getBounds()._southWest.lat
            + ','
            + map.getBounds()._northEast.lng
            + ','
            + map.getBounds()._northEast.lat
            + '&WIDTH='
            + map.getSize().x
            + '&HEIGHT=' + map.getSize().y
            + '&styles=default',
            {
                success: function (data) {
                    map.spin(false)
                    if ($(data).find('td').length != 0) {
                        var popup = L.popup().setLatLng([e.latlng.lat, e.latlng.lng]).setContent(
                            '<h3>' + $(data).find('td:nth-child(5)').html() + '</h3><p>' + $(data).find('td:nth-child(26)').html() + '</p>').openOn(map);
                    }
                },
                type: 'html'
            })
    }
}

function parseMapResults(data) {
    //oms.clearLayers()
    geoJSON.clearLayers();
    geoJSON.addData(data).addTo(map);
};

function getPopup(props) {
    var span="";
    // Use for debugging only
    //console.log(props);
    if (props.factoids && props.factoids.length > 0) {
        span = ' colspan="4"';
    }
    str = '<table class="simple headersX"><tbody><tr><th'+span+'><a href="/record/place/' + props.id + '">' + props.name + '</a>, '+ props.parent +'</th></tr>';

    if (props.people && props.people.length > 0) {
        //str += '<tr><th>People:</th></tr>';
        for (p in props.people) {
            str += '<tr><td><a href="/record/person/' + props.people[p].id + '">' + props.people[p].name + '</a> '+ props.people[p].floruit +'</td></tr>'
        }
    }
    if (props.charters && props.charters.length > 0) {
        //str += '<tr><th>Source:</th></tr>';
        for (c in props.charters) {
            str += '<tr><td><a href="/record/source/' + props.charters[c].id + '">'
                + props.charters[c].hammondnumber + '</a> ' + props.charters[c].firmdate +'</td></tr>'
        }
    }
    if (props.factoids && props.factoids.length > 0) {
        //str += '<tr><th colspan="4">Factoids:</th></tr>';
        for (f in props.factoids) {
            str += '<td><a href="/record/factoid/' + props.factoids[f].id + '">'
                + props.factoids[f].description + '</a></td><td>'
                + props.factoids[f].inferred_type + '</td><td>'
                + '<a href="/record/source/' + props.charter_id + '">'+ props.factoids[f].hammondnumber + '</a></td><td>'
                + props.factoids[f].firmdate+'</td>';
            if (f!=0){
                str +="<hr/>"
            }
            str += "</td></tr>";
        }
    }
    str += '</tbody></table>'
    return str;
};

function removeType(filterString) {
    for (i in geoJSON._layers) {
        if (geoJSON._layers[i].feature.properties.style == filterString) {
            // store removed data
            storedJSON[filterString].push(JSON.stringify(geoJSON._layers[i].toGeoJSON()));
            geoJSON.removeLayer(geoJSON._layers[i])
        }
    }
}

function replaceType(filterString) {
    for (i in storedJSON[filterString]) {
        feature = eval('(' + storedJSON[filterString][i] + ')')
        geoJSON.addData(feature)
    }
    storedJSON[filterString] = new Array();
};





function openMapImage(data) {
    $('.ui-tooltip-content').html(data)
    map.addLayer(oms)
    map.removeLayer(geoJSON)
};

function updateResults() {
    map.spin(true);
    if (geomQry != '') {
        $.ajax('search/?' + geomQry, {
            dataType: "jsonp",
            complete: function () {
                map.spin(false);
            }
        });
    }
    else if (parentID != '') {
        $.ajax('search-by-parent/?id=' + parentID, {
            dataType: "jsonp",
            complete: function () {
                map.spin(false);
            }

        });
    }
};

// Init Function
function initMap()
{
    storedJSON = new Object();
    storedJSON.place = new Array();
    storedJSON.charter = new Array();
    storedJSON.person = new Array();
    mapHeight = $(window).height()
    L.SpinMapMixin = {
        spin: function (state, options) {
            if (!!state) {
                // start spinning !
                if (!this._spinner) {
                    this._spinner = new Spinner(options).spin(this._container);
                    this._spinning = 0;
                }
                this._spinning++;
            }
            else {
                this._spinning--;
                if (this._spinning <= 0) {
                    // end spinning !
                    if (this._spinner) {
                        this._spinner.stop();
                        this._spinner = null;
                    }
                }
            }
        }
    };

    L.Map.include(L.SpinMapMixin);

    L.Map.addInitHook(function () {
        this.on('layeradd', function (e) {
            // If added layer is currently loading, spin !
            if (e.layer.loading) this.spin(true);
            if (typeof e.layer.on != 'function') return;
            e.layer.on('data:loading', function () {
                this.spin(true);
            }, this);
            e.layer.on('data:loaded', function () {
                this.spin(false);
            }, this);
        }, this);
        this.on('layerremove', function (e) {
            // Clean-up
            if (e.layer.loading) this.spin(false);
            if (typeof e.layer.on != 'function') return;
            e.layer.off('data:loaded');
            e.layer.off('data:loading');
        }, this);
    });

    // Markers!
    personMarker = L.AwesomeMarkers.icon({
        icon: 'male',
        markerColor: 'red',
        prefix: 'fa'
    });

    personCharterMarker = L.AwesomeMarkers.icon({
        icon: 'male',
        markerColor: 'green',
        prefix: 'fa'
    });

    charterMarker = L.AwesomeMarkers.icon({
        icon: 'book',
        markerColor: 'green',
        prefix: 'fa'
    });

    factoidMarker = L.AwesomeMarkers.icon({
        icon: 'balance-scale',
        markerColor: 'blue',
        prefix: 'fa'
    });

    plainMarker = L.AwesomeMarkers.icon({
        icon: 'university',
        markerColor: 'blue',
        prefix: 'fa'
    });

    $('#map').height(mapHeight)
    map = new L.map('map', {crs: L.CRS.EPSG3857, scrollWheelZoom: false});
    layer = new L.TileLayer('http://{s}.tiles.mapbox.com/v3/isawnyu.map-knmctlkh/{z}/{x}/{y}.png',
        {attribution: 'Map base by <a href="http://awmc.unc.edu/">AWMC</a>'}).addTo(map);
    modern = new L.TileLayer("http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}")
    regions = new L.tileLayer.wms('/geoserver/gwc/service/wms?', {
            layers: 'PDE_Postgres:scotland_regions_simple',
            format: 'image/png',
            transparent: true,
            attribution: 'Orndnance Survey BoundaryLine'
        }
    );
    land_use = new L.tileLayer.wms('/geoserver/gwc/service/wms?', {
            layers: 'PoMS:scottish_medieval_landuse_2015_08',
            format: 'image/png',
            transparent: true,
            attribution: '<a href="http://hla.rcahms.gov.uk/">Historic Environment Scotland</a>'
        }
    );
    os_1st_ed = new L.TileLayer('http://geo.nls.uk/maps/os/1inch_2nd_ed/{z}/{x}/{y}.png', {
        tms: false,
        attribtution: '<a href="http://maps.nls.uk/">National Library of Scotland</a>'
    })

    geology = new L.tileLayer.wms('https://map.bgs.ac.uk/arcgis/services/BGS_Detailed_Geology/MapServer/WMSServer?', {
        layers: 'BGS.50k.Bedrock',
        format: 'image/png',
        crs: L.CRS.EPSG3857,
        minZoom: 13,
        opacity: 0.5,
        transparent: true,
        attribution: 'BGS:50k'
    });
    superficial = new L.tileLayer.wms('https://map.bgs.ac.uk/arcgis/services/BGS_Detailed_Geology/MapServer/WMSServer?', {
            layers: 'BGS.50k.Superficial.deposits',
            format: 'image/png',
            crs: L.CRS.EPSG3857,
            minZoom: 13,
            opacity: 0.5,
            transparent: true,
            attribution: 'BGS:50k'
        }
    );
    map.setView([56.3926, -3.724], 7);

    // Initialise the FeatureGroup to store editable layers
    drawnItems = new L.FeatureGroup();
    map.addLayer(drawnItems);
    oms = new OverlappingMarkerSpiderfier(map);

    switcher = new L.control.layers({'Terrain': layer, 'Modern': modern}, {
        'Modern regions': regions,
        'OS 1st Ed. 1885-1990 (1 inch)': os_1st_ed,
        'Medieval Land use': land_use,
        'Bedrock (Zoom 13+)': geology,
        'Superficial (Zoom 13+)': superficial
    }).addTo(map)

    $('.leaflet-control-layers-overlays label input:checkbox').click(function () {
        if ($(this).next().html() == ' Bedrock (Zoom 13+)') {
            if ($(this).attr('checked')) {
                map.on('click', getBGSBedrock)
            }
            else {
                map.off('click', getBGSBedrock)
            }
        }
    })

    $('.leaflet-control-layers-overlays label input:checkbox').click(function () {
        if ($(this).next().html() == ' Superficial (Zoom 13+)') {
            if ($(this).attr('checked')) {
                map.on('click', getBGSSuperficial)
            }
            else {
                map.off('click', getBGSSuperficial)
            }
        }
    })

    var drawControl = new L.Control.Draw({
        edit: {
            featureGroup: drawnItems,
            edit: false
        },
        draw:
            {
                polyline: false,
                circle: false,
                rectangle: true,
                polygon: false,
                marker: false,
                position: 'bottomleft'
            }
    }).addTo(map);

    map.on('draw:created', function (e) {
        drawnItems.clearLayers();
        var type = e.layerType,
            layer = e.layer;
        drawnItems.addLayer(layer);
        geomQry = '&selected_geom=' + JSON.stringify(e.layer.toGeoJSON().geometry.coordinates)
        updateResults();
    })

    map.on('draw:deleted', function (e) {
        geomQry = ''
    })


    $('.leaflet-control-zoom-in').after('<a id="zoom-level">7</a>');

    map.on('zoomend', function (e) {
        $('#zoom-level').html(map.getZoom());
    })

    $.ajax('hierarchy/', {
            success: function (data) {
                $('.leaflet-control-container').append(data);
                $('#parent-places input').click('', function () {
                    if (this.checked) {
                        drawnItems.clearLayers()
                        geomQry = '';
                        parentID = $(this).data('place-id');
                        updateResults();
                    }
                    else {
                        drawnItems.clearLayers()
                        parentID = ''
                        map.spin(false);
                        geoJSON.clearLayers();
                    }
                })
                $($('#parent-places label')[0]).before('<img src="/static/images/map_key.png"></img>')
            }
        }
    )

    geoJSON = new L.geoJson(null,
        {
            onEachFeature: function (feature, layer) {
                var props = feature.properties
                layer.bindPopup(getPopup(props), {minWidth: '300'})
            },
            pointToLayer: function (feature, latlng) {
                if (feature.properties.people && feature.properties.people.length > 0) {
                    marker = new L.marker(latlng, {icon: personMarker});
                    //{ marker =  new L.circleMarker(latlng);
                    feature.properties['style'] = 'person';
                    // Are there charters as well?
                    if (feature.properties.charters && feature.properties.charters.length > 0) {
                        marker = new L.marker(latlng, {icon: personCharterMarker});
                        //marker = new L.circleMarker(latlng)
                    }
                }
                else if (feature.properties.charters && feature.properties.charters.length > 0) {
                    marker = new L.marker(latlng, {icon: charterMarker});
                    feature.properties['style'] = 'charter'
                }else if (feature.properties.factoids && feature.properties.factoids.length > 0) {
                    marker = new L.marker(latlng, {icon: factoidMarker});
                    feature.properties['style'] = 'factoid'
                }
                else {
                    marker = new L.marker(latlng, {icon: plainMarker});
                    //marker = new L.circleMarker(latlng)
                    feature.properties['style'] = 'place'
                }
                oms.addMarker(marker);
                //oms.addLayer(marker);
                return marker
            }
        }
    );
}


// Go!
$(document).ready(function()
{
    if($('.browse-map').length)
    {
        initMap();
    }
});
