'''
Allows for a quick startup loading commonly used classes, installed apps, and console utils.

To use: After manage.py shell, enter from project.utils.shellstartup import *
'''

from django.conf import settings
from django.db import connection, models
from time import strftime



# Load each installed app and put models into the global namespace.
for app in models.get_apps():
	exec("from %s import *" % app.__name__)
		
def last_query():
	"Show the last query performed."
	return connection.queries[-1]


def describe_instance(i):
	"""utility that shows all the contents of an object - TO BE TESTED MORE.. for example it doesn't work 
		with a string, although it is an object.."""
	if isinstance(i, object):
		print 'Type : ', type(i), "\n++++++++"
		try:
			for k in i.__dict__.keys():
				print k, ':', i.__dict__[k]
		except:
			print "ERROR: \'", i, "\' does not have the __dict__ attribute.. is it an object?"
				


#===================================================
# Add commonly used modules, classes, functions here
#===================================================
from django import forms
import os
from datetime import datetime
from django.db.models import Avg, Max, Min, Count, Q
import operator, time


#  from utils.shellstartup import *

#### stuff for testing the facetedBrowser

from facetedbrowser.facetviews import *


#  init vars
loaded_facet_groups = []
facets_for_template = []

# load facet specs 
# 1: create groups from SPECS.facet_groups	
# 2: load facets into groups using SPECS.facetslist
for x in reversed(sorted(SPECS.facet_groups, key=lambda (k): k['position'])):
	if x['default']:
		loaded_facet_groups.append(FacetsGroup(x['uniquename'], x['label'], x['position'])) 
for g in loaded_facet_groups:
	g.buildfacets_fromspecs(SPECS.facetslist)
# 3: load result types
result_types = SPECS.result_types 

# initialize the faceted manager
fm = FacetedManager(loaded_facet_groups, result_types)

logs = """ 
COMMANDS LOADED:::
===================
#  init vars
loaded_facet_groups = []
facets_for_template = []

# load facet specs 
# 1: create groups from SPECS.facet_groups	
# 2: load facets into groups using SPECS.facetslist
for x in reversed(sorted(SPECS.facet_groups, key=lambda (k): k['position'])):
	if x['default']:
		loaded_facet_groups.append(FacetsGroup(x['uniquename'], x['label'], x['position'])) 
for g in loaded_facet_groups:
	g.buildfacets_fromspecs(SPECS.facetslist)
# 3: load result types
result_types = SPECS.result_types 

# initialize the faceted manager
fm = FacetedManager(loaded_facet_groups, result_types)


fm.init_resulttypes_activeIDs()	
fm.cacheResultTypes()
===================
"""

# print logs

 
if True:
	fm.init_resulttypes_activeIDs()	 #cache this in memory first.



if False:
	fm.cacheResultTypes()



def cacheAllFacets(fm, result_types, SLICING = None):
	for facet in fm.get_all_facets():
		for r in result_types:
			v = fm._cacheOneFacetValue(facet, resulttype=r, ENFORCE=True, SLICING = SLICING) # ENFORCE = True
			if v:
				print "\n\nzzzzzzzzzzzzzzzzzz sleeping 30 seconds zzzzzzzzzzzzzzzzzzzzzzzz\n\n"
				time.sleep(30)
			
			
# this is caching only one facet, for all result types, and no QueryArgs
def cacheOneFacetAllResults(facet_name, fm, ENFORCE=False, SLICING = None):
	facet = fm.get_facet_from_name(facet_name)
	for r in result_types:
		v = fm._cacheOneFacetValue(facet, resulttype=r, ENFORCE=ENFORCE, SLICING = SLICING) #  ENFORCE = True, DELETE =True
		if v:
			print "\n\nzzzzzzzzzzzzzzzzzz sleeping 30 seconds zzzzzzzzzzzzzzzzzzzzzzzz\n\n"
			time.sleep(30)
		

def cacheOneFacetOneResult(facet_name, result_name, fm, ENFORCE=False, SLICING = None):
	facet = fm.get_facet_from_name(facet_name)
	r1 = fm.get_resulttype_from_name(result_name)
	v = fm._cacheOneFacetValue(facet, resulttype=r1, ENFORCE=ENFORCE, SLICING = SLICING) # Queryargs, ENFORCE = True, DELETE =True
	if v:
		print "\n\nzzzzzzzzzzzzzzzzzz DONE zzzzzzzzzzzzzzzzzzzzzzzz\n\n"



# technique for caching facets-values with lots of values (that generate a mem-error!)
def cache_longestFacets(fm):
	for f in ['surname', 'forename']:
		for t in [(0, 2000), (2000, 4000), (4000, 6000)]:
			try:
				cacheOneFacetOneResult(f, 'factoid', fm, ENFORCE=True, SLICING = t)
				cacheOneFacetOneResult(f, 'source', fm, ENFORCE=True, SLICING = t)
				cacheOneFacetOneResult(f, 'people', fm, ENFORCE=True, SLICING = t)
			except:
				break ## in case the slicing fails...


def cacheAllFacets_butLongestOnes(fm):
	for facet in fm.get_all_facets():
		if facet.uniquename == 'surname' or facet.uniquename == 'forename':
			continue
		else:
			cacheOneFacetAllResults(facet.uniquename, fm, ENFORCE=True)





# deleteCachedFacet(fm, 'forename', 'source')
# deleteCachedFacet(fm, 'forename', 'people')
# deleteCachedFacet(fm, 'forename', 'factoid')

# QueryArgs: list of [active_facetsGroup, active_facet, facetvalue]
# set queryargs to 'only_with_queryargs' to delete only stuff with queryargs
def deleteCachedFacet(fm, facet_name, result_name, queryargs = None):
	fm._emptyCacheForFacetQuery(fm.get_facet_from_name(facet_name), fm.get_resulttype_from_name(result_name), queryargs)


# set queryargs to 'only_with_queryargs' to delete only stuff with queryargs
def deleteAllCachedFacets(fm, queryargs = None):
	for facet in fm.get_all_facets():
		for r in result_types:
			fm._emptyCacheForFacetQuery(facet, r, queryargs)
	pass





	# HOW TO GET TO THE LATEST SAVED CACHED QUERY..
	# 
	# >>> CachedQueryArgs.objects.get(facets='medievalga', values='')
	# <CachedQueryArgs: CachedQueryArgs object>
	# >>> c = _
	# >>> c.id
	# 37L
	# >>> CachedFacetQuery.objects.get(facet='forename', resulttype='factoid', queryargs=c)
	# <CachedFacetQuery: CachedFacetQuery object>
	# >>> x = CachedFacetQuery.objects.get(facet='forename', resulttype='factoid', queryargs=c)
	# >>> x.delete()
	# >>> x = CachedFacetQuery.objects.get(facet='surname', resulttype='factoid', queryargs=c)
	# >>> x.delete()
	


				

#
# run what is needed: 
#










##################
#  Thu Sep  2 19:08:36 BST 2010
#  CACHING 2ND LEVEL: first attempt: 
#
##################



# finds all cached values that still have more than X results; uses them to compose a query, and re-calculates all
# values-count in this new context...
def cache_secondLevel_objects(n, fmanager, test = False):
	l = CachedFacetValue.objects.filter(count__gt=n).order_by('-count')
	totcount = len(l)
	count = 0
	if test:
		l = l[:1]   # TESTING WITH ONE VALUE
	for cachedValue in l:  
		count += 1 	
		facetvalue_name = cachedValue.facetvalue
		cachedQuery = cachedValue.cachedfacetquery_set.all()[0]
		facet_name = cachedQuery.facet
		resulttype_name =  cachedQuery.resulttype

		print("\n$$$$$$$$$$$$\nFIND_VALUES_WITH_COUNT_MORETHAN:\n [facetvalue= *%s*] [facet = *%s*][restype = *%s*] with count *%d* ..... caching...\nvalue %d of %d\n$$$$$$$$$$$$\n" % (facetvalue_name, 
									facet_name, resulttype_name, cachedValue.count, count, totcount))
		fmanager.empty_queryargs()
		
		# now get the objects and compose the QueryArg list
		active_facet = fmanager.get_facet_from_name(facet_name)
		active_resulttype = fmanager.get_resulttype_from_name(resulttype_name)
		active_facetvalue = active_facet.get_facetvalue_from_name(facetvalue_name)
		active_facetsGroup = None	#### facetGroup is not used... 
		
		# QueryArgs: list of [active_facetsGroup, active_facet, facetvalue]
		fmanager.add_queryarg(active_facetsGroup, active_facet, active_facetvalue) 
	
		# we changed the state of fmanager, so the query will cache other stuff!
		
		# we cache the count for all facets, using that specific resultType where the count is very high.
		for fac in fmanager.get_all_facets():
			print "\n[%s]\n" % strftime("%Y-%m-%d %H:%M:%S")
			if fac.uniquename == 'surname' or fac.uniquename == 'forename' or fac.uniquename == 'titles':
				for t in [(0, 1000), (1000, 2000), (2000, 3000), (3000, 4000), (4000, 5000)]:
					try:
						cacheOneFacetOneResult(fac.uniquename, resulttype_name, fmanager, SLICING = t)  #ENFORCE=True,
					except:
						break ## in case the slicing fails...
			else:
				cacheOneFacetOneResult(fac.uniquename, resulttype_name, fmanager,)  #ENFORCE=True
			print "\n[%s]\nzzzzzzzzzzzzzzzzzz waiting 1 second zzzzzzzzzzzzzzzzzzzzzzzz\n" % strftime("%Y-%m-%d %H:%M:%S")
			time.sleep(1)

			
			# v = fmanager._cacheOneFacetValue(fac, active_resulttype)  #ENFORCE=True
			# if v:

		
# cache_secondLevel_objects(500, fm)		






