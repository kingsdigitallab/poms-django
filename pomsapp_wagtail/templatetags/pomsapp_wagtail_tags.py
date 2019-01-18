from django import template

from wagtail.core.models import Page

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


@register.inclusion_tag('tags/get_menu_pages.html', takes_context=True)
def get_menu_pages(context, page):
    """Returns the sidebar content  """
    children = None
    siblings = None
    if page:
        # Don't show siblings for first level
        if page.get_parent() != context['request'].site.root_page:
            children = page.get_children().filter(live=True,
                                                  show_in_menus=True)
            siblings = page.get_siblings().filter(live=True,
                                                  show_in_menus=True)
        else:
            # set children as siblings to only show one level
            siblings = page.get_children().filter(live=True,
                                                  show_in_menus=True)

    return {'children': children,
            'current_page': page, 'siblings': siblings}


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    """Returns the site root Page, not the implementation-specific model used.

    :rtype: `wagtail.core.models.Page`
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


@register.filter('startswith')
def startswith(text, starts):
    return text.startswith(starts)
