from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtailmenus.models import MenuPage
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class BlogPage(MenuPage):
    # owner can be obtained from the owner attribute (in Page).
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('feed_image'),
    ]


class GenericPage(MenuPage):
    subtitle = models.CharField(blank=True, max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]


class HomePage(MenuPage):
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery Images"),  # the carousel on the page
        InlinePanel('main_cards', label="Card Views")
    ]


class PeopleDirectoryPage(MenuPage):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        InlinePanel('people')
    ]

class LinkPage(MenuPage):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        InlinePanel('links')
    ]

class ClubPage(MenuPage):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        InlinePanel('club')
    ]


class Club(Orderable):
    page = ParentalKey(ClubPage, related_name='club')
    name = models.CharField(max_length=200)
    description = RichTextField()
    leader = models.CharField(max_length=100)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name="+"
    )
    facebook_link = models.URLField(blank=True)
    email_address = models.EmailField(blank=True)
    twitter_link = models.URLField(blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('leader'),
        ImageChooserPanel('image'),
        FieldPanel('facebook_link'),
        FieldPanel('email_address'),
        FieldPanel('twitter_link')
    ]
class PageLinks(Orderable):
    page = ParentalKey(LinkPage, related_name='links')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    destination_page =  models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        ImageChooserPanel('image'),
        PageChooserPanel('destination_page')
    ]
class PersonProfile(Orderable):
    page = ParentalKey(PeopleDirectoryPage, related_name='people')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rolename = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        ImageChooserPanel('image'),
        FieldPanel('rolename'),
        FieldPanel('description'),
    ]


class MainPageStaticCard(Orderable):
    page = ParentalKey(HomePage, related_name="main_cards")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    card_title = models.CharField(blank=True, max_length=250)
    label = RichTextField(blank=True)
    destination_page =  models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('card_title'),
        FieldPanel('label'),
        PageChooserPanel('destination_page'),
    ]


class MainPageCarouselImage(Orderable):
    page = ParentalKey(HomePage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    title = models.CharField(blank=True, max_length=250)
    description = models.CharField(blank=True, max_length=500)
    primary = models.BooleanField(default=False)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('primary'),
    ]
