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
    var closed_icon = '›';
    var open_icon = 'v';
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
            var url = "/browse/" + facet_group + "/" + facet_name + "/?"+$('#search_form').serialize();
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


    //new gRanger('#range', '#min', '#max');
});
