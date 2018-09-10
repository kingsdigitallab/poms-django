from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as django_settings
from django import forms
import datetime
from utils.adminextra.autocomplete_tree_admin import *
from utils.myutils import blank_or_string, preview_string
import utils.modelextra.mymodels as mymodels


#
# AUTHORITY LISTS
#
# note that all these AL don't have UPDATED_AT / CREATED_AT info....
# they're inherited
class DocTickboxes(mymodels.PomsAuthorityList):

    """DocTickboxes authority list - name and desc fields are inherited, as well as timestamps
        This model IS NOT ADMINISTERED through the admin, but directly via code!
        ==> check in the action_models the relevant method.
    """

    class Meta:
        verbose_name_plural = "DocTickboxes"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class TransTickboxes(mymodels.PomsAuthorityList):

    """TransTickboxes authority list - name and desc fields are inherited, as well as timestamps
        This model IS NOT ADMINISTERED through the admin, but directly via code!
        ==> check in the action_models the relevant method.
    """

    class Meta:
        verbose_name_plural = "TransTickboxes"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class GrantorCategory(mymodels.PomsAuthorityList):

    """GrantorCategory authority list - name and desc fields are inherited, as well as timestamps
        This model IS NOT ADMINISTERED through the admin, but directly via code!
        ==> check in the action_models the relevant method.
    """

    class Meta:
        verbose_name_plural = "Grantor Categories"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class MatrixShape(mymodels.PomsAuthorityList):

    """MatrixShape authority list - name and desc fields are inherited, as well as timestamps"""

    class Meta:
        verbose_name_plural = "Matrix Shape"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class SealColor(mymodels.PomsAuthorityList):

    """SealColor authority list - name and desc fields are inherited, as well as timestamps"""

    class Meta:
        verbose_name_plural = "Seal Color"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class AttachmentType(mymodels.PomsAuthorityList):

    """AttachmentType authority list (for seals) - name and desc fields are inherited, as well as timestamps"""

    class Meta:
        verbose_name_plural = "Attachment Type"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Role(mymodels.PomsAuthorityList):

    """(this was called 'Factoidpersontype')"""
    # rolename = models.CharField(max_length=300)
    # what is this for?
    spiritualbenefit = models.BooleanField(
        default=False, blank=True, verbose_name="spiritual benefits",)

    class Meta:
        verbose_name_plural = "Roles"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    table_group = 'Authority lists'


class TitleType(mymodels.PomsAuthorityList):

    """(TitleType description)"""
    placefk = models.ForeignKey(
        'Place', null=True, blank=True, verbose_name="Place related",)

    class Admin(NoLookupsForeignKeyAutocompleteAdmin):
        related_search_fields = {'placefk': ('name',), }

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()
        list_display = ('id', 'name', 'description', 'placefk',
                        'editedrecord', 'review', 'updated_by', 'updated_at',)
        search_fields = ('name', 'id')
        list_filter = (
            'updated_at', 'created_by__username', 'editedrecord', 'review', )
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
                    ['name', 'description', 'placefk', ],
                 }),

        ]

        class Media:
            js = ("js/admin_fixes/admin_fixes.js",)

    class Meta:
        verbose_name_plural = "titles"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


#  this NEEDS a different admin probably....
class Floruit(mymodels.PomsAuthorityList):
    eml = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="modifier",)
    century = models.CharField(
        max_length=60, null=True, blank=True, verbose_name="century",)
    startyear = models.IntegerField(
        null=True, blank=True, verbose_name="start year",)
    endyear = models.IntegerField(
        null=True, blank=True, verbose_name="end year",)

    class Meta:
        verbose_name_plural = "floruit"

    class Admin(admin.ModelAdmin):

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()
        list_display = ('id', 'name', 'description', 'startyear',
                        'endyear', 'editedrecord', 'review', 'updated_by', 'updated_at',)
        search_fields = ('name',)
        list_filter = (
            'updated_at', 'created_by__username', 'editedrecord', 'review', )
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
                    ['name', 'description', 'startyear', 'endyear'],
                 }),

        ]

    def __unicode__(self):
        return self.eml + self.century
        # return 'Id[%s], Type[%s], Date[%s], Title[%s]' % (self.id,

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Gender(mymodels.PomsAuthorityList):
    # genderfull = models.CharField(max_length=120)
    # genderabrv = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "gender"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


# 29 June 2010 ******************************************************************
# a proxy model for the FB: excludes Institutions because it has a
# separate facet

class GenderNoInstitution_Manager(models.Manager):

    def get_query_set(self):
        return super(GenderNoInstitution_Manager, self).get_query_set().exclude(id=5)


class GenderNoInstitution(Gender):
    objects = GenderNoInstitution_Manager()

    class Meta:
        proxy = True


class Chartertype(mymodels.PomsAuthorityList):
    # chartertypename = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "charter types"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Relationshipmetatype(mymodels.PomsAuthorityList):

    """(Relationshiptype description)"""
    # categorytype = models.CharField(max_length=600, null=True, blank=True, verbose_name="category type",)
    # name = models.CharField(max_length=600)
    class Meta:
        verbose_name_plural = "relationship type"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


# from pomsapp.widgets import *

# this AUTHLIST has a custom admin
class Relationshiptype(mymodels.PomsAuthorityList):

    """(Relationshiptype description)"""
    metatype = models.ForeignKey(
        'Relationshipmetatype', null=True, blank=True, verbose_name="relation type",)
    # name = models.CharField(max_length=600)

    class Meta:
        verbose_name_plural = "relationship"
        verbose_name = "relationship"
        ordering = ['name']

    class Admin(admin.ModelAdmin):

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()
        list_display = ('id', 'name', 'description',
                        'editedrecord', 'review', 'updated_by', 'updated_at',)
        search_fields = ('name',)
        list_filter = (
            'updated_at', 'created_by__username', 'editedrecord', 'review', )
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
                    ['name', 'metatype', 'description']
                 }),

        ]

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Referencetype(mymodels.PomsAuthorityList):

    """(Occupationtype description)"""
    # name = models.CharField(max_length=765)
    class Meta:
        verbose_name_plural = "reference type"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Occupationtype(mymodels.PomsAuthorityList):

    """(Occupationtype description)"""
    # name = models.CharField(max_length=765)
    class Meta:
        verbose_name_plural = "occupation type"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Exemptiontype(mymodels.PomsAuthorityList):

    """(Exemptiontype description)"""
    # name = models.CharField(max_length=765, null=True, blank=True,
    # verbose_name="name",)
    class Meta:
        verbose_name_plural = "exemption type"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Nominalrendertype(mymodels.PomsAuthorityList):

    """(Nominalrendertype : )"""
    # rendername = models.CharField(max_length=765, null=True, blank=True,
    # verbose_name="name",)
    class Meta:
        verbose_name_plural = "nominal render type"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


# these are the SPIRITUAL BENEFITS!
class Proanimagenerictypes(mymodels.PomsAuthorityList):

    """(Proanimagenerictypes description) = spiritual benefits"""
    # name = models.CharField(max_length=765, null=True, blank=True,
    # verbose_name="name",)
    orderno = models.IntegerField(null=True, blank=True, verbose_name="order",)
    newline = models.IntegerField(
        null=True, blank=True, verbose_name="newline",)  # this field should not be needed anymore

    class Meta:
        verbose_name_plural = "proanima generic types (= Spiritual Benefits)"
        verbose_name = "proanima generic types (= Spiritual Benefits)"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Renderdate(mymodels.PomsAuthorityList):

    """(Renderdate description)"""
    # name = models.CharField(blank=True, max_length=200, verbose_name="name")
    class Meta:
        verbose_name_plural = "render date"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'

#  check if these fields are still needed....


class Sicutclausetype(mymodels.PomsAuthorityList):

    """(Sicutclausetype description)"""
    # name = models.CharField(max_length=765, null=True, blank=True,
    # verbose_name="name",)
    orderno = models.IntegerField(null=True, blank=True, verbose_name="order",)
    newline = models.IntegerField(
        null=True, blank=True, verbose_name="newline",)

    class Meta:
        verbose_name_plural = "sicut clause type"
        ordering = ['name']

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    table_group = 'Authority lists'


class Tenendasclauseoptions(mymodels.PomsAuthorityList):

    """(Tenendasclauseoptions description)"""
    # name = models.CharField(blank=True, max_length=200, verbose_name="name")
    class Meta:
        verbose_name_plural = "tenendas clause options"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
    table_group = 'Authority lists'


class Transactiontype(mymodels.PomsAuthorityList):

    """(Transactiontype description)"""
    # name = models.CharField(blank=True, max_length=200, verbose_name="name")
    class Meta:
        verbose_name_plural = "transaction type"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
    table_group = 'Authority lists'


# new models added on 5Jun to handle the 'tickbox' options table
# basically we're making all of those things explicit!

class LegalPertinents(mymodels.PomsAuthorityList):

    """(LegalPertinents description)"""
    # name = models.CharField(blank=True, max_length=100, verbose_name="name")
    # extendedname = models.CharField(blank=True, max_length=100,
    # verbose_name="extended name")
    class Meta:
        verbose_name_plural = "Legal Pertinents"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Returns_military(mymodels.PomsAuthorityList):

    """(Returns_military description)"""
    # name = models.CharField(blank=True, max_length=100, verbose_name="name")
    # extendedname = models.CharField(blank=True, max_length=100,
    # verbose_name="extended name")
    class Meta:
        verbose_name_plural = "Returns military"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Returns_renders(mymodels.PomsAuthorityList):

    """(Returns_renders description)"""
    # name = models.CharField(blank=True, max_length=100, verbose_name="name")
    # extendedname = models.CharField(blank=True, max_length=100,
    # verbose_name="extended name")
    class Meta:
        verbose_name_plural = "Returns renders"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class CommonBurdens(mymodels.PomsAuthorityList):

    """(CommonBurdens description)"""
    # name = models.CharField(blank=True, max_length=100, verbose_name="name")
    # extendedname = models.CharField(blank=True, max_length=100,
    # verbose_name="extended name")
    class Meta:
        verbose_name_plural = "Common Burdens"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class Language(mymodels.PomsAuthorityList):

    """(Languages used in Documents)"""
    # name = models.CharField(blank=True, max_length=100, verbose_name="name")
    # extendedname = models.CharField(blank=True, max_length=100,
    # verbose_name="extended name")
    class Meta:
        verbose_name_plural = "Languages"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
    table_group = 'Authority lists'


#  new 18/1/2010


def medieval_audio_file_name(instance, filename):
    return '/'.join(['uploads/audio/medieval', instance.name, filename])


def modern_audio_file_name(instance, filename):
    return '/'.join(['uploads/audio/modern', instance.name, filename])


class MedievalGaelicForename(mymodels.PomsAuthorityList):

    """(MedievalGaelicForename for the Person template)"""
    audiofile = models.FileField(
        blank=True, upload_to=medieval_audio_file_name,  verbose_name="audio recording",
        help_text="upload a file in WAV or MP3 format [beta-stage functionality, can't remove a saved file  for the moment but just overwrite it]")

    class Meta:
        verbose_name_plural = "Medieval Gaelic Forenames"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'


class ModernGaelicForename(mymodels.PomsAuthorityList):

    """(ModernGaelicForename for the Person template)"""
    audiofile = models.FileField(
        blank=True, upload_to=modern_audio_file_name,  verbose_name="audio recording",
        help_text="upload a file in WAV or MP3 format [beta-stage functionality, can't remove a saved file  for the moment but just overwrite it]")

    class Meta:
        verbose_name_plural = "Modern Gaelic Forenames"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
    table_group = 'Authority lists'

#
# choices for DATES and related stuff


DAY_CHOICES = [  # (0, "undefined"),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20),
    (21, 21),
    (22, 22),
    (23, 23),
    (24, 24),
    (25, 25),
    (26, 26),
    (27, 27),
    (28, 28),
    (29, 29),
    (30, 30),
    (31, 31)
]

WEEKDAY_CHOICES = [
    # (0, "undefined"),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
]

MON_CHOICES = [
    # (0, "undefined"),
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
]

SEASON_CHOICES = [
    # (0, "undefined"),
    (1, 'Spring'),
    (2, 'Summer'),
    (3, 'Autumn'),
    (4, 'Winter'),
]


#   years not used
# years = [(i, i) for i in range(1300,2010)]
# YEAR_CHOICES =    years.insert(0, (0, 'undefined'))

# modifier before the weekday
DATE_MODIFIERS = [
    # ('exa', 'exactly'),
    ('cir', 'circa'),
    ('by', 'by'),
    ('bef', 'before'),
    ('aft', 'after'),
]

# modifier before the month/season
DATE_MODIFIERS2 = [
    ('mid', 'mid'),
    ('ear', 'early'),
    ('lat', 'late'),
]


PONELINK_SURENESS = [
    ('con', 'confident'),
    ('pro', 'probably'),
    ('unl', 'unlikely'),
    ('fam', 'from the same family'),
]
