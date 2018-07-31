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

            });
        }
        /*
        if ($(title).data("load") == 1 &&factoidTypeKey > 0 && personid > 0) {
            $.get("/factoidgroup/" + personid + "/" + factoidTypeKey + "/", function (data) {
                var ul = $(title).next().children('ul');
                if (ul.length > 0) {
                    var content = ul[0];
                    $(content).html(data);
                    $(title).data("load",0);
                }
            });
        }*/
    });

    // Expand / Collapse
    $('.facet-group-name').bind('click', function () {
        $(this).next('.facets-list').slideToggle(400).toggleClass('hide');
        $(this).toggleClass('active');
        return false;
    });

    //new gRanger('#range', '#min', '#max');
});
