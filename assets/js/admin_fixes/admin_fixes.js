
// make certain fields uneditable
function update_document() {
	
	$("#id_firmdate").attr("DISABLED", "DISABLED");
	$("#lookup_sourcekey").attr("SIZE", "50");
	$("#lookup_placefielty").attr("SIZE", "50");
	$("#lookup_place").attr("SIZE", "50");
	$("#lookup_placefk").attr("SIZE", "50");
	// for tree models
	$("#lookup_parent").attr("SIZE", "50");
	
	
	// for factoids with associated people
	$("tr.dynamic-assocfactoidperson_set td.person input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidwitness_set td.person input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidproanima_set td.person input").attr("SIZE", "50"); // m2m fields
	// for possessions
	$("tr.dynamic-assocfactoidprivileges_set td.privilege input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidposs_alms_set td.poss_alms input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidposs_unfreep_set td.poss_unfree_persons input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidposs_revenuesilver_set td.poss_revsilver input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidposs_revenuekind_set td.poss_revkind input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidposs_pgeneral_set td.poss_pgeneral input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidposs_office_set td.poss_office input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidposs_objects_set td.poss_object input").attr("SIZE", "50"); // m2m fields
	$("tr.dynamic-assocfactoidposs_lands_set td.poss_land input").attr("SIZE", "50"); // m2m fields
}



// give time to jquery to load..
setTimeout("update_document();", 1000);

