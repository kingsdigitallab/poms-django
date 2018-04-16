from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as django_settings
from django import forms
import datetime
from utils.myutils import blank_or_string, preview_string
import utils.modelextra.mymodels as mymodels
# from django_extensions.admin.inline_autocomplete import *
from utils.adminextra.autocomplete_tree_admin import InlineAutocompleteAdmin


from pomsapp.models_authlists import TitleType


#  ====================================

# ASSOC to FACTOIDS

#  ====================================


class AssocFactoidPerson(mymodels.TimeStampedHiddenModel):
    #factoidpersonkey = models.IntegerField()
    factoid = models.ForeignKey('Factoid')
    person = models.ForeignKey('Person')
    # person = AjaxForeignKeyField('Person', (('name', {})))
    role = models.ForeignKey(
        'Role', null=True, blank=True, verbose_name="role",)
    nameoriglang = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="nameoriglang", )
    nametranslation = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="nametranslation",)
    standardmedievalform = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="standardmedievalform",)
    orderno = models.IntegerField(
        null=True, blank=True, verbose_name="Order number",)

    class Meta:
        # pass
        ordering = ['orderno']

    def save(self, force_insert=False, force_update=False):
        """fills out the shortdesc of Factoid Relationship depending on wheter there is an 
        associated person with a <Primary> role specified. We had to use this save() method instead of 
        the FactRelationship one because this gets saved *after* that...."""
        super(AssocFactoidPerson, self).save(force_insert, force_update)
        save_helperAssociation(self)
        # first let's make sure it's a relationship factoid
        factoidtype = self.factoid.get_right_subclass()
        # in some case we have junk-factoids that have no types, to be deleted
        # so we are making sure this is a 'good' factoid
        if factoidtype:
            if factoidtype[0] in ["relationship", "title/occupation"]:
                this_factoid = factoidtype[1]
                if this_factoid.shortdesc == "":
                    if factoidtype[0] == "relationship":
                        # for all Assoc objects having this related factoid
                        for assoc in AssocFactoidPerson.objects.filter(factoid=this_factoid):
                            primary_person = ""
                            relat_name = ""
                            relat_meta_name = ""
                            particle = ""
                            if assoc.role.name == "Primary":
                                particle = "of"
                                primary_person = assoc.person
                                if this_factoid.relationship:
                                    relat_name = this_factoid.relationship.name
                                    if this_factoid.relationship.metatype:
                                        relat_meta_name = this_factoid.relationship.metatype.name
                                this_factoid.shortdesc = "%s %s %s (%s)" % (
                                    relat_name, particle, primary_person, relat_meta_name)
                                this_factoid.save()
                    if factoidtype[0] == "title/occupation":
                        # for all Assoc objects having this related factoid
                        for assoc in AssocFactoidPerson.objects.filter(factoid=this_factoid):
                            primary_person = ""
                            title_name = ""
                            particle = ""
                            if assoc.role.name == "Primary":
                                particle = "of"
                                primary_person = assoc.person
                                if this_factoid.titletypekey:
                                    title_name = this_factoid.titletypekey.name
                                # this_factoid.shortdesc = "%s, %s" % (primary_person, title_name,)
                                this_factoid.shortdesc = "%s" % (title_name,)
                                this_factoid.save()

    def delete(self):
        existing_obj = AssocHelperPerson.objects.filter(
            helper_oldid=self.id, helper_type=self.__class__.__name__)
        if existing_obj:
            print("AssocHelperPerson: deleting object........")
            obj = existing_obj[0]
            obj.delete()
        super(AssocFactoidPerson, self).delete()

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)


class AssocFactoidWitness(mymodels.TimeStampedHiddenModel):
    #factoidpersonkey = models.IntegerField()
    factoid = models.ForeignKey('Factoid')
    person = models.ForeignKey('Person')
    role = models.ForeignKey(
        'Role', null=True, blank=True, verbose_name="role",  default=4)
    nameoriglang = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="nameoriglang", )
    nametranslation = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="nametranslation",)
    standardmedievalform = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="standardmedievalform",)
    orderno = models.IntegerField(
        null=True, blank=True, verbose_name="Order number",)

    class Meta:
        # pass
        ordering = ['orderno']

    def save(self, force_insert=False, force_update=False):
        """saves the helper association model"""
        super(AssocFactoidWitness, self).save(force_insert, force_update)
        save_helperAssociation(self)

    def delete(self):
        existing_obj = AssocHelperPerson.objects.filter(
            helper_oldid=self.id, helper_type=self.__class__.__name__)
        if existing_obj:
            print("AssocHelperPerson: deleting object........")
            obj = existing_obj[0]
            obj.delete()
        super(AssocFactoidWitness, self).delete()

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)


# 16 Apr: added the role:40 (might not be in the local DB)
# 26 May: added the role:41 (might not be in the local DB)

class AssocFactoidProanima(mymodels.TimeStampedHiddenModel):
    #factoidpersonkey = models.IntegerField()
    factoidtrans = models.ForeignKey('Factoid')
    person = models.ForeignKey('Person')
    role = models.ForeignKey('Role', null=True, blank=True, verbose_name="role",
                             limit_choices_to={'id__in': [14, 22, 23, 30, 34, 40, 41]}, default=14)  # the ProAnima roles: not sure about default
    nameoriglang = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="nameoriglang", )
    nametranslation = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="nametranslation",)
    standardmedievalform = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="standardmedievalform",)
    orderno = models.IntegerField(
        null=True, blank=True, verbose_name="Order number",)

    class Meta:
        # pass
        ordering = ['orderno']

    def save(self, force_insert=False, force_update=False):
        """saves the helper association model"""
        super(AssocFactoidProanima, self).save(force_insert, force_update)
        save_helperAssociation(self)

    def delete(self):
        existing_obj = AssocHelperPerson.objects.filter(
            helper_oldid=self.id, helper_type=self.__class__.__name__)
        if existing_obj:
            print("AssocHelperPerson: deleting object........")
            obj = existing_obj[0]
            obj.delete()
        super(AssocFactoidProanima, self).delete()

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)


##################
#  Wed Sep	1 15:59:45 BST 2010
#  ASSOC MODEL THAT COMBINES ALL THE THREE ABOVE, FOR SEARCHING PURPOSES
#
# thid model requires adjustements in both SAVE and DELETE method of its 'source' modes above...
#
##################


# method used to create a mirror copy (normalized) of all associations together..
def save_helperAssociation(assoc):
    try:
        existing_obj = AssocHelperPerson.objects.filter(
            helper_oldid=assoc.id, helper_type=assoc.__class__.__name__)
        if existing_obj:  # try to see if we already have this obj saved
            print(
                "AssocHelperPerson: found existing object ... just updating.........")
            obj = existing_obj[0]
            if assoc.__class__ == AssocFactoidProanima:
                obj.factoid = assoc.factoidtrans
            else:
                obj.factoid = assoc.factoid
            obj.person = assoc.person
            obj.role = assoc.role
            obj.nameoriglang = assoc.nameoriglang
            obj.nametranslation = assoc.nametranslation
            obj.standardmedievalform = assoc.standardmedievalform
            obj.orderno = assoc.orderno

        else:  # in this case, create a new obj
            print("AssocHelperPerson: creating NEW object ...........")
            if assoc.__class__ == AssocFactoidProanima:
                obj = AssocHelperPerson(factoid=assoc.factoidtrans, person=assoc.person, role=assoc.role, nameoriglang=assoc.nameoriglang,
                                        nametranslation=assoc.nametranslation, standardmedievalform=assoc.standardmedievalform, orderno=assoc.orderno,
                                        helper_oldid=assoc.id, helper_type=assoc.__class__.__name__)
            else:
                obj = AssocHelperPerson(factoid=assoc.factoid, person=assoc.person, role=assoc.role, nameoriglang=assoc.nameoriglang,
                                        nametranslation=assoc.nametranslation, standardmedievalform=assoc.standardmedievalform, orderno=assoc.orderno,
                                        helper_oldid=assoc.id, helper_type=assoc.__class__.__name__)
        obj.save()
        print("Saved AssocHelperPerson [%d] Original ID: [%d]" % (
            obj.id, assoc.id))
    except:
        print("Error: could not save AssocHelperPerson")


class AssocHelperPerson(mymodels.TimeStampedHiddenModel):
    #factoidpersonkey = models.IntegerField()
    factoid = models.ForeignKey('Factoid')
    person = models.ForeignKey('Person')
    role = models.ForeignKey(
        'Role', null=True, blank=True, verbose_name="role", )
    nameoriglang = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="nameoriglang", )
    nametranslation = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="nametranslation",)
    standardmedievalform = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="standardmedievalform",)
    orderno = models.IntegerField(
        null=True, blank=True, verbose_name="Order number",)
    helper_oldid = models.IntegerField(
        verbose_name="the id of the original association",)
    helper_type = models.CharField(
        max_length=30, verbose_name="text representation of the assoc type of the original", )

    class Meta:
        # pass
        ordering = ['orderno']

    def __unicode__(self):
        return "%s %s" % ("AssocHelperPerson:", self.id)


#  ====================================

# POSSESSIONS ASSOCIATIONs

#  ====================================


# ++++
#  1
# ++++
class AssocFactoidPoss_alms(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoid = models.ForeignKey('Factoid')
    poss_alms = models.ForeignKey('Poss_Alms',	verbose_name="alms",)
    originaltext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="original text",)
    helper_inferred = models.BooleanField(
        default=False, verbose_name="Is True if a possession association has been inferred (for the FB)")

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)
# inline definition


class AssocFactoidPoss_almsInline(InlineAutocompleteAdmin):
    model = AssocFactoidPoss_alms
    # raw_id_fields = ('poss_alms',)
    verbose_name_plural = 'Alms (ex possessions)'
    exclude = ('helper_inferred',)
    extra = 1
    related_search_fields = {

        'poss_alms': ('name',),
    }


# ++++
#  2
# ++++
class AssocFactoidPoss_unfreep(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoid = models.ForeignKey('Factoid')
    poss_unfree_persons = models.ForeignKey(
        'Poss_Unfree_persons', verbose_name="unfree persons",)
    originaltext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="original text",)
    helper_inferred = models.BooleanField(
        default=False, verbose_name="Is True if a possession association has been inferred (for the FB)")

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)
# inline definition


class AssocFactoidPoss_unfreepInline(InlineAutocompleteAdmin):
    model = AssocFactoidPoss_unfreep
    # raw_id_fields = ('poss_unfree_persons', )
    verbose_name_plural = 'Unfree persons (ex possessions)'
    exclude = ('helper_inferred',)
    extra = 1
    related_search_fields = {
        'poss_unfree_persons': ('name',),
    }


# ++++
#  3
# ++++
class AssocFactoidPoss_revenuesilver(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoid = models.ForeignKey('Factoid')
    poss_revsilver = models.ForeignKey(
        'Poss_Revenues_silver', verbose_name="revenues in silver",)
    originaltext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="original text",)
    helper_inferred = models.BooleanField(
        default=False, verbose_name="Is True if a possession association has been inferred (for the FB)")

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)
# inline definition


class AssocFactoidPoss_revsilverInline(InlineAutocompleteAdmin):
    model = AssocFactoidPoss_revenuesilver
    # raw_id_fields = ('poss_revsilver', )
    verbose_name_plural = 'Revenues in silver (ex possessions)'
    exclude = ('helper_inferred',)
    extra = 1
    related_search_fields = {
        'poss_revsilver': ('name',),
    }


# ++++
#  4
# ++++
class AssocFactoidPoss_revenuekind(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoid = models.ForeignKey('Factoid')
    poss_revkind = models.ForeignKey(
        'Poss_Revenues_kind', verbose_name="revenues in kind",)
    originaltext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="original text",)
    helper_inferred = models.BooleanField(
        default=False, verbose_name="Is True if a possession association has been inferred (for the FB)")

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)
# inline definition


class AssocFactoidPoss_revkindInline(InlineAutocompleteAdmin):
    model = AssocFactoidPoss_revenuekind
    # raw_id_fields = ('poss_revkind', )
    verbose_name_plural = 'Revenues in kind (ex possessions)'
    exclude = ('helper_inferred',)
    extra = 1
    related_search_fields = {
        'poss_revkind': ('name',),
    }


# ++++
#  5
# ++++
class AssocFactoidPoss_pgeneral(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoid = models.ForeignKey('Factoid')
    poss_pgeneral = models.ForeignKey(
        'Poss_General', verbose_name="possessions in general",)
    originaltext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="original text",)
    helper_inferred = models.BooleanField(
        default=False, verbose_name="Is True if a possession association has been inferred (for the FB)")

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)
# inline definition


class AssocFactoidPoss_pgeneralInline(InlineAutocompleteAdmin):
    model = AssocFactoidPoss_pgeneral
    # raw_id_fields = ('poss_pgeneral', )
    verbose_name_plural = 'Possessions in general (ex possessions)'
    exclude = ('helper_inferred',)
    extra = 1
    related_search_fields = {
        'poss_pgeneral': ('name',),
    }


# ++++
#  6
# ++++
class AssocFactoidPoss_office(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoid = models.ForeignKey('Factoid')
    poss_office = models.ForeignKey('Poss_Office', verbose_name="office",)
    originaltext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="original text",)
    helper_inferred = models.BooleanField(
        default=False, verbose_name="Is True if a possession association has been inferred (for the FB)")

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)
# inline definition


class AssocFactoidPoss_officeInline(InlineAutocompleteAdmin):
    model = AssocFactoidPoss_office
    # raw_id_fields = ('poss_office', )
    verbose_name_plural = 'Office (ex. possessions)'
    exclude = ('helper_inferred',)
    extra = 1
    related_search_fields = {
        'poss_office': ('name',),
    }


# ++++
#  7
# ++++
class AssocFactoidPoss_objects(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoid = models.ForeignKey('Factoid')
    poss_object = models.ForeignKey('Poss_Objects', verbose_name="objects",)
    originaltext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="original text",)
    helper_inferred = models.BooleanField(
        default=False, verbose_name="Is True if a possession association has been inferred (for the FB)")

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)
# inline definition


class AssocFactoidPoss_objectsInline(InlineAutocompleteAdmin):
    model = AssocFactoidPoss_objects
    # raw_id_fields = ('poss_object', )
    verbose_name_plural = 'Objects (ex. possessions)'
    exclude = ('helper_inferred',)
    extra = 1
    related_search_fields = {
        'poss_object': ('name',),
    }


# ++++
#  8
# ++++
class AssocFactoidPoss_lands(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoid = models.ForeignKey('Factoid')
    poss_land = models.ForeignKey('Poss_Lands', verbose_name="lands",)
    originaltext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="original text",)
    helper_inferred = models.BooleanField(
        default=False, verbose_name="Is True if a possession association has been inferred (for the FB)")

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)
# inline definition


class AssocFactoidPoss_landsInline(InlineAutocompleteAdmin):
    model = AssocFactoidPoss_lands
    # raw_id_fields = ('poss_land', )
    verbose_name_plural = 'Lands (ex. possessions)'
    exclude = ('helper_inferred',)
    extra = 4
    related_search_fields = {
        'poss_land': ('name', ),  # 'name',
    }


# ++++
#  9
# ++++
class AssocFactoidPrivileges(mymodels.TimeStampedHiddenModel):
    """(used to be called 'Factoidpossession')"""
    factoid = models.ForeignKey('Factoid')
    privilege = models.ForeignKey('Privileges', verbose_name="privileges",)
    originaltext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="original text",)
    helper_inferred = models.BooleanField(
        default=False, verbose_name="Is True if a possession association has been inferred (for the FB)")

    def __unicode__(self):
        return "%s %s" % ("id:", self.id)
# inline definition


class AssocFactoidPrivilegesInline(InlineAutocompleteAdmin):
    model = AssocFactoidPrivileges
    # raw_id_fields = ('privilege', )
    verbose_name_plural = 'Privileges'
    exclude = ('helper_inferred',)
    extra = 2
    related_search_fields = {
        'privilege': ('name',),
    }


#	privileges = models.ForeignKey('Privileges', null=True, blank=True, verbose_name="privileges",)
#	originaltext = models.CharField(max_length=765, null=True, blank=True, verbose_name="original text",)
#	# orderno = models.IntegerField(null=True, blank=True, verbose_name="order no",)
#
#	def __unicode__(self):
#		return "%s %s" % ("id:", self.id)
#
# ## inline definition
# class AssocFactoidPoss_almsInline(admin.TabularInline):
#	model = AssocFactoidPoss_alms
#	raw_id_fields = ()
#	verbose_name = 'Associated Alms (possessions)'
#	# verbose_name_plural = 'Associated Possessions'
#	extra = 1
