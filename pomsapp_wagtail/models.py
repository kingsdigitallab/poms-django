from django.db import models

"""
Wagtail classes to replace wordpress static pages
"""
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page



class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]


class IndexPage(Page):
    content = RichTextField(blank=True)

    search_name = 'Index Page'
    search_fields = Page.search_fields
    subpage_types = ['IndexPage', 'RichTextPage']

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full")
    ]


class RichTextPage(Page):
    content = RichTextField()

    search_fields = Page.search_fields
    search_name = 'Rich Text Page'
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full")
    ]
