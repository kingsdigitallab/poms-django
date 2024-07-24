from poms.facetedbrowser.facetviews import *  # noqa
'''
Allows for a quick startup loading commonly used
classes, installed apps, and console utils.

To use: After manage.py shell, enter from
project.utils.shellstartup import *
'''

from django.db import connection, models

# Load each installed app and put models into the global namespace.
for app in models.get_apps():
    exec("from %s import *" % app.__name__)


def last_query():
    "Show the last query performed."
    return connection.queries[-1]


def describe_instance(i):
    """utility that shows all the contents of an object
        TO BE TESTED MORE.. for example it doesn't work
        with a string, although it is an object.."""
    if isinstance(i, object):
        print('Type : ', type(i), "\n++++++++")
        try:
            for k in i.__dict__.keys():
                print(k, ':', i.__dict__[k])
        except BaseException:
            print("ERROR: \'", i, "\' does not have the\
                __dict__ attribute.. is it an object?")


# ===================================================
# Add commonly used modules, classes, functions here
# ===================================================


#  from utils.shellstartup import *

# stuff for testing the facetedBrowser


#  init vars
loaded_facet_groups = []
facets_for_template = []

# load facet specs
# 1: create groups from SPECS.facet_groups
for x in reversed(sorted(SPECS.facet_groups, key=lambda k: k['position'])):
    if x['default']:
        loaded_facet_groups.append(
            FacetsGroup(
                x['uniquename'],
                x['label'],
                x['position']))
# 2: load facets into groups using SPECS.facetslist
for g in loaded_facet_groups:
    g.buildfacets_fromspecs(SPECS.facetslist)
# 3: load result types
result_types = SPECS.result_types

# initialize the faceted manager
f = FacetedManager(loaded_facet_groups, result_types)

# prepare data for visualization
for g in loaded_facet_groups:
    facets_for_template.append(
        (g, [
            (facet, split_list_into_two(
                facet.get_facetvalues_sample(
                    maxnumber=0))) for facet in g.facets]))


#  feedback:
print('+++ Loaded facet groups:')
for x in loaded_facet_groups:
    print(x.uniquename, x.position)

print('+++ loaded result types:')
for x in result_types:
    print(x['uniquename'], " : ", x['infospace'])


if True:
    f.init_resulttypes_activeIDs()


logs = """
COMMANDS LOADED:::
===================
for x in reversed(sorted(SPECS.facet_groups, key=lambda (k): k['position'])):
    if x['default']:
        loaded_facet_groups.append(FacetsGroup(
            x['uniquename'], x['label'], x['position']))
for g in loaded_facet_groups:
    g.buildfacets_fromspecs(SPECS.facetslist)
# 3: load result types
result_types = SPECS.result_types

# initialize the faceted manager
f = FacetedManager(loaded_facet_groups, result_types)

# prepare data for visualization
for g in loaded_facet_groups:
    facets_for_template.append((g, [(facet,
    split_list_into_two(facet.get_facetvalues_sample(
        maxnumber=0))) for facet in g.facets]))

#  feedback:
print '+++ Loaded facet groups:'
for x in loaded_facet_groups: print x.name, x.position

print '+++ loaded result types:'
for x in result_types: print x['uniquename'], " : ", x['infospace']

f.init_resulttypes_activeIDs()

# to TEST the DBcache:
>>> genderfacet = f.get_facet_from_name('gender')
>>> genderval = genderfacet.get_facetvalue_from_displayname('M')
>>> genderval2 = genderfacet.get_facetvalue_from_displayname('F')
>>> queryargs = [[None, genderfacet, genderval],
[None, genderfacet, genderval2]]
>>> cacheDB = DbCache(f, queryargs, None)
>>> cacheDB.getCachedFacetValues('source', genderfacet)
>>> cacheDB.getCachedFacetValue_fromValue(genderfacet, 'source', 'M')
>>> cacheDB.getCachedFacetValueCount_fromValue(genderfacet, 'source', 'M')


# TO TEST THE TREEs in FB:
>>> facet1 = f.get_facet_from_name('possoffice')
>>> val2 = facet1.get_facetvalue_from_name(
    'Office of Forester of Coldinghamshire')
>>> facet1.recursive_tree_forfacetvalue(val2)

>>> facet2 = f.get_facet_from_name('possunfreepersons')
>>> fv1 = facet2.get_facetvalue_from_name('3 bondmen')
>>> facet2.recursive_tree_forfacetvalue(fv1)


===================
"""

print(logs)
