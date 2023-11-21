from django.contrib import admin

from sna.models import *  # noqa


class LegendInline(admin.StackedInline):
    model = LegendItem
    extra = 1


class BasicAdmin(admin.ModelAdmin):
    inlines = [LegendInline, ]


admin.site.register(GephiVis, BasicAdmin)
