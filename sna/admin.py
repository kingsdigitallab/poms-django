from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *
from django.utils.translation import ugettext_lazy as _

from sna.models import *



class LegendInline(admin.StackedInline):
    model = LegendItem
    extra = 1



class BasicAdmin(admin.ModelAdmin):
    inlines = [LegendInline,]




admin.site.register(GephiVis, BasicAdmin)

