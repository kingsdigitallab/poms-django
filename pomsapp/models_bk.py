from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as django_settings
 
import datetime
from django import forms


import utils.adminextra.rangevaluesfilterspec
import utils.adminextra.alphabeticfilterspec
import utils.adminextra.buttonmodeladmin as extrab
import utils.modelextra.mymodels as mymodels
from pomsapp.widgets import *

import mptt
from feincms.admin import editor


######################
### AUTHORITY LISTS
######################

# note that all these AL don't have UPDATED_AT / CREATED_AT info....



class Role(mymodels.PomsAuthorityList):
	"""(this was called 'Factoidpersontype')"""
	# rolename = models.CharField(max_length=300)
	# what is this for?
	spiritualbenefit = models.BooleanField(default=False, blank=True, verbose_name="spiritual benefits",)
	class Meta:
		verbose_name_plural="Roles"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'



class TitleType(mymodels.PomsAuthorityList):
	"""(TitleType description)"""
	# titlename = models.CharField(max_length=300)	
	class Meta:
		verbose_name_plural="titles"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'



#  this NEEDS a different admin probably....
class Floruit(mymodels.PomsAuthorityList):
	eml = models.CharField(max_length=30, null=True, blank=True, verbose_name="",)
	century = models.CharField(max_length=60, null=True, blank=True, verbose_name="",)
	startyear = models.IntegerField(null=True, blank=True, verbose_name="",)
	endyear = models.IntegerField(null=True, blank=True, verbose_name="",)
	class Meta:
		verbose_name_plural="floruit"
	class Admin(admin.ModelAdmin):
		list_display = ()
		search_fields = ()
		ordering = ['name']
	def __unicode__(self):
	  return self.eml + self.century
		# return 'Id[%s], Type[%s], Date[%s], Title[%s]' % (self.id, 
	table_group = 'Authority lists'

class Gender(mymodels.PomsAuthorityList):
	# genderfull = models.CharField(max_length=120)
	# genderabrv = models.CharField(max_length=30)
	class Meta:
		verbose_name_plural="gender"
		ordering = ['name']
	def __unicode__(self):
	  return self.name
	table_group = 'Authority lists'

class Chartertype(mymodels.PomsAuthorityList):
	# chartertypename = models.CharField(max_length=300)
	class Meta:
		verbose_name_plural = "charter types"
		ordering = ['name']
	def __unicode__(self):
	  return self.name
	table_group = 'Authority lists'


class Relationshipmetatype(mymodels.PomsAuthorityList):
	"""(Relationshiptype description)"""
	# categorytype = models.CharField(max_length=600, null=True, blank=True, verbose_name="category type",)
	# name = models.CharField(max_length=600)
	class Meta:
		verbose_name_plural="relationship type"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'


# from pomsapp.widgets import *

# this AUTHLIST has a custom admin
class Relationshiptype(mymodels.PomsAuthorityList):
	"""(Relationshiptype description)"""
	metatype = models.ForeignKey('Relationshipmetatype', null=True, blank=True, verbose_name="relation type",)
	# name = models.CharField(max_length=600)
	class Meta:
		verbose_name_plural="relationship"
		verbose_name="relationship"
		ordering = ['name']

	class Admin(admin.ModelAdmin):
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			obj.save()
		list_display = ('id', 'name', 'description', 'editedrecord', 'review','updated_by', 'updated_at',)
		search_fields = ('name',)
		list_filter = ('updated_at', 'updated_by', 'editedrecord', 'review', )
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
	table_group = 'Authority lists'






class Occupationtype(mymodels.PomsAuthorityList):
	"""(Occupationtype description)"""	
	# name = models.CharField(max_length=765)
	class Meta:
		verbose_name_plural="occupation type"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'


class Exemptiontype(mymodels.PomsAuthorityList):
	"""(Exemptiontype description)"""
	# name = models.CharField(max_length=765, null=True, blank=True, verbose_name="name",)	
	class Meta:
		verbose_name_plural="exemption type"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'


class Nominalrendertype(mymodels.PomsAuthorityList):
	"""(Nominalrendertype : )"""
	# rendername = models.CharField(max_length=765, null=True, blank=True, verbose_name="name",)	
	class Meta:
		verbose_name_plural="nominalrendertype"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'
	


# these are the SPIRITUAL BENEFITS!
class Proanimagenerictypes(mymodels.PomsAuthorityList):
	"""(Proanimagenerictypes description) = spiritual benefits"""
	# name = models.CharField(max_length=765, null=True, blank=True, verbose_name="name",)
	orderno = models.IntegerField(null=True, blank=True, verbose_name="order",)				
	newline = models.IntegerField(null=True, blank=True, verbose_name="newline",) #this field should not be needed anymore
	class Meta:
		verbose_name_plural="proanima generic types"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'
	

class Renderdate(mymodels.PomsAuthorityList):
	"""(Renderdate description)"""
	# name = models.CharField(blank=True, max_length=200, verbose_name="name")	
	class Meta:
		verbose_name_plural="render date"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'
	
#  check if these fields are still needed....
class Sicutclausetype(mymodels.PomsAuthorityList):
	"""(Sicutclausetype description)"""
	# name = models.CharField(max_length=765, null=True, blank=True, verbose_name="name",)
	orderno = models.IntegerField(null=True, blank=True, verbose_name="order",)
	newline = models.IntegerField(null=True, blank=True, verbose_name="newline",)	
	class Meta:
		verbose_name_plural="sicut clause type"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'


class Tenendasclauseoptions(mymodels.PomsAuthorityList):
	"""(Tenendasclauseoptions description)"""
	# name = models.CharField(blank=True, max_length=200, verbose_name="name")
	class Meta:
		verbose_name_plural="tenendas clauseoptions"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'


class Transactiontype(mymodels.PomsAuthorityList):
	"""(Transactiontype description)"""
	# name = models.CharField(blank=True, max_length=200, verbose_name="name")
	class Meta:
		verbose_name_plural="transaction type"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'


# new models added on 5Jun to handle the 'tickbox' options table
# basically we're making all of those things explicit!

class LegalPertinents(mymodels.PomsAuthorityList):
	"""(LegalPertinents description)"""
	# name = models.CharField(blank=True, max_length=100, verbose_name="name")
	# extendedname = models.CharField(blank=True, max_length=100, verbose_name="extended name")
	class Meta:
		verbose_name_plural="LegalPertinents"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'

	
class Returns_military(mymodels.PomsAuthorityList):
	"""(Returns_military description)"""
	# name = models.CharField(blank=True, max_length=100, verbose_name="name")
	# extendedname = models.CharField(blank=True, max_length=100, verbose_name="extended name") 
	class Meta:
		verbose_name_plural="Returns_military"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'


class Returns_renders(mymodels.PomsAuthorityList):
	"""(Returns_renders description)"""
	# name = models.CharField(blank=True, max_length=100, verbose_name="name")
	# extendedname = models.CharField(blank=True, max_length=100, verbose_name="extended name") 
	class Meta:
		verbose_name_plural="Returns_renders"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'



class CommonBurdens(mymodels.PomsAuthorityList):
	"""(CommonBurdens description)"""
	# name = models.CharField(blank=True, max_length=100, verbose_name="name")
	# extendedname = models.CharField(blank=True, max_length=100, verbose_name="extended name") 
	class Meta:
		verbose_name_plural="CommonBurdens"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'


class Language(mymodels.PomsAuthorityList):
	"""(Languages used in Documents)"""
	# name = models.CharField(blank=True, max_length=100, verbose_name="name")
	# extendedname = models.CharField(blank=True, max_length=100, verbose_name="extended name") 
	class Meta:
		verbose_name_plural="Languages"
		ordering = ['name']
	def __unicode__(self):
		return self.name
	table_group = 'Authority lists'



		# class Monthname(models.Model):
		#	  monthnamekey = models.IntegerField()
		#	  shortname = models.CharField(max_length=30)
		#	  class Meta:
		#		  db_table = u'MonthName'
		#











#########################
##### POSSESSIONS and PRIVILEGES
#########################




class PossessionOld(mymodels.PomsModel):
	"""(Possession description)"""
	possname = models.CharField(max_length=765, null=True, blank=True, verbose_name="name",)
	nameextension = models.CharField(max_length=765, null=True, blank=True, verbose_name="name extension",)
	parent =  models.ForeignKey('PossessionOld', null=True, blank=True, verbose_name="parent", related_name='children')
	orderno = models.IntegerField(null=True, blank=True, verbose_name="order number",)
	lft = models.IntegerField(null=True, blank=True, verbose_name="lft?",)
	rgt = models.IntegerField(null=True, blank=True, verbose_name="rgf",)
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place",)
	notes = models.TextField(null=True, blank=True, verbose_name="notes",)	

	class Admin(admin.ModelAdmin):
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			obj.save()
		list_display = ('id', 'possname', 'editedrecord', 'review','updated_by', 'updated_at',)
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
		verbose_name_plural="PossessionsOld"
	def __unicode__(self):
		return self.possname
	# table_order = 7
	table_group = 'Possessions & Privileges [in progress]'
	table_order = 1




class Privileges(mymodels.PomsTreeModel):
	"""(Privileges description)"""
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='privilegeschildren')
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place (not used)",)

	class Meta:
		verbose_name_plural="Privileges"
		ordering = ['tree_id', 'lft']
	def __unicode__(self):
		return self.possname
	table_group = 'Possessions & Privileges [in progress]'
	table_order = 3





class Possession(mymodels.PomsModel):
	"""(Possession description)"""
	possname = models.CharField(max_length=765, null=True, blank=True, verbose_name="name",)
	nameextension = models.CharField(max_length=765, null=True, blank=True, verbose_name="name extension",)
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='children')
	# orderno = models.IntegerField(null=True, blank=True, verbose_name="order number",)
	# lft = models.IntegerField(null=True, blank=True, verbose_name="lft?",)
	theoldid = models.IntegerField(null=True, blank=True, verbose_name="the old id",)
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place",)
	notes = models.TextField(null=True, blank=True, verbose_name="notes",)	

	class Meta:
		verbose_name_plural="Possession"
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








class Poss_Alms(mymodels.PomsTreeModel):
	"""(Privileges description)"""
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='children')
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place (not used)",)

	class Meta:
		verbose_name_plural="Alms"
		ordering = ['tree_id', 'lft']
	def __unicode__(self):
		return self.possname
	table_group = 'Possessions & Privileges [in progress]'
	table_order = 4
		
class Poss_Lands(mymodels.PomsTreeModel):
	"""(Lands description)"""
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='children')
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place (not used)",)

	class Meta:
		verbose_name_plural="Lands"
		ordering = ['tree_id', 'lft']
	def __unicode__(self):
		return self.possname
	table_group = 'Possessions & Privileges [in progress]'
	table_order = 5
	
class Poss_Objects(mymodels.PomsTreeModel):
	"""(Lands description)"""
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='children')
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place (not used)",)

	class Meta:
		verbose_name_plural="Objects"
		ordering = ['tree_id', 'lft']
	def __unicode__(self):
		return self.possname
	table_group = 'Possessions & Privileges [in progress]'
	table_order = 6

class Poss_Revenues_silver(mymodels.PomsTreeModel):
	"""(Lands description)"""
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='children')
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place (not used)",)

	class Meta:
		verbose_name_plural="Revenues_in_silver"
		ordering = ['tree_id', 'lft']
	def __unicode__(self):
		return self.possname
	table_group = 'Possessions & Privileges [in progress]'
	table_order = 7
		
class Poss_Revenues_kind(mymodels.PomsTreeModel):
	"""(Lands description)"""
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='children')
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place (not used)",)

	class Meta:
		verbose_name_plural="Revenues_in_kind"
		ordering = ['tree_id', 'lft']
	def __unicode__(self):
		return self.possname
	table_group = 'Possessions & Privileges [in progress]'
	table_order = 8
		
class Poss_General(mymodels.PomsTreeModel):
	"""(Lands description)"""
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='children')
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place (not used)",)

	class Meta:
		verbose_name_plural="Possession_general"
		ordering = ['tree_id', 'lft']
	def __unicode__(self):
		return self.possname
	table_group = 'Possessions & Privileges [in progress]'
	table_order = 9
	
class Poss_Office(mymodels.PomsTreeModel):
	"""(Lands description)"""
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='children')
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place (not used)",)

	class Meta:
		verbose_name_plural="Office"
		ordering = ['tree_id', 'lft']
	def __unicode__(self):
		return self.possname
	table_group = 'Possessions & Privileges [in progress]'
	table_order = 10
		
class Poss_Unfree_persons(mymodels.PomsTreeModel):
	"""(Lands description)"""
	parent =  models.ForeignKey('self', null=True, blank=True, verbose_name="parent", 
			related_name='children')
	place = models.ForeignKey('Place', null=True, blank=True, verbose_name="related place (not used)",)

	class Meta:
		verbose_name_plural="Unfree_persons"
		ordering = ['tree_id', 'lft']
	def __unicode__(self):
		return self.possname
	table_group = 'Possessions & Privileges [in progress]'			
	table_order = 11
	


mptt.register(Possession,)


mptt.register( Poss_Alms,)
mptt.register( Poss_Unfree_persons,)
mptt.register( Poss_Revenues_silver,)
mptt.register( Poss_Revenues_kind,)
mptt.register(Poss_General,)
mptt.register( Poss_Office,)
mptt.register(Poss_Objects,)
mptt.register( Poss_Lands,)
mptt.register( Privileges,)









#########################
##### MAIN DOMAIN OBJECTS
#########################



# if USED, we'll have to use MPTT with PLACEs TOO!!! 

class Place(mymodels.PomsModel):
	"""(Place description)"""
	placename = models.CharField(max_length=765, null=True, blank=True, verbose_name="name",)
	genericname = models.CharField(max_length=765, null=True, blank=True, verbose_name="generic name",)
	articletext = models.CharField(max_length=765, null=True, blank=True, verbose_name="article text",)
	specificname = models.CharField(max_length=765, null=True, blank=True, verbose_name="specific name",)
	parent = models.ForeignKey('Place', null=True, blank=True, verbose_name="parent place", related_name="children",)
	orderno = models.IntegerField(null=True, blank=True, verbose_name="ordering",)
	lft = models.IntegerField(null=True, blank=True, verbose_name="lft?",)
	rgt = models.IntegerField(null=True, blank=True, verbose_name="rgt?",)
	notes = models.TextField(null=True, blank=True, verbose_name="notes",)	

	class Admin(admin.ModelAdmin):
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			obj.save()
		list_display = ('id', 'editedrecord', 'review','updated_by', 'updated_at',)
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
					['placename', 'genericname', 'articletext', 'specificname', 'notes' ]
					}),
	
		]
	class Meta:
		verbose_name_plural="Place"
	def __unicode__(self):
		return self.placename
	table_order = 6




class Person(mymodels.PomsModel):
	persondisplayname = models.CharField(max_length=255, null=True, blank=True, verbose_name="Surface name", )
	standardmedievalname = models.CharField(max_length=255, null=True, blank=True, verbose_name="Medieval name",)
	moderngaelicname = models.CharField(max_length=255, null=True, blank=True, verbose_name="Modern gaelic name",)
	persondescription = models.TextField(null=True, blank=True, verbose_name="biography",)

	floruitstartpre = models.CharField(max_length=50, null=True, blank=True, verbose_name="pre",)
	floruitstartyr = models.IntegerField(null=True, blank=True, verbose_name="year",)
	floruitstartpost = models.CharField(max_length=50, null=True, blank=True, verbose_name="post",)
	floruitendpre = models.CharField(max_length=50, null=True, blank=True, verbose_name="pre",)
	floruitendyr = models.IntegerField(null=True, blank=True, verbose_name="year",)
	floruitendpost = models.CharField(max_length=50, null=True, blank=True, verbose_name="post",)

	florlowkey =  models.ForeignKey('Floruit', null=True, blank=True, verbose_name="century", related_name='flor_lowKey',)
	florhikey =	 models.ForeignKey('Floruit', null=True, blank=True, verbose_name="century", related_name='flor_hiKey',)
	genderkey = models.ForeignKey('Gender', null=True, blank=True, verbose_name="Gender", )

	forename = models.CharField(max_length=765, verbose_name="Forename",  null=True, blank=True,)
	surname = models.CharField(max_length=765, verbose_name="Surname",	null=True, blank=True,)
	sonof = models.CharField(max_length=765, verbose_name="SonOf",	null=True, blank=True,)
	patronym = models.CharField(max_length=765, verbose_name="Patronym",  null=True, blank=True,)
	ofstring = models.CharField(max_length=765, verbose_name="ofString",  null=True, blank=True,)
	placeandinst = models.CharField(max_length=765, verbose_name="Place/ institutional",  null=True, blank=True,)
	datestring = models.CharField(max_length=765, verbose_name="Dates",	 null=True, blank=True,)

	# created_at = models.DateTimeField(auto_now_add=True)
	# updated_at = models.DateTimeField(auto_now=True)

	# the following two were in the DB but I took them away..
	# tstamp = models.DateTimeField()
	# creationdate = models.DateField(null=True, blank=True)

	def get_admin_url(self):
		return "/%sadmin/pomsapp/person/%s" % (django_settings.URL_PREFIX, self.id)		
	get_admin_url.allow_tags = True
	def get_databrowse_url(self):
		return "/%sdatabrowse/pomsapp/person/objects/%s" % (django_settings.URL_PREFIX,self.id)		
	get_databrowse_url.allow_tags = True	
	# returns all associations form a person:  method useful for template rendering
	def get_all_associations(self):
		return list(self.assocfactoidperson_set.all()) + list(self.assocfactoidproanima_set.all()) + list(self.assocfactoidwitness_set.all())
	get_all_associations.allow_tags = True

	# includes a mysterious example.com ?????
	@models.permalink
	def get_absolute_url(self):
		return ('person_detail', [str(self.id)])
	
	class Meta:
		ordering = ["persondisplayname"]
	class Admin(admin.ModelAdmin):
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			# procedure for creating the surface name
			if getattr(obj, 'persondisplayname', None) == "":
				composed_name = ""
				fore = getattr(obj, 'forename', None)
				sur = getattr(obj, 'surname', None)
				sonof = getattr(obj, 'sonof', None)
				patr = getattr(obj, 'patronym', None)
				ofstr = getattr(obj, 'ofstring', None)
				place = getattr(obj, 'placeandinst', None)
				dates = getattr(obj, 'datestring', None)
				composed_name = fore + " " + sur 
				if patr:
					composed_name += ", " + sonof + " " + patr 
				if place:
					composed_name += ", " + ofstr + " " + place
				composed_name += " " + dates								
				obj.persondisplayname = composed_name
			obj.save()

		list_display = ('id','persondisplayname', 'editedrecord', 'review','updated_by', 'updated_at',)
		# filter_horizontal = ('location',) 
		# radio_fields = {"ltbrole": admin.VERTICAL}
		list_filter = ['updated_at', 'updated_by', 'editedrecord', 'review', ]
		search_fields = ['persondisplayname']
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
					['persondisplayname', 'standardmedievalname', 'moderngaelicname', 
						'genderkey',	'persondescription',	]
					}),
			('Name components',			
				{'fields':	
					['forename', 'surname', 'sonof', 'patronym', 'ofstring', 'placeandinst', 'datestring' ]
					}),
			('Floruits',			
				{'fields':	# to be ORDERED
					[ ('florlowkey','floruitstartpre', 'floruitstartyr', 'floruitstartpost'),
					 ('florhikey', 'floruitendpre', 'floruitendyr', 'floruitendpost'),	]
					}),
			]
					
	def __unicode__(self):
	  return self.persondisplayname
	
	table_order = 5





class Source(mymodels.PomsModel):
	"""Metaclass for MAtrix, CHartes etc.. at the moment we're using only Charters"""
	#sourcekey = models.IntegerField() --> automatically created
	source_tradid = models.CharField(max_length=765, null=True, blank=True, verbose_name="Trad. ID",)
	#sourcetypekey = models.IntegerField()	--> not nec. cause we have subclasses
	description = models.TextField(null=True, blank=True, verbose_name="description",)
	sourcefordataentry = models.TextField(null=True, blank=True, verbose_name="source for data entry",)
	#otherprintedsources = models.TextField(blank=True)	 --> never used
	#manuscriptsource = models.TextField(blank=True)  --> never used
	
	hammondnumber = models.IntegerField(null=True, blank=True, verbose_name="calendar number #1",)
	hammondnumb2 = models.IntegerField(null=True, blank=True, verbose_name="#2",)
	hammondnumb3 = models.IntegerField(null=True, blank=True, verbose_name="#3",)
	hammondext = models.CharField(max_length=300, null=True, blank=True, verbose_name="ext.",)

	notes = models.TextField(null=True, blank=True, verbose_name="notes",)
	# I put at this level the date info specs
	probabledate = models.CharField(max_length=765, null=True, blank=True, verbose_name="prob date",)
	firmdate = models.CharField(max_length=765, null=True, blank=True, verbose_name="firm date",)
	datingnotes = models.TextField(null=True, blank=True, verbose_name="dating notes",)

	language = models.ForeignKey(Language, null=True, blank=True, verbose_name="language",
		default=1)
		
	def get_right_subclass(self):
		# once you get a source instance, it's useful to know quickly what subclass it is...
		try:
			sbcls = ["charter", self.charter]
		except:
			sbcls = None
		return sbcls
	get_right_subclass.allow_tags = True

	@models.permalink
	def get_absolute_url(self):
		return ('source_detail', [str(self.id)])

	class Meta:
		pass
	def __unicode__(self):
		#	  if self.source_tradid:
		# italic_name = self.source_tradid.replace("_", "<i>", 1)
		# italic_name = italic_name.replace("_", "</i>", 1)
	  out = "Charter %s/%s/%s %s (%s)" % (self.hammondnumber, self.hammondnumb2, self.hammondnumb3, self.hammondext, self.source_tradid)
	  return out
	table_order = 4



class Charter(Source):
	
	chartertypekey = models.ForeignKey('Chartertype', blank=True, null=True, verbose_name="charter type")

	ischirograph = models.BooleanField(default=False, verbose_name="Chirograph?") 
	doctypenotes = models.TextField(blank=True, verbose_name="Doc type notes")
	placedatemodern = models.CharField(max_length=765, null=True, blank=True, verbose_name="Place (modern)",)
	placedatedoc = models.CharField(max_length=765, null=True, blank=True, verbose_name="Place (document)",)

	letterpatent = models.BooleanField(default=False, verbose_name="referred to as letter patent")
	origcontemp = models.BooleanField(default=False, verbose_name="Original (contemporary)")
	duporigcontemp = models.BooleanField(default=False, verbose_name="Duplicate Original (contemporary)")
	orignoncontemp = models.BooleanField(default=False, verbose_name="Original (non-contemporary)")
	duporignoncontemp = models.BooleanField(default=False, verbose_name="Duplicate Original (non-contemporary)")

	def get_admin_url(self):
		return "/%sadmin/pomsapp/charter/%s" % (django_settings.URL_PREFIX, self.id)		
	get_admin_url.allow_tags = True
	def get_databrowse_url(self):
		return "/%sdatabrowse/pomsapp/charter/objects/%s" % (django_settings.URL_PREFIX, self.id)		
	get_databrowse_url.allow_tags = True

	class Meta:
		pass
	class Admin(admin.ModelAdmin):
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			obj.save()
		list_display = ('source_tradid', 'hammondnumber', 'hammondnumb2', 'hammondnumb3', 'hammondext',
		'editedrecord', 'review','updated_by', 'updated_at',)
		# raw_id_fields = ('chartertypekey',)
		# filter_horizontal = ('location',) 
		# radio_fields = {"ltbrole": admin.VERTICAL}
		list_filter = ['updated_at', 'updated_by', 'editedrecord', 'review', ]
		search_fields = ['source_tradid', 'hammondnumber', 'hammondnumb2', 'hammondnumb3', 'hammondext', ]
		fieldsets = [
			('Administration',	
				{'fields':	
					['editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'), 
					  ('updated_at', 'updated_by')
					 ],	 
				'classes': ['collapse']
				}),
			('ID',			
				{'fields':	 
					['source_tradid', ('hammondnumber', 'hammondnumb2', 'hammondnumb3', 'hammondext'),	]
					}),
			('Description',			
				{'fields':	
					[ 'chartertypekey', ('ischirograph', 'letterpatent', ), 'language', 'doctypenotes', 
					  'description', 'sourcefordataentry'	]
					}),
			('Dates',			
				{'fields':	
					[ 'firmdate', 'probabledate','datingnotes', ]
					}),
			('Place date',			
				{'fields':	
					['placedatemodern', 'placedatedoc',	 ]
					}),
			('Other info',			
				{'fields':	
					[('origcontemp', 'duporigcontemp','orignoncontemp',
					  'duporignoncontemp'), 'notes']
					}),

		]
	def __unicode__(self):
		#	  if self.source_tradid:
		# italic_name = self.source_tradid.replace("_", "<i>", 1)
		# italic_name = italic_name.replace("_", "</i>", 1)
	  out = "Charter %s/%s/%s %s (%s)" % (self.hammondnumber, self.hammondnumb2, self.hammondnumb3, self.hammondext, self.source_tradid)
	  return out
	table_order = 1





class Matrix(Source):
	# to be defined
	class Meta:
		pass
	class Admin(admin.ModelAdmin):
		list_display = ()
		search_fields = ()
	def __unicode__(self):
	  pass






#  ====================================

################ ASSOC to FACTOIDS

#  ====================================





class AssocFactoidPerson(mymodels.TimeStampedHiddenModel):
	#factoidpersonkey = models.IntegerField()
	factoid = models.ForeignKey('Factoid')
	person = models.ForeignKey('Person')
	# person = AjaxForeignKeyField('Person', (('name', {})))
	role = models.ForeignKey('Role', null=True, blank=True, verbose_name="role",)
	nameoriglang = models.CharField(max_length=765, null=True, blank=True, verbose_name="nameoriglang", )
	nametranslation = models.CharField(max_length=765, null=True, blank=True, verbose_name="nametranslation",)
	standardmedievalform = models.CharField(max_length=765, null=True, blank=True, verbose_name="standardmedievalform",)
	# porderno = models.IntegerField(null=True, blank=True, verbose_name="Order number",)
	class Meta:
		pass
	def save(self, force_insert=False, force_update=False):
		"""fills out the shortdesc of Factoid Relationship depending on wheter there is an 
		associated person with a <Primary> role specified. We had to use this save() method instead of 
		the FactRelationship one because this gets saved *after* that...."""
		super(AssocFactoidPerson, self).save(force_insert, force_update)
		# first let's make sure it's a relationship factoid 
		try:
			this_factoid = self.factoid.factrelationship
		except:
			this_factoid = ""
		if this_factoid:
			if this_factoid.shortdesc == "":
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
						this_factoid.shortdesc = "%s %s %s (%s)" % (relat_name, particle, primary_person, relat_meta_name)
						this_factoid.save()
		
	def __unicode__(self):
		return "%s %s" % ("id:", self.id)



# this model goes inline 
class AssocPersonInline(admin.TabularInline):
	model = AssocFactoidPerson
	verbose_name = 'Associated person'
	verbose_name_plural = 'Associated people'
	raw_id_fields = ( ) #'person', TOFIX
	extra = 2



class AssocFactoidWitness(mymodels.TimeStampedHiddenModel):
	#factoidpersonkey = models.IntegerField()
	factoid = models.ForeignKey('Factoid')
	person = models.ForeignKey('Person')
	role = models.ForeignKey('Role', null=True, blank=True, verbose_name="role",  default=4)
	nameoriglang = models.CharField(max_length=765, null=True, blank=True, verbose_name="nameoriglang", )
	nametranslation = models.CharField(max_length=765, null=True, blank=True, verbose_name="nametranslation",)
	standardmedievalform = models.CharField(max_length=765, null=True, blank=True, verbose_name="standardmedievalform",)
	# porderno = models.IntegerField(null=True, blank=True, verbose_name="Order number",)
	class Meta:
		pass

	def __unicode__(self):
		return "%s %s" % ("id:", self.id)
		
class AssocWitnessInline(admin.TabularInline):
	model = AssocFactoidWitness
	raw_id_fields = ()
	verbose_name = 'Associated witness'
	verbose_name_plural = 'Associated witnesses'
	extra = 1
	exclude = ['role']	# role is assigned by default



class AssocFactoidProanima(mymodels.TimeStampedHiddenModel):
	#factoidpersonkey = models.IntegerField()
	factoidtrans = models.ForeignKey('Factoid', related_name='assocfactoidproanima')
	person = models.ForeignKey('Person')
	role = models.ForeignKey('Role', null=True, blank=True, verbose_name="role",  
		limit_choices_to = {'id__in' : [14, 22, 23, 30]}, default=14 )	#the ProAnima roles: not sure about default
	nameoriglang = models.CharField(max_length=765, null=True, blank=True, verbose_name="nameoriglang", )
	nametranslation = models.CharField(max_length=765, null=True, blank=True, verbose_name="nametranslation",)
	standardmedievalform = models.CharField(max_length=765, null=True, blank=True, verbose_name="standardmedievalform",)
	# porderno = models.IntegerField(null=True, blank=True, verbose_name="Order number",)
	class Meta:
		pass

	def __unicode__(self):
		return "%s %s" % ("id:", self.id)

class AssocProanimaInline(admin.TabularInline):
	model = AssocFactoidProanima
	raw_id_fields = ()
	verbose_name = 'Associated ProAnima person'
	verbose_name_plural = 'Associated ProAnima people'
	extra = 1
	# exclude = ['role']

	

class AssocFactoidPossession(mymodels.TimeStampedHiddenModel):
	"""(used to be called 'Factoidpossession')"""
	factoidpos = models.ForeignKey('Factoid')
	possession_old = models.ForeignKey('PossessionOld', verbose_name="possessions - old classification",)
	possession = models.ForeignKey('Possession', null=True, blank=True, verbose_name="possessions - new temp classification",) # shall we keep this as the default one?
	poss_alms = models.ForeignKey('Poss_Alms', null=True, blank=True, verbose_name="alms",)
	poss_unfree_persons = models.ForeignKey('Poss_Unfree_persons', null=True, blank=True, verbose_name="unfree persons",)
	poss_revenues_silver = models.ForeignKey('Poss_Revenues_silver', null=True, blank=True, verbose_name="revenues in silver",)
	poss_revenues_kind = models.ForeignKey('Poss_Revenues_kind', null=True, blank=True, verbose_name="revenues in kind",)
	poss_general = models.ForeignKey('Poss_General', null=True, blank=True, verbose_name="possessions in general",)
	poss_office = models.ForeignKey('Poss_Office', null=True, blank=True, verbose_name="office",)
	poss_objects = models.ForeignKey('Poss_Objects', null=True, blank=True, verbose_name="objects",)
	poss_lands = models.ForeignKey('Poss_Lands', null=True, blank=True, verbose_name="lands",)
	privileges = models.ForeignKey('Privileges', null=True, blank=True, verbose_name="privileges",)
	originaltext = models.TextField(null=True, blank=True, verbose_name="original text",)
	# orderno = models.IntegerField(null=True, blank=True, verbose_name="order no",)

	class Admin(admin.ModelAdmin):
		list_display = ()
		search_fields = ()
	class Meta:
		pass
	def __unicode__(self):
		return "%s %s" % ("id:", self.id)


## inline definition
class Assoc_FactPossessionInline(admin.StackedInline):
	model = AssocFactoidPossession
	raw_id_fields = ()
	verbose_name = 'Associated Possession'
	verbose_name_plural = 'Associated Possessions'
	extra = 1
	fieldsets = [
		('',	
			{'fields':	
				['possession_old', 'possession', ('poss_alms', 'poss_unfree_persons', 
				'poss_revenues_silver', 'poss_revenues_kind', 'poss_general', 'poss_office', 
				'poss_objects', 'poss_lands', 'privileges'), 'originaltext'
				 ],	 
			'classes': ['wide']

				}),

	]



class AssocFactoidPoss_alms(mymodels.TimeStampedHiddenModel):
	"""(used to be called 'Factoidpossession')"""
	factoidpos = models.ForeignKey('Factoid')
	poss_alms = models.ForeignKey('Poss_Alms',blank=True, verbose_name="alms",)
	originaltext = models.CharField(max_length=765, null=True, blank=True, verbose_name="original text",)	
	def __unicode__(self):
		return "%s %s" % ("id:", self.id)
		
## inline definition
class AssocFactoidPoss_almsInline(admin.TabularInline):
	model = AssocFactoidPoss_alms
	raw_id_fields = ()
	verbose_name = 'Associated Alms (possessions)'
	# verbose_name_plural = 'Associated Possessions'
	extra = 1




# 
# class AssocFactoidPoss_alms(mymodels.TimeStampedHiddenModel):
# 	"""(used to be called 'Factoidpossession')"""
# 	factoidpos = models.ForeignKey('Factoid')
# 	possession_old = models.ForeignKey('PossessionOld', verbose_name="possessions - old classification",)
# 	possession = models.ForeignKey('Possession', null=True, blank=True, verbose_name="possessions - new temp classification",) # shall we keep this as the default one?
# 	poss_alms = models.ForeignKey('Poss_Alms',blank=True, verbose_name="alms",)
# 	poss_unfree_persons = models.ForeignKey('Poss_Unfree_persons', null=True, blank=True, verbose_name="unfree persons",)
# 	poss_revenues_silver = models.ForeignKey('Poss_Revenues_silver', null=True, blank=True, verbose_name="revenues in silver",)
# 	poss_revenues_kind = models.ForeignKey('Poss_Revenues_kind', null=True, blank=True, verbose_name="revenues in kind",)
# 	poss_general = models.ForeignKey('Poss_General', null=True, blank=True, verbose_name="possessions in general",)
# 	poss_office = models.ForeignKey('Poss_Office', null=True, blank=True, verbose_name="office",)
# 	poss_objects = models.ForeignKey('Poss_Objects', null=True, blank=True, verbose_name="objects",)
# 	poss_lands = models.ForeignKey('Poss_Lands', null=True, blank=True, verbose_name="lands",)
# 	privileges = models.ForeignKey('Privileges', null=True, blank=True, verbose_name="privileges",)
# 	originaltext = models.CharField(max_length=765, null=True, blank=True, verbose_name="original text",)
# 	# orderno = models.IntegerField(null=True, blank=True, verbose_name="order no",)
# 
# 	def __unicode__(self):
# 		return "%s %s" % ("id:", self.id)
# 
# ## inline definition
# class AssocFactoidPoss_almsInline(admin.TabularInline):
# 	model = AssocFactoidPoss_alms
# 	raw_id_fields = ()
# 	verbose_name = 'Associated Alms (possessions)'
# 	# verbose_name_plural = 'Associated Possessions'
# 	extra = 1








# ================================
################ FACTOIDS
# ================================




class Factoid(mymodels.PomsModel):
	#factoidkey = models.IntegerField()
	#factoidtypekey = models.IntegerField()	 --> not needed cause I have subclasses now
	sourcekey = models.ForeignKey('Source', verbose_name="Charter")
	people = models.ManyToManyField(Person, through='AssocFactoidPerson', related_name='factoids', 
			verbose_name="associated people",)
	# I put them here even though they're used only by specific Factoids!
	witnesses = models.ManyToManyField(Person, through='AssocFactoidWitness', related_name='factoidswitness', 
			verbose_name="witnesses",)
	possessions = models.ManyToManyField(PossessionOld, through='AssocFactoidPossession', 
		verbose_name="possessions",)			
	proanimapeople = models.ManyToManyField(Person, through=AssocFactoidProanima, 
		verbose_name="pro anima people",)
		
	shortdesc = models.CharField(max_length=765, null=True, blank=True, verbose_name="short description",)
	probabledate = models.CharField(max_length=765, null=True, blank=True, verbose_name="probable date",)
	firmdate = models.CharField(max_length=765, null=True, blank=True, verbose_name="firm date",)
	datingnotes = models.TextField(null=True, blank=True, verbose_name="dating notes",)
	notes = models.TextField(null=True, blank=True, verbose_name="notes",)
	# problems should go into the 'internal notes' field...
	problems = models.TextField(null=True, blank=True, verbose_name="problems",)
	# UNUSED
	sourceref = models.CharField(max_length=300, null=True, blank=True, 
		verbose_name="source reference (unused for now)",)
		
	#alkey = models.IntegerField() --> this is the 'magic' field we're going to explode into subclasses info
	@models.permalink
	def get_absolute_url(self):
		return ('factoid_detail', [str(self.id)])
	
	def get_right_subclass(self):
		# once you get a factois instance, it's useful to know quickly what subclass it is...
		try:
			sbcls = ["possession", self.factpossession]
		except:
			try:
				sbcls = ["relationship" , self.factrelationship]
			except:
				try:
					sbcls = ["title/occupation" , self.facttitle]
				except:
					try:
						sbcls = ["transaction" , self.facttransaction]
					except:
						sbcls = None
		return sbcls
	get_right_subclass.allow_tags = True				 

	class Meta:
		pass
	def __unicode__(self):
	  return self.shortdesc
	




class FactTitle(Factoid):
	"""(in poms-linnet this used to be called 'Title')"""
	#factoidkey = models.IntegerField()	 --> not needed anymore, as it's a subclass
	#  there must be a title
	titletypekey =	models.ForeignKey('TitleType', verbose_name="title type",)
	#these two are booleans, but's there are some strange '-1' in the db.. maybe it'll break
	bygraceofgod =	models.BooleanField(default=False,	blank=True, verbose_name="by grace of God",)
	byanotherdivineinvocation = models.BooleanField(default=False, blank=True, verbose_name="by another divine invocation",)	

	class Admin(AutocompleteModelAdmin):
		related_search_fields = { 

				'sourcekey': ('source_tradid',),
		}
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			obj.save()
		list_display = ('id', 'sourcekey', 'titletypekey', 'shortdesc',
					'editedrecord', 'review','updated_by', 'updated_at',)
		# filter_horizontal = ('location',) 
		# radio_fields = {"ltbrole": admin.VERTICAL}
		inlines = (AssocPersonInline, )
		# raw_id_fields = ('sourcekey', )
		list_filter = ['updated_at', 'updated_by', 'editedrecord', 'review', ]
		search_fields = ['shortdesc']
		fieldsets = [
			('Administration',	
				{'fields':	
					['editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'), 
					  ('updated_at', 'updated_by')
					 ],	 
				'classes': ['collapse']
				}),
			('Source',			
				{'fields':	
					['sourcekey', ]
					}),
			('Description',			
				{'fields':	
					[ 'titletypekey', 'shortdesc', 'bygraceofgod', 'byanotherdivineinvocation','notes'	]
					}),
			('Dates',			
				{'fields':	
					[ 'firmdate', 'probabledate','datingnotes', ]
					}),
	
		]
	def get_admin_url(self):
		return "/%sadmin/pomsapp/facttitle/%s" % (django_settings.URL_PREFIX, self.id)		
	get_admin_url.allow_tags = True
	def get_databrowse_url(self):
		return "/%sdatabrowse/pomsapp/facttitle/objects/%s" % (django_settings.URL_PREFIX, self.id)		
	get_databrowse_url.allow_tags = True
	class Meta:
		verbose_name_plural="Factoid Title/Occupation"
	def __unicode__(self):
		return "%s %s %s" % ("id:", self.id, self.shortdesc)
	table_order = 11


class FactRelationship(Factoid):
	"""(FactRelationship description)"""
	relationship = models.ForeignKey(Relationshiptype, null=True, blank=True, verbose_name="relationship",)

	def get_admin_url(self):
		return "/%sadmin/pomsapp/factrelationship/%s" % (django_settings.URL_PREFIX, self.id)		
	get_admin_url.allow_tags = True
	def get_databrowse_url(self):
		return "/%sdatabrowse/pomsapp/factrelationship/objects/%s" % (django_settings.URL_PREFIX, self.id)		
	get_databrowse_url.allow_tags = True
	
	# class Admin(admin.ModelAdmin):
	class Admin(AutocompleteModelAdmin):
		related_search_fields = { 

				'sourcekey': ('source_tradid',),
		}
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			obj.save()	
			
		list_display = ('id', 'sourcekey', 'relationship', 'shortdesc',
					'editedrecord', 'review','updated_by', 'updated_at',)
		# filter_horizontal = ('location',) 
		# radio_fields = {"ltbrole": admin.VERTICAL}
		# raw_id_fields = ('sourcekey', )
		inlines = (AssocPersonInline, )
		list_filter = ['updated_at', 'updated_by', 'editedrecord', 'review', ]
		search_fields = ['shortdesc']
		fieldsets = [
			('Administration',	
				{'fields':	
					['editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'), 
					  ('updated_at', 'updated_by')
					 ],	 
				'classes': ['collapse']
				}),
			('Source',			
				{'fields':	
					['sourcekey', ]
					}),
			('Description',			
				{'fields':	
					[ 'relationship', 'shortdesc', 'notes'	]
					}),
			('Dates',			
				{'fields':	
					[ 'firmdate', 'probabledate','datingnotes', ]
					}),
	
		]
	class Meta:
		verbose_name_plural="FactoidRelationship"
	def __unicode__(self):
		return "id[%s], from source [%s], desc: %s" % (self.id, self.sourcekey, self.shortdesc)
	table_order = 12




class FactPossession(Factoid):
	"""(FactPossession description)"""
	# the possession relation is in Factoid
	
	# add a method for showing possessions in a list

	def get_admin_url(self):
		return "/%sadmin/pomsapp/factpossession/%s" % (django_settings.URL_PREFIX, self.id)		
	get_admin_url.allow_tags = True
	def get_databrowse_url(self):
		return "/%sdatabrowse/pomsapp/factpossession/objects/%s" % (django_settings.URL_PREFIX, self.id)		
	get_databrowse_url.allow_tags = True
	
	class Admin(AutocompleteModelAdmin):
		related_search_fields = { 

				'sourcekey': ('source_tradid',),
		}
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			obj.save()
		list_display = ('id', 'sourcekey', 'shortdesc',
					'editedrecord', 'review','updated_by', 'updated_at',)
		# filter_horizontal = ('location',) 
		# radio_fields = {"ltbrole": admin.VERTICAL}
		# raw_id_fields = ('sourcekey', )
		inlines = (AssocPersonInline, Assoc_FactPossessionInline)
		list_filter = ['updated_at', 'updated_by', 'editedrecord', 'review', ]
		search_fields = ['shortdesc']
		fieldsets = [
			('Administration',	
				{'fields':	
					['editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'), 
					  ('updated_at', 'updated_by')
					 ],	 
				'classes': ['collapse']
				}),
			('Source',			
				{'fields':	
					['sourcekey', ]
					}),
			('Description',			
				{'fields':	
					[ 'shortdesc', 'notes'	]
					}),
			('Dates',			
				{'fields':	
					[ 'firmdate', 'probabledate','datingnotes', ]
					}),
	
		]
	class Meta:
		verbose_name_plural="FactoidPossession"
	def __unicode__(self):
		return "id[%s], from source [%s],  possessions[%s]" % (self.id, self.sourcekey , 
					", ".join(["%s" % p for p in self.possessions.all()])) 
	table_order = 13





class FactTransaction(Factoid):
	"""The main factoid at the moment"""
	
	def get_admin_url(self):
		return "/%sadmin/pomsapp/facttransaction/%s" % (django_settings.URL_PREFIX, self.id)		
	get_admin_url.allow_tags = True
	def get_databrowse_url(self):
		return "/%sdatabrowse/pomsapp/facttransaction/objects/%s" % (django_settings.URL_PREFIX, self.id)		
	get_databrowse_url.allow_tags = True
		
	transactiontype = models.ForeignKey(Transactiontype, null=True, blank=True, verbose_name="type of transaction",)

	isprimary = models.BooleanField(default=False, verbose_name="Primary")
	isdare = models.BooleanField(default=False, verbose_name="Dare?")
	isexchange = models.BooleanField(default=False, verbose_name="Exchange")
	verbsnotspecified = models.BooleanField(default=False, verbose_name="verbs not specified?")
	conveth = models.BooleanField(default=False, verbose_name="Conveth?")
	# witnesses
	genericwitnesses = models.BooleanField(default=False, 
		verbose_name="Witnesses in original, but not copied into cartulary")
	testemeipso = models.BooleanField(default=False, verbose_name="teste me ipso")
		
	#many2many
	tenendas = models.ManyToManyField(Tenendasclauseoptions, verbose_name="tenendas", blank=True) #through='Ass_TransTenendas', 
	exemptions = models.ManyToManyField(Exemptiontype,	verbose_name="exemptions", blank=True) #through='Ass_TransExemption',
	tenendasclauseolang = models.TextField(blank=True, verbose_name="tenendas orig. languag")
	exemptionclauseolang = models.TextField(blank=True, verbose_name="exemptions orig. languag")
	renderdates = models.ManyToManyField(Renderdate,  verbose_name="render dates", blank=True) #through='Ass_TransRenderDate',
	rendernominal = models.ManyToManyField(Nominalrendertype,  verbose_name="nominal renders", blank=True) 
	sicutclauses = models.ManyToManyField(Sicutclausetype,	
		verbose_name="sicut clause or equivalent", blank=True)	

	previouschartermention = models.BooleanField(default=False, 
		verbose_name="previous mention in charter")
	previouschirographmention = models.BooleanField(default=False, 
		verbose_name="previous mention in chirograph")
	perambulation = models.BooleanField(default=False, verbose_name="perambulation")
	corroborationsealing = models.BooleanField(default=False, verbose_name="corroboration / sealing")
	# added by Matthew 17/2/09 -->	
	ismalediction = models.BooleanField(default=False, verbose_name="malediction?")
	bothaddressorsmentioned = models.BooleanField(default=False, verbose_name="both addressors mentioned")
	warrandice = models.BooleanField(default=False, verbose_name="warrandice")

	# new many2many 5 Jun (translation of 'tickboxOptions')
	legalpertinents = models.ManyToManyField(LegalPertinents,	verbose_name="additional legal pertinents", blank=True) 
	returnsmilitary = models.ManyToManyField(Returns_military,	verbose_name="returns / military", blank=True) 
	returnsrenders = models.ManyToManyField(Returns_renders, verbose_name="returns / renders", blank=True) 
	commonburdens = models.ManyToManyField(CommonBurdens,  verbose_name="common burdens", blank=True)

	spiritualbenefits = models.ManyToManyField(Proanimagenerictypes,  verbose_name="Generics",
		blank=True)


	class Admin (AutocompleteModelAdmin):
		related_search_fields = { 

				'sourcekey': ('source_tradid',),
		}
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			obj.save()
		list_display = ('id', 'sourcekey', 'shortdesc',
					'editedrecord', 'review','updated_by', 'updated_at',)
		filter_horizontal = ('sicutclauses', 'renderdates', 'rendernominal', 'tenendas', 'spiritualbenefits', 'exemptions',
								'legalpertinents', 'returnsmilitary', 'returnsrenders', 'commonburdens')
		# radio_fields = {"ltbrole": admin.VERTICAL}
		# raw_id_fields = ('sourcekey', )
		inlines = (AssocPersonInline, AssocWitnessInline, AssocProanimaInline)
		list_filter = ['updated_at', 'updated_by', 'editedrecord', 'review', ]
		search_fields = ['shortdesc']
		fieldsets = [
			('Administration',	
				{'fields':	
					['editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'), 
					  ('updated_at', 'updated_by')
					 ],	 
				'classes': ['collapse']
				}),
			('Source and transaction type',			
				{'fields':	
					['sourcekey', 'transactiontype', ('isprimary', 'isdare', 'verbsnotspecified', 
						'isexchange', 'conveth') ]
					}),
			('Description',			
				{'fields':	
					[ 'shortdesc', 'notes'	]
					}),
			('Dates',			
				{'fields':	
					[ 'firmdate', 'probabledate','datingnotes', ]
					}),
			('Clauses: tenendas and exemption',			
				{'fields':	
					['tenendas', 'tenendasclauseolang', 'exemptions', 'exemptionclauseolang', 
					], 
				'classes': ['collapse']
					}),
			('Clauses: renders',			
				{'fields':	
					['renderdates', 'rendernominal', 
					], 
				'classes': ['collapse']
					}),
			('Clauses: sicut clause, add. legal pertinents, returns/renders and common burdens',			
				{'fields':	
					['sicutclauses',  'legalpertinents', 'returnsmilitary', 'returnsrenders', 'commonburdens',
					], 
				'classes': ['collapse']
					}),
			('Clauses: other tickboxes',			
				{'fields':	
					[ ('previouschartermention', 'previouschirographmention'), 
					 'perambulation', 'ismalediction', 'corroborationsealing', 'bothaddressorsmentioned',
					'warrandice'
					], 
				'classes': ['collapse']
					}),
			('Spiritual benefits:',			
				{'fields':	
					['spiritualbenefits',	
					], 
				'classes': ['collapse']
					}),
			('Witnesses',			
				{'fields':	
					['genericwitnesses', 'testemeipso', ]
					}),
	
		]	

	class Meta:
		verbose_name_plural="FactoidTransaction"
	def __unicode__(self):
		return "id[%s], from source [%s] " % (self.id, self.sourcekey)
		
	table_order = 15



	# typical admin for FACTOIDS
	############################
	# class Admin(admin.ModelAdmin):
	#	def save_model(self, request, obj, form, change):
	#		"""adds the user information when the rec is saved"""
	#		if getattr(obj, 'created_by', None) is None:
	#			  obj.created_by = request.user
	#		obj.updated_by = request.user
	#		obj.save()
	#	list_display = ('sourcekey', 'occupation', 'shortdesc',
	#				'editedrecord', 'review','updated_by', 'updated_at',)
	#	# filter_horizontal = ('location',) 
	#	# radio_fields = {"ltbrole": admin.VERTICAL}
	#	inlines = (AssocPersonInline, )
	#	list_filter = ['updated_at', 'updated_by', 'editedrecord', 'review', ]
	#	search_fields = ['id']
	#	fieldsets = [
	#		('Administration',	
	#			{'fields':	
	#				['editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'), 
	#				  ('updated_at', 'updated_by')
	#				 ],	 
	#			'classes': ['collapse']
	#			}),
	#		('Source',			
	#			{'fields':	
	#				['sourcekey', ]
	#				}),
	#		('Description',			
	#			{'fields':	
	#				[ 'occupation', 'shortdesc', 'notes'	]
	#				}),
	#		('Dates',			
	#			{'fields':	
	#				[ 'firmdate', 'probabledate','datingnotes', ]
	#				}),
	# 
	#	]



# 
# 
# class AssocFactoidPossessionNew(mymodels.TimeStampedHiddenModel):
#	"""(used to be called 'Factoidpossession')"""
#	test = models.ForeignKey('Test')
#	possession = models.ForeignKey('PossessionNew')
#	originaltext = models.TextField(null=True, blank=True, verbose_name="original text",)
#	# orderno = models.IntegerField(null=True, blank=True, verbose_name="order no",)
# 
#	class Admin(admin.ModelAdmin):
#		list_display = ()
#		search_fields = ()
#	class Meta:
#		pass
#	def __unicode__(self):
#		return "%s %s" % ("id:", self.id)
# 
# 
# ## inline definition
# class Assoc_FactPossessionInline2(admin.StackedInline):
#	model = AssocFactoidPossessionNew
#	raw_id_fields = ('possession',)
#	verbose_name = 'Associated Possession'
#	verbose_name_plural = 'Associated Possessions'
#	extra = 1
# 
# 
# class Test(mymodels.PomsModel):
#	#factoidkey = models.IntegerField()
#	#factoidtypekey = models.IntegerField()	 --> not needed cause I have subclasses now
#	sourcekey = models.ForeignKey('Charter', verbose_name="Charter")
#	possessions = models.ManyToManyField(PossessionNew, through='AssocFactoidPossessionNew', 
#		verbose_name="possessions",)
#	class Admin(admin.ModelAdmin):
#		def save_model(self, request, obj, form, change):
#			"""adds the user information when the rec is saved"""
#			if getattr(obj, 'created_by', None) is None:
#				  obj.created_by = request.user
#			obj.updated_by = request.user
#			obj.save()
#		inlines = (Assoc_FactPossessionInline2,)
# 




