"""Haystack search indexes to replace DJFacet"""
from haystack import indexes

import pomsapp.models as poms_models

"""
Replacing the result types with four indexes:

#	label = interface name / uniquename = internal name / infospace: a Model or a QuerySet instance
result_types = [{'label': 'Factoids',
                 'uniquename': 'factoid',
                 'infospace': Factoid},

                {'label': 'Sources',
                 'uniquename': 'source',  # at the moment the name can't be changed cause the js uses iT!
                 'infospace': Source},

                {'label': 'People and Institutions',
                 'uniquename': 'people',
                 'infospace': Person,
                 'isdefault': True	},

                    {	'label' : 'Places',
                         'uniquename' : 'place',
                         'infospace' : Place	},
                    ]
"""


class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    """

    """
    text = indexes.CharField(document=True, use_template=True)
    person_id = indexes.IntegerField(model_attr='id')
    surname = indexes.CharField(model_attr='helper_searchbigsur',
                                faceted=True,
                                null=True)
    forename = indexes.CharField(model_attr='forename',
                                 faceted=True,
                                 null=True)
    gender = indexes.CharField(model_attr='genderkey__name',
                               faceted=True,
                               null=True)
    # todo institutions are also people, not sure this is right
    institutions = indexes.MultiValueField(model_attr='id',
                                           faceted=True,
                                           null=True)
    titles = indexes.MultiValueField(
        model_attr='factoids__facttitle__titletypekey__name',
        faceted=True,
        null=True
    )
    medievalgaelicforename = indexes.CharField(
        model_attr='medievalgaelicforename__name',
        faceted=True,
        null=True)
    personstartdate = indexes.CharField(
        model_attr='floruitstartyr',
        faceted=True,
        null=True)
    persondaterange = indexes.CharField(
        model_attr='helper_daterange',
        faceted=True,
        null=True)
    documenttype = indexes.MultiValueField(
        model_attr='factoids__sourcekey__charter__chartertypekey__name',
        faceted=True,
        null=True
    )
    documentcategory = indexes.MultiValueField(
        model_attr='factoids__sourcekey__charter__hammondnumber',
        faceted=True,
        null=True)
    grantorcategory = indexes.MultiValueField(
        model_attr='factoids__sourcekey__charter__grantor_category__name',
        faceted=True,
        null=True
    )
    placedatemodern = indexes.MultiValueField(
        model_attr='factoids__sourcekey__charter__placedatemodern',
        faceted=True,
        null=True
    )
    language = indexes.CharField(
        model_attr='factoids__sourcekey__charter__language__name',
        faceted=True,
        null=True)
    sourcesfeatures = indexes.MultiValueField(
        model_attr='factoids__sourcekey__charter__helper_tickboxes__name',
        faceted=True,
        null=True
    )
    sourcesstartdate = indexes.IntegerField(
        model_attr='factoids__sourcekey__from_year',
        faceted=True,
    )
    sourcesdaterange = indexes.CharField(
        model_attr='factoids__sourcekey__helper_daterange',
        faceted=True,
        null=True
    )
    relationshiptypes = indexes.MultiValueField(
        model_attr='factoids__factrelationship__relationship__name',
        faceted=True,
        null=True
    )
    roles = indexes.MultiValueField(
        model_attr='assochelperperson__role__name',
        faceted=True,
        null=True
    )
    spiritualbenefits = indexes.MultiValueField(
        model_attr='factoids__facttransaction__spiritualbenefits__name',
        faceted=True,
        null=True
    )
    factrelstartdate = indexes.IntegerField(
        model_attr='factoids__factrelationship__from_year',
        faceted=True,
    )
    factreldaterange = indexes.CharField(
        model_attr='factoids__factrelationship__helper_daterange',
        faceted=True,
        null=True
    )
    transactiontypes = indexes.MultiValueField(
        model_attr='factoids__facttransaction__transactiontype__name',
        faceted=True,
        null=True
    )
    transfeatures = indexes.MultiValueField(
        model_attr='factoids__facttransaction__helper_tickboxes__name',
        faceted=True,
        null=True
    )
    possoffice = indexes.MultiValueField(
        model_attr='factoids__poss_office__name',
        faceted=True,
        null=True
    )
    possunfreepersons = indexes.MultiValueField(
        model_attr='factoids__poss_unfreep__name',
        faceted=True,
        null=True
    )
    posslands = indexes.MultiValueField(
        model_attr='factoids__poss_lands__name',
        faceted=True,
        null=True
    )
    possrevkind = indexes.MultiValueField(
        model_attr='factoids__poss_revkind__name',
        faceted=True,
        null=True
    )
    possrevsilver = indexes.MultiValueField(
        model_attr='factoids__poss_revsilver__name',
        faceted=True,
        null=True
    )
    privileges = indexes.MultiValueField(
        model_attr='factoids__poss_privileges__name',
        faceted=True,
        null=True
    )
    # Not sure this is relevant ->
    #  'querypath' : 'helper_places__name',	 #if using the explosded version..
    places = indexes.MultiValueField(
        model_attr='relatedplace__name',
        faceted=True,
        null=True
    )
    facttrastartdate = indexes.IntegerField(
        model_attr='factoids__facttransaction__from_year',
        faceted=True
    )
    factposstartdate = indexes.IntegerField(
        model_attr='factoids__factpossession__from_year',
        faceted=True
    )
    facttradaterange = indexes.CharField(
        model_attr='factoids__facttransaction__helper_daterange',
        faceted=True
    )
    factposdaterange = indexes.CharField(
        model_attr='factoids__factpossession__helper_daterange',
        faceted=True
    )
    tenendasoptions = indexes.CharField(
        model_attr='factoids__facttransaction__tenendas__name',
        faceted=True
    )
    exemptionoptions = indexes.CharField(
        model_attr='factoids__facttransaction__exemptions__name',
        faceted=True
    )
    sicutclause = indexes.CharField(
        model_attr='factoids__facttransaction__sicutclauses__name',
        faceted=True
    )
    returnsrenders = indexes.CharField(
        model_attr='factoids__facttransaction__returnsrenders__name',
        faceted=True
    )
    nominalrenders = indexes.CharField(
        model_attr='factoids__facttransaction__rendernominal__name',
        faceted=True
    )
    renderdates = indexes.MultiValueField(
        model_attr='factoids__facttransaction__renderdates__name',
        faceted=True,
        null=True
    )
    returnsmilitary = indexes.CharField(
        model_attr='factoids__facttransaction__returnsmilitary__name',
        faceted=True
    )
    commonburdens = indexes.MultiValueField(
        model_attr='factoids__facttransaction__commonburdens__name',
        faceted=True,
        null=True
    )
    legalpertinents = indexes.MultiValueField(
        model_attr='factoids__facttransaction__legalpertinents__name',
        faceted=True,
        null=True
    )


    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def get_model(self):
        return poms_models.Person
