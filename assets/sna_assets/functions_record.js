/* creator: michelepasin */


Cufon.replace('.nvg a', {fontSize: '16px'});
Cufon.replace('.c h3' , {fontSize: '22px'});
Cufon.replace('.nvl a', {fontSize: '14px'});
Cufon.replace('.nvh h4', {fontSize: '14px'});
Cufon.replace('.tsn a', {fontSize: '16px'});
Cufon.replace('.ct h2');






$(document).ready(function() {
    $('html').addClass('j');
    $('a[rel]').click(function () {
        var linkTarget = $(this).attr('rel');
        if (linkTarget == 'external') {
            linkTarget = '_blank'
        };
        $(this).attr({'target':linkTarget});
    });
    $(".nvh h5 label").overlabel();


    $("#tabs").tabs();

    $("#results").css('overflow', 'auto');


    // toggle_citationpanel();
    // toggle_historypanel();

/* Tipsy tool tips */
   try {
       $(".tip").tipsy({
           delayIn: 500,
           delayOut: 500,
           fade: true
       });
   } catch(e) {
       // pass
       }


});


jQuery.fn.simple_blink = function() {
    return this.fadeOut("fast").fadeIn("slow");
};
jQuery.fn.add_loading_icon = function() {
    loadingData = "<img src='/media/static/paul/i/g.gif' alt='loading data' />"
    return this.empty().append(loadingData);
};

// ///////////////////////////////////////////////////


// for the Person/Source record-page
function update_related_factoids(page, ordering, tab){
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
function update_source_factoids(page, ordering, tab){
    if (!tab) var tab = "fragment-1";   // we pass the tab-ids directly in the functions... might be done dynamically later..
    $("#" + tab).add_loading_icon();
    ajax_update_tabs("#" + tab, "", tab, page, ordering);
}



 /*
main AJAX cals */


// name (= value in the facet), type(facet group), facet (the facet within a group) identify a value uniquely
function ajax_update_tabs(divname, ajaxcall, tab, page, ordering) {
    if (!page) var page = 1;   // if no page defaults to 1
    if (!tab) var tab = 1;   // if no page defaults to 1
    if (!ordering) var ordering = 'default';   // if no page defaults to 1person_detail

    $.get(ajaxcall,
         { tab: tab, page: page, ordering: ordering},
              function(data){
                 $(divname).empty().append(data);
                // reload qtips
                 qtip_previews();
              }
   );
}








// ;;--------
// ;  Mon Aug 20 12:37:31 BST 2012
// ;  QTIPS
// ;;--------




function qtip_labs(){
    // labs integration
    $('.labslink').qtip({
        // content: 'this is a tooltip',
        content: {  attr: 'alt' },
        position: {
            my: 'top left',
            at: 'bottom right'
        },
        show: 'mouseover',
        style: {
            tip: true,
            classes: 'ui-tooltip-nav'
        },
        effect: function() { $(this).slideDown(100); }, // Show
        effect: function() { $(this).slideUp(100); }, // Hide
    });
}



function qtip_history(){
    // overlay for history

    $('#historybutton').qtip(
    {
        id: 'modal', // Since we're only creating one modal, give it an ID so we can style it
        content: {
            text: $('#historyContent'),
            title: {
                text: 'History',
                button: true
            }
        },
        position: {
            my: 'center', // ...at the center of the viewport
            at: 'center',
            target: $(window)
        },
        show: {
            event: 'click', // Show it on click...
            solo: true, // ...and hide all other tooltips...
            modal: true // ...and make it modal
        },
        hide: false,
        style: 'ui-tooltip-light ui-tooltip-rounded'
    });
}


function qtip_citation(){

    // overlay for citation

    $('#citationbutton').qtip(
    {
        id: 'modal', // Since we're only creating one modal, give it an ID so we can style it
        content: {
            text: $('#citationContent'),
            title: {
                text: 'How to Cite this record',
                button: true
            }
        },
        position: {
            my: 'center', // ...at the center of the viewport
            at: 'center',
            target: $(window)
        },
        show: {
            event: 'click', // Show it on click...
            solo: true, // ...and hide all other tooltips...
            modal: true // ...and make it modal
        },
        hide: false,
        style: 'ui-tooltip-light ui-tooltip-rounded'
    });

}



function qtip_previews(STATIC_URL){

    if (!STATIC_URL) var STATIC_URL = "/media/static/";

    // ajax previews:
    $('a.no_extlink').each(function(){
        $(this).qtip({
            content: {
                text: '<img height="20" src="' + STATIC_URL + 'labs/img/loading.gif" alt="Loading..." />',
                ajax: {
                    url: $(this).attr('href') + "?preview=true" // Use the rel attribute of each element for the url to load
                },
                title: {
                    // Give the tooltip box a title
                    // text: $(this).attr('title'),
                    text: "Record Preview - <a href='" + $(this).attr('href') + "#'>click to show the full record</a> <small>(<a target='_blank' href='" + $(this).attr('href') + "#'>new tab</a>)</small>",
                    button: true
                }
            },
            style: {
                classes: 'ui-tooltip-bootstrap ui-tooltip-shadow'
            },

            show: {
                event: 'click',
                delay: 10,
                solo: true // Only show one tooltip at a time
            },

            position: {
                my: 'center', // ...at the center of the viewport
                at: 'center',
                target: $(window),
                        },

            hide: 'unfocus',
            })
        })
    // Make sure it doesn't follow the link when we click it
    .click(function(event) { event.preventDefault(); });

	$('#preview-map').each(function(){
		$(this).qtip({
			content: {
				text: '<img height="20" src="' + STATIC_URL + 'labs/img/loading.gif" alt="Loading..." />',
				ajax: {
					url: $(this).attr('href') // Use the rel attribute of each element for the url to load
				},
				title: {
					// Give the tooltip box a title 
					// text: $(this).attr('title'), 
					text: "Map Preview - <a href='" + $(this).attr('href') + "#'>click to show the full map</a> <small>(<a target='_blank' href='" + $(this).attr('href') + "#'>new tab</a>)</small>", 
					button: true
				}
			},
			style: {
				classes: 'ui-tooltip-bootstrap ui-tooltip-shadow ui-map'  
			},
			show: {
				event: 'click',
				delay: 10,
				solo: true // Only show one tooltip at a time
			},
			position: {
				my: 'center', // ...at the center of the viewport
				at: 'center',
				target: $(window),
			},
			hide: 'unfocus',
			})
		})			
	// Make sure it doesn't follow the link when we click it
	.click(function(event) { event.preventDefault(); });		
	
	
}























// USED?
//
//
// function toggle_citationpanel() {
//     $('#citationHandle').click(function() {
//      if (!$('#historyHandle').hasClass('buttonToggle')) {
//          // alert("history is still open");
//          $('#historyControl').animate({width: 'toggle'});
//          $('#historyHandle').toggleClass('buttonToggle');
//      }
//
//    $('#citationControl').animate({width: 'toggle'});
//        $(this).toggleClass('buttonToggle');
//      });
//  }
//
//
// function toggle_historypanel() {
//  $('#historyHandle').click(function() {
//      if (!$('#citationHandle').hasClass('buttonToggle')) {
//          // alert("search is still open");
//          $('#citationControl').animate({width: 'toggle'});
//          $('#citationHandle').toggleClass('buttonToggle');
//      }
//
//    $('#historyControl').animate({width: 'toggle'});
//    $(this).toggleClass('buttonToggle');
//  });
// }
//
//
//








