from django.db import models

"""
Wagtail classes to replace wordpress static pages
"""
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    promo_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    promo_caption = models.CharField(
        verbose_name='Caption',
        max_length=255,
        null=True,
        blank=True
    )

    link_1_title = models.CharField(
        verbose_name='Link 1 Title',
        max_length=255,
        null=True,
        blank=True
    )
    link_1_url = models.CharField(
        verbose_name='Link 1 URL',
        max_length=255,
        null=True,
        blank=True
    )
    link_1_thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Link 1 Thumbnail',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    link_2_title = models.CharField(
        verbose_name='Link 2 Title',
        max_length=255,
        null=True,
        blank=True
    )
    link_2_url = models.CharField(
        verbose_name='Link 2 URL',
        max_length=255,
        null=True,
        blank=True
    )
    link_2_thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Link 2 Thumbnail',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    link_3_title = models.CharField(
        verbose_name='Link 3 Title',
        max_length=255,
        null=True,
        blank=True
    )
    link_3_url = models.CharField(
        verbose_name='Link 3 URL',
        max_length=255,
        null=True,
        blank=True
    )
    link_3_thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Link 3 Thumbnail',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    link_4_title = models.CharField(
        verbose_name='Link 4 Title',
        max_length=255,
        null=True,
        blank=True
    )
    link_4_url = models.CharField(
        verbose_name='Link 4 URL',
        max_length=255,
        null=True,
        blank=True
    )
    link_4_thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Link 4 Thumbnail',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        MultiFieldPanel(
            [
                ImageChooserPanel('promo_image'),
                FieldPanel('promo_caption', classname='full')
            ],
            heading='Main Promo Image'
        ),
        MultiFieldPanel(
            [
                FieldPanel('link_1_title', classname='full'),
                FieldPanel('link_1_url', classname='full'),
                ImageChooserPanel('link_1_thumbnail'),
                FieldPanel('link_2_title', classname='full'),
                FieldPanel('link_2_url', classname='full'),
                ImageChooserPanel('link_2_thumbnail'),
                FieldPanel('link_3_title', classname='full'),
                FieldPanel('link_3_url', classname='full'),
                ImageChooserPanel('link_3_thumbnail'),
                FieldPanel('link_4_title', classname='full'),
                FieldPanel('link_4_url', classname='full'),
                ImageChooserPanel('link_4_thumbnail')
            ],
            heading='Homepage Links'
        )
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
