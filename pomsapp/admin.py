from django.utils.translation import ugettext_lazy as _

from pomsapp.models import *  # noqa
from utils.adminextra.autocomplete_tree_admin import AutocompleteTreeEditor
from django.contrib import admin

class BasicAdmin(admin.ModelAdmin):
    pass


# NOT TESTED YET !
# http://docs.djangoproject.com/en/dev/ref/contrib/
# admin/actions/#making-actions-available-site-wide
def make_edited(modeladmin, request, queryset):
    queryset.update(editedrecord=True)


make_edited.short_description = "Mark selected objects as edited"


def make_notedited(modeladmin, request, queryset):
    queryset.update(editedrecord=False)


make_notedited.short_description = "Mark selected objects as NOT edited"


def make_review(modeladmin, request, queryset):
    queryset.update(review=True)


make_review.short_description = "Mark selected objects as under review"


def make_notreview(modeladmin, request, queryset):
    queryset.update(review=False)


make_notreview.short_description = "Mark selected objects as NOT under review"

admin.site.add_action(make_edited, 'make_edited')
admin.site.add_action(make_notedited, 'make_notedited')
admin.site.add_action(make_review, 'export_selected')
admin.site.add_action(make_notreview, 'make_notreview')


# STANDARD admin definitions

class AuthListStandardAdmin(admin.ModelAdmin):
    """Standard admin definitions used by all authority lists"""

    def save_model(self, request, obj, form, change):
        """adds the user information when the rec is saved"""
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    list_display = (
        'id',
        'name',
        'description',
        'editedrecord',
        'review',
        'updated_by',
        'updated_at',
    )
    search_fields = ('name', 'id')
    list_filter = (
        'created_at',
        'updated_at',
        'created_by__username',
        'editedrecord',
        'review',
    )
    fieldsets = [
        ('Administration',
         {'fields':
          ['editedrecord', 'review', 'internal_notes', ('created_at',
                                                        'created_by'),
           ('updated_at', 'updated_by')
           ],
          'classes': ['collapse']
          }),
        ('Description',
         {'fields':
          ['name', 'description']
          }),

    ]


# =========>>>>>>> the FEINCMS admin!!!!!!!!!!!!!!!!!
class GenericPossessionsAdmin(AutocompleteTreeEditor):
    # list_display = ('possname',)
    def save_model(self, request, obj, form, change):
        """adds the user information when the rec is saved"""
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    #  extending TreeAdmin's _actions_column
    def _actions_column(self, page):
        actions = super(GenericPossessionsAdmin, self)._actions_column(page)
        actions.insert(0,
                       u'<a href="add/?parent=%s" title="%s">\
                         <img src="%simg/admin/icon_addlink.gif"\
                         alt="%s"></a>' % (
                           page.pk, _('Add child page'),
                           settings.MEDIA_URL, _('Add child page')))
        #  actions.insert(0, u'<a href="add/?parent=%s"
        # title="%s"><img src="%simg/admin/icon_addlink.gif"
        # alt="%s"></a>' % (
        # 	 page.pk, _('Add child page'), django_settings.
        # ADMIN_MEDIA_PREFIX ,_('Add child page')))
        #  actions.insert(0, u'<a href="%s" title="%s">
        # <img src="%simg/admin/selector-search.gif" alt="%s" /></a>'
        # % (
        # page.get_absolute_url(), _('View on site'),
        # django_settings.ADMIN_MEDIA_PREFIX, _('View on site')))
        return actions

    list_display = (
        'name',
        'id',
        'parent',
        'editedrecord',
        'review',
        'updated_by',
        'updated_at',
    )
    # filter_horizontal = ('location',)
    # radio_fields = {"ltbrole": admin.VERTICAL}
    list_filter = [
        'updated_at',
        'created_by__username',
        'editedrecord',
        'review',
        'util_topancestor']  # 'parent'
    search_fields = ['id', 'name']
    related_search_fields = {'parent': ('name',),
                             'place': ('name',)
                             }
    fieldsets = [
        ('Administration',
         {'fields':
          ['editedrecord', 'review', 'internal_notes',
           ('created_at', 'created_by'),
           ('updated_at', 'updated_by')
           ],
          'classes': ['collapse']
          }),
        ('Description',
         {'fields':
          ['name', 'nameextension', 'parent', 'notes']
          }),
        ('Place',
         {'fields':
          ['place', ]
          }),

    ]

    class Media:
        js = ("js/admin_fixes/admin_fixes.js",)


# ++AUDIO files admin definitions: MedievalGaelicForename
#  ModernGaelicForename

class AuthListAudiofileAdmin(admin.ModelAdmin):
    """Standard admin definitions used by all authority lists"""

    def save_model(self, request, obj, form, change):
        """adds the user information when the rec is saved"""
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    list_display = (
        'id',
        'name',
        'description',
        'editedrecord',
        'review',
        'updated_by',
        'updated_at',
    )
    search_fields = ('name', 'id')
    list_filter = (
        'updated_at',
        'created_by__username',
        'editedrecord',
        'review',
    )
    fieldsets = [
        ('Administration',
         {'fields':
          ['editedrecord', 'review', 'internal_notes',
           ('created_at', 'created_by'),
           ('updated_at', 'updated_by')
           ],
          'classes': ['collapse']
          }),
        ('Description',
         {'fields':
          ['name', 'description']
          }),
        ('Extra',
         {'fields':
          ['audiofile', ]
          }),

    ]


# ============================================================================


# ++++++++++++++++++++++++++++++
# authority lists admin definition
auth_lists = [MatrixShape, SealColor, AttachmentType, Role, Gender,
              Chartertype, Relationshipmetatype, Occupationtype,
              Exemptiontype, Nominalrendertype, Proanimagenerictypes,
              Renderdate, Sicutclausetype,
              Tenendasclauseoptions,
              Transactiontype, LegalPertinents, Returns_military,
              Returns_renders, CommonBurdens, Language,
              Referencetype]


def func(x):
    return admin.site.register(x, AuthListStandardAdmin)


map(func, auth_lists)

# ad hoc auth admins
admin.site.register(Relationshiptype, Relationshiptype.Admin)
admin.site.register(TitleType, TitleType.Admin)
admin.site.register(Floruit, Floruit.Admin)
admin.site.register(MedievalGaelicForename, AuthListAudiofileAdmin)
admin.site.register(ModernGaelicForename, AuthListAudiofileAdmin)

# ++++++++++++++++++++++++++++++
# admin definition for TREE models


possessions_lists = [Privileges, Poss_Alms, Poss_Unfree_persons,
                     Poss_Revenues_silver, Poss_Revenues_kind,
                     Poss_Office, Poss_Objects, Poss_Lands,
                     Poss_General, ]  # Possession

for possession in possessions_lists:
    admin.site.register(possession, GenericPossessionsAdmin)
# func = lambda x : admin.site.register(x, TestAdmin)
# map(func, possessions_lists)
# ad hoc possession admins


admin.site.register(Place, Place.Admin)

# ++++++++++++++++++++++++++++++
# admin definition for AUTH lists with AUDIO files


# ++++++++++++++++++++++++++++++
# admin definition for main DOMAIN models

# Created these objects to add search fields to make them work
# with Django 2 autocomplete

class SourceAdmin(admin.ModelAdmin):
    search_fields = ['hammondnumber','hammondnumb2','hammondnumb3','get_hammondnumber']


class RoleAdmin(admin.ModelAdmin):
    search_fields = ['name']

class Poss_AlmsAdmin(admin.ModelAdmin):
    search_fields = ['name']

class Poss_UnfreepersonsAdmin(admin.ModelAdmin):
    search_fields = ['name']

class Poss_OfficeAdmin(admin.ModelAdmin):
    search_fields = ['name']

class Poss_ObjectsAdmin(admin.ModelAdmin):
    search_fields = ['name']

class Poss_LandAdmin(admin.ModelAdmin):
    search_fields = ['name']

class TransactiontypeAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Transactiontype,TransactiontypeAdmin)
#admin.site.register(Poss_Lands,Poss_LandAdmin)
#admin.site.register(Poss_Objects,Poss_ObjectsAdmin)
#admin.site.register(Poss_Office,Poss_OfficeAdmin)
#admin.site.register(Poss_Unfree_persons,Poss_UnfreepersonsAdmin)
#admin.site.register(Poss_Alms,Poss_AlmsAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Charter, Charter.Admin)
admin.site.register(Seal, Seal.Admin)
admin.site.register(Matrix, Matrix.Admin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Person, Person.Admin)
admin.site.register(Factoid, Factoid.Admin)
admin.site.register(FactTitle, FactTitle.Admin)
admin.site.register(FactRelationship, FactRelationship.Admin)
# admin.site.register(FactOccupation, FactOccupation.Admin)
admin.site.register(FactPossession, FactPossession.Admin)
admin.site.register(FactReference, FactReference.Admin)
admin.site.register(FactTransaction, FactTransaction.Admin)
admin.site.register(PlaceType, PlaceType.Admin)
