from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as django_settings
from django import forms
import datetime
import utils.modelextra.mymodels as mymodels

import mptt


# ++++
#  OLD STUFF USED TO IMPORT THE DATA - IT'S NOT USED ANYMORE
# ++++


class old_PossessionCurlew(mymodels.PomsModel):
    """(Possession description)"""
    possname = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="name",)
    nameextension = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="name extension",)
    parent = models.ForeignKey(
        'self', null=True, blank=True, verbose_name="parent", related_name='children')
    orderno = models.IntegerField(
        null=True, blank=True, verbose_name="order number",)
    lft = models.IntegerField(null=True, blank=True, verbose_name="lft?",)
    rgt = models.IntegerField(null=True, blank=True, verbose_name="rgf",)
    place = models.ForeignKey(
        'Place', null=True, blank=True, verbose_name="related place",)
    notes = models.TextField(null=True, blank=True, verbose_name="notes",)

    class Admin(admin.ModelAdmin):
        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()
        list_display = ('id', 'possname', 'editedrecord',
                        'review', 'updated_by', 'updated_at',)
        # filter_horizontal = ('location',)
        # radio_fields = {"ltbrole": admin.VERTICAL}
        list_filter = ['updated_at', 'updated_by', 'editedrecord', 'review', ]
        search_fields = ['id']
        fieldsets = [
            ('Administration',
             {'fields':
              ['editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'),
               ('updated_at', 'updated_by')
               ],
              'classes': ['collapse']
              }),
            ('Description',
             {'fields':
              ['possname', 'nameextension', 'parent', 'place', 'notes'	]
              }),

        ]

    class Meta:
        verbose_name_plural = "PossessionsOld - curlew"

    def __unicode__(self):
        return self.possname
    # table_order = 7
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 1


class old_PossessionMptt(mymodels.PomsModel):
    """(Possession description)"""
    possname = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="name",)
    nameextension = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="name extension",)
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name="parent",
                               related_name='children')
    # orderno = models.IntegerField(null=True, blank=True, verbose_name="order number",)
    # lft = models.IntegerField(null=True, blank=True, verbose_name="lft?",)
    theoldid = models.IntegerField(
        null=True, blank=True, verbose_name="the old id",)
    place = models.ForeignKey(
        'Place', null=True, blank=True, verbose_name="related place",)
    notes = models.TextField(null=True, blank=True, verbose_name="notes",)

    class Meta:
        verbose_name_plural = "Possession"
        ordering = ['tree_id', 'lft']

    def show_ancestors_tree(self):
        exit = ""
        for el in self.get_ancestors():
            exit += "%s>>>" % (el.possname)
        exit += self.possname
        return exit

    def __unicode__(self):
        exit = ""
        if self.parent:
            exit = "%s>>>" % (self.parent.possname)
        exit += self.possname
        return exit
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 2


mptt.register(old_PossessionMptt,)


class old_AssocFactoidPossession(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoidpos = models.ForeignKey('Factoid')
    possession_old = models.ForeignKey(
        'old_PossessionCurlew', verbose_name="possessions - old classification",)
    possession = models.ForeignKey('old_PossessionMptt', null=True, blank=True,
                                   verbose_name="possessions - new temp classification",)  # shall we keep this as the default one?
    originaltext = models.TextField(
        null=True, blank=True, verbose_name="original text",)
    # orderno = models.IntegerField(null=True, blank=True, verbose_name="order no",)

    class Admin(admin.ModelAdmin):
        list_display = ()
        search_fields = ()

    class Meta:
        pass

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)


# inline definition
class Assoc_FactPossessionInline(admin.StackedInline):
    model = old_AssocFactoidPossession
    raw_id_fields = ()
    verbose_name = 'Associated Possession'
    verbose_name_plural = 'Associated Possessions'
    extra = 1
    fieldsets = [
        ('',
         {'fields':
          ['possession_old', 'possession', 'originaltext'
           ],
          'classes': ['wide']

          }),

    ]


#  ===================
# then put in admin.py
#  ===================

#
# from pomsapp.models import *
# from django.contrib import admin
# import mptt
# from feincms.admin import editor
# from django.conf import settings
# from django.utils.translation import ugettext_lazy as _
#
# # the temp Possession - differs in the possname field...
# admin.site.register(Possession, OldGenericPossessionsAdmin)
# # the OLD POSSESSIONS ==> to be removed
# admin.site.register(PossessionOld, PossessionOld.Admin)
#
#
#
# # =========>>>>>>> the FEINCMS admin!!!!!!!!!!!!!!!!!
# class OldGenericPossessionsAdmin(editor.TreeEditor):
# 	# list_display = ('possname',)
# 	def save_model(self, request, obj, form, change):
# 		"""adds the user information when the rec is saved"""
# 		if getattr(obj, 'created_by', None) is None:
# 			  obj.created_by = request.user
# 		obj.updated_by = request.user
# 		obj.save()
# 	#  extending TreeAdmin's _actions_column
# 	def _actions_column(self, page):
# 		actions = super(OldGenericPossessionsAdmin, self)._actions_column(page)
# 		actions.insert(0, u'<a href="add/?parent=%s" title="%s"><img src="%simg/admin/icon_addlink.gif" alt="%s"></a>' % (
# 			page.pk, _('Add child page'), settings.ADMIN_MEDIA_PREFIX , _('Add child page')))
# #	 actions.insert(0, u'<a href="add/?parent=%s" title="%s"><img src="%simg/admin/icon_addlink.gif" alt="%s"></a>' % (
# #		 page.pk, _('Add child page'), django_settings.ADMIN_MEDIA_PREFIX ,_('Add child page')))
# #	 actions.insert(0, u'<a href="%s" title="%s"><img src="%simg/admin/selector-search.gif" alt="%s" /></a>' % (
# #		 page.get_absolute_url(), _('View on site'), django_settings.ADMIN_MEDIA_PREFIX, _('View on site')))
# 		return actions
# 	list_display = ( 'possname', 'id', 'parent', 'editedrecord', 'review','updated_by', 'updated_at',)
# 	# filter_horizontal = ('location',)
# 	# radio_fields = {"ltbrole": admin.VERTICAL}
# 	list_filter = ['updated_at', 'updated_by', 'editedrecord', 'review', 'parent']
# 	search_fields = ['id', 'possname']
# 	fieldsets = [
# 		('Administration',
# 			{'fields':
# 				['editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'),
# 				  ('updated_at', 'updated_by')
# 				 ],
# 			'classes': ['collapse']
# 			}),
# 			('Description',
# 				{'fields':
# 					['possname', 'nameextension', 'parent', 'place', 'notes'	]
# 				}),
#
# 	]
#
