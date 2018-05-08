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
        # model_attr='factoids__facttitle__titletypekey__name',
        faceted=True,
        null=True
    )
    medievalgaelicforename = indexes.CharField(
        model_attr='medievalgaelicforename__name',
        faceted=True,
        null=True)
    startdate = indexes.CharField(
        model_attr='floruitstartyr',
        faceted=True,
        null=True)
    daterange = indexes.CharField(
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
    # REMOVED
    # sourcesstartdate = indexes.IntegerField(
    #     model_attr='factoids__sourcekey__from_year',
    #     faceted=True,
    # )
    # sourcesdaterange = indexes.CharField(
    #     model_attr='factoids__sourcekey__helper_daterange',
    #     faceted=True,
    #     null=True
    # )
    relationshiptypes = indexes.MultiValueField(
        # model_attr='assoc_factoid_person__factrelationship__relationship__name',
        faceted=True,
        null=True
    )
    roles = indexes.MultiValueField(
        # model_attr='assochelperperson__role__name',
        faceted=True,
        null=True
    )
    spiritualbenefits = indexes.MultiValueField(
        #model_attr='assoc_factoid_person__facttransaction__spiritualbenefits__name',
        faceted=True,
        null=True
    )
    # REMOVED
    # factrelstartdate = indexes.IntegerField(
    #     #model_attr='assoc_factoid_person__factrelationship__from_year',
    #     faceted=True,
    #     null=True
    # )
    # factreldaterange = indexes.CharField(
    #     #model_attr='assoc_factoid_person__factrelationship__helper_daterange',
    #     faceted=True,
    #     null=True
    # )
    transactiontypes = indexes.MultiValueField(
        #model_attr='assoc_factoid_person__facttransaction__transactiontype__name',
        faceted=True,
        null=True
    )
    transfeatures = indexes.MultiValueField(
        #model_attr='fassoc_factoid_person__facttransaction__helper_tickboxes__name',
        faceted=True,
        null=True
    )
    possoffice = indexes.MultiValueField(
        #model_attr='assoc_factoid_person__poss_office__name',
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
    # REMOVED
    # facttrastartdate = indexes.IntegerField(
    #     model_attr='assoc_factoid_person__facttransaction__from_year',
    #     faceted=True,
    #     null=True
    # )
    # factposstartdate = indexes.IntegerField(
    #     #model_attr='assoc_factoid_person__factpossession__from_year',
    #     faceted=True,
    #     null=True
    # )
    # facttradaterange = indexes.CharField(
    #     #model_attr='assoc_factoid_person__facttransaction__helper_daterange',
    #     faceted=True,
    #     null=True
    # )
    # factposdaterange = indexes.CharField(
    #     #model_attr='factoids__factpossession__helper_daterange',
    #     faceted=True,
    #     null=True
    # )

    # model_attr='facttransaction__tenendas__name',
    tenendasoptions = indexes.CharField(
        faceted=True,
        null=True
    )

    # model_attr='assoc_factoid_person__facttransaction__exemptions__name',
    exemptionoptions = indexes.CharField(
        faceted=True,
        null=True
    )
    sicutclause = indexes.CharField(
        #model_attr='assoc_factoid_person__facttransaction__sicutclauses__name',
        faceted=True,
        null=True
    )
    returnsrenders = indexes.CharField(
        #model_attr='assoc_factoid_person__facttransaction__returnsrenders__name',
        faceted=True,
        null=True
    )
    nominalrenders = indexes.CharField(
        #model_attr='assoc_factoid_person__facttransaction__rendernominal__name',
        faceted=True
    )
    renderdates = indexes.MultiValueField(
       # model_attr='assoc_factoid_person__facttransaction__renderdates__name',
        faceted=True,
        null=True
    )
    returnsmilitary = indexes.CharField(
       # model_attr='assoc_factoid_person__facttransaction__returnsmilitary__name',
        faceted=True,
        null=True
    )
    commonburdens = indexes.MultiValueField(
       # model_attr='assoc_factoid_person__facttransaction__commonburdens__name',
        faceted=True,
        null=True
    )
    legalpertinents = indexes.MultiValueField(
       # model_attr='assoc_factoid_person__facttransaction__legalpertinents__name',
        faceted=True,
        null=True
    )

    def prepare_roles(self, obj):
        return poms_models.Role.objects.filter(
            assochelperperson__person=obj
        ).values_list('name', flat=True)


    def prepare_relationshiptypes(self, obj):
        return poms_models.Relationshiptype.objects.filter(
            factrelationship__people=obj
        ).values_list('name', flat=True)

    def prepare_spiritualbenefits(self, obj):
        return poms_models.Proanimagenerictypes.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_transactiontypes(self, obj):
        return poms_models.Transactiontype.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_transfeatures(self, obj):
        return poms_models.TransTickboxes.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_possoffice(self, obj):
        return poms_models.Poss_Office.objects.filter(
            assocfactoidposs_office__factoid__people=obj
        ).values_list('name', flat=True)

    def prepare_tenendasoptions(self, obj):
        return poms_models.Tenendasclauseoptions.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_exemptionoptions(self, obj):
        return poms_models.Exemptiontype.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_sicutclause(self, obj):
        return poms_models.Sicutclausetype.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_returnsrenders(self, obj):
        return poms_models.Returns_renders.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_nominalrenders(self, obj):
        return poms_models.Nominalrendertype.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_renderdates(self, obj):
        return poms_models.Renderdate.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_returnsmilitary(self, obj):
        return poms_models.Returns_military.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_commonburdens(self, obj):
        return poms_models.CommonBurdens.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)

    def prepare_legalpertinents(self, obj):
        return poms_models.LegalPertinents.objects.filter(
            facttransaction__people=obj
        ).values_list('name', flat=True)


    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(id__lt=200)

    def get_model(self):
        return poms_models.Person

