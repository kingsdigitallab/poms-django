// Filter facet choices for quick searching
var filterFacets = function () {
    var value = $(this).val().toLowerCase();
    var facet = $(this).data('facet');
    $("ul." + facet + "_choices li").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
}


$(function () {
    $('a.async').click(function (e) {
        e.preventDefault();
        var facet_group = $(this).data('facet_group');
        var facet_name = $(this).data('facet_name');
        var label=$(this).children('strong');
        if ($(this).attr('class').indexOf('loaded') < 0) {
            // Load the facet choices
            var selected_facets = $(this).data('selected_facets');
            var title = this;
            var url = "/browse/" + facet_group + "/" + facet_name + "/?";
            if (selected_facets && selected_facets.length > 0) {
                url += selected_facets;
            }
            if ($('div.' + facet_group + '__' + facet_name).html().length < 1) {
                $.get(url, function (data) {
                    var div = $('div.' + facet_group + '__' + facet_name);
                    if (div.length > 0) {
                        var content = div[0];
                        $(content).append(data);
                    }
                    $("#" + facet_name + "_facetfilter").on("keyup", filterFacets);
                    $(label).html($(label).html().replace('+','-'));
                });
            }

            $(this).toggleClass('loaded');
            $(this).toggleClass('active');
        } else{
            if ($(this).attr('class').indexOf('active') > 0){
                // Already loaded and open
                $(label).html($(label).html().replace('-','+'));
            } else{
                //Loaded and closed
                $(label).html($(label).html().replace('+','-'));
            }
            $('div.' + facet_group + '__' + facet_name).slideToggle(400);
            $(this).toggleClass('active');
        }

    });



    //new gRanger('#range', '#min', '#max');
});
