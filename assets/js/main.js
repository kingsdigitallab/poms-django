$(function() {
     $('a.async').click(function (e) {
            e.preventDefault();
            var facet_group = $(this).data('facet_group');
            var facet_name = $(this).data('facet_name');
            var index_type = $(this).data('index_type');
            var title = this;
            $.get("/browse/" + facet_group + "/" + facet_name + "/?index_type="+index_type, function (data) {
                var div = $('div.'+facet_group+'__'+facet_name);
                if (div.length > 0){
                    var content = div[0];
                    $(content).html(data);
                }

            });
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
    $('.facet-group-name').bind('click', function() {
        $(this).next('.facets-list').slideToggle(400).toggleClass('hide');
        $(this).toggleClass('active');
        return false;
    });
});
