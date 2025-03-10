// Fix to update new ref to jquery
var $=jQuery;
var gProj = proj4('EPSG:3857')
var wgsProj = proj4('EPSG:4326')




function geocode() {
	$('#geocode-select').html('');
        var val = $('#geocoder').val();
        //base_url = 'http://nominatim.openstreetmap.org/search?';
		base_url = '/nominatim/search?';
		query_url = 'q='+val;
		params = '&format=json&json_callback=listPoints'
		url = base_url + query_url + params;
		django.jQuery.ajax({
			url: url,
			dataType: "jsonp",
			async:true,
			jsonpCallback: "listPoints",
			jsonp: 'callback'
		});
};

function listPoints(locations){
	locationList = locations;
	$('#geocode-select').append('<option value="">...</option>');
	for (l in locations){
		var str = locations[l].display_name;
		var opt = l;
		$('#geocode-select').append('<option value='+l+'>'+str+'</option>');
	};
};

function centreMap(l){
	var loc = new L.LatLng( parseFloat(locationList[l].lat),parseFloat(locationList[l].lon));
	marker.setLatLng(loc);
	//$('#id_geom').html('POINT ('+ marker.getLatLng().lng +' '+ marker.getLatLng().lat +')')
        // Need to reproject marker since Django upgrade back to EPSG3857
        var markerReproj = proj4(wgsProj,gProj,[ marker.getLatLng().lng, marker.getLatLng().lat ])

        $('#id_geom').html('{"type":"Point","coordinates":[' + markerReproj[0] + ',' +  
        markerReproj[1] + ']}')
}



$(document).ready(function(){
	//Create Google and WGS84 projections
	marker=null;
	$('#id_geom').parent().parent().parent().parent().before(
	   "<div class='form-row map'>"+
		"<div>"+
		"<div id='map'>"+
		"</div>"+
		"</div><!--end container-->" +
		"</div><!--end form row -->"		
		);

        // Hide open layers map  
        //$('.form-row .map').hide();

    	
	$('#map').before('<form id="geocode-form"><label for="geocoder">Place search:</label><input id="geocoder" type="text"></input>'+
	'<input type="button" style="margin:10px;" onclick="geocode()" value="Submit"/><select id="geocode-select"></select></form>');
	

    $('#geocode-select').change(function(){
		centreMap(	$(this).val()	);
	});
		
	// Create map and basic layer:	
	map = new L.map('map');
	var layer = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
	map.setView([56.486,-4.465],6);
	
	// Retrieve and then hide the geom string if it exists:
	geomWKT = $('#id_geom').html();
	$('.form-row.geom').hide();
	geomError = false
	// Parse text field to object
	//m = JSON.parse(geomWKT);
	// Reproject coordinates
	//reprojectedPoint = proj4(gProj,wgsProj,[m.coordinates[0],m.coordinates[1]]);

	// get LatLng :
	if (geomWKT != ''){
		try{ 	
	        m = JSON.parse(geomWKT);
        	// Reproject coordinates
        	reprojectedPoint = proj4(gProj,wgsProj,[m.coordinates[0],m.coordinates[1]]);
	   //geomLng = parseFloat(geomWKT.split(' ')[1].split('(')[1])
   	   //geomLat = parseFloat(geomWKT.split(' ')[2].split(')')[0])
   	   // Plot any existing points
   	   marker = new L.marker([reprojectedPoint[1],reprojectedPoint[0]],{draggable:true}).addTo(map);
   	   map.setView([reprojectedPoint[1],reprojectedPoint[0]],6);
   	}
   	catch(e){
   		geomError = true;
   		//marker = new L.marker([56.486,-4.465],{draggable:true}).addTo(map);
                map.setView([56.486,-4.465],7);
   	}
   }
   else {
   	geomError = true;
   	marker = new L.marker([58,0],{draggable:true}).addTo(map);
   }

	marker.on('dragend',function(){
		//$('#id_geom').html('POINT ('+ marker.getLatLng().lng +' '+ marker.getLatLng().lat +')')

	        var markerReproj = proj4(wgsProj,gProj,[ marker.getLatLng().lng, marker.getLatLng().lat ])

        	$('#id_geom').html('{"type":"Point","coordinates":[' + markerReproj[0] + ',' +
        	markerReproj[1] + ']}')

	});
})
