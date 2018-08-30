from django import template

from wagtail.wagtailcore.models import Page

register = template.Library()

def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.inclusion_tag('includes/navigation.html', takes_context=True)
def main_menu(context, root, current_page=None):
    """Returns the main menu items, the children of the root page. Only live
    pages that have the show_in_menus setting on are returned."""
    menu_pages = root.get_children().filter(live=True, show_in_menus=True)

    for menu_page in menu_pages:
        menu_page.show_dropdown = has_menu_children(menu_page)

    return {'request': context['request'], 'root': root,
            'current_page': current_page, 'menu_pages': menu_pages}


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    """Returns the site root Page, not the implementation-specific model used.

    :rtype: `wagtail.wagtailcore.models.Page`
    """
    return context['request'].site.root_page

@register.simple_tag()
def get_wagtail_page(slug):
    pages = Page.objects.filter(slug=slug)
    if pages.count() > 0:
        return pages[0]
    return None




@register.filter
def is_current_or_ancestor(page, current_page):
    """Returns True if the given page is the current page or is an ancestor of
    the current page."""
    return current_page.is_current_or_ancestor(page)
