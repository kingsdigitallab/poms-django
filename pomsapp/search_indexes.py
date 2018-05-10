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


class PomsFields(indexes.SearchIndex):
    """ Base object with fields common to all result types
    """
    #
    object_id = indexes.IntegerField(model_attr='id')
    text = indexes.CharField(document=True, use_template=True)
    surname = indexes.MultiValueField(
        faceted=True,
        null=True)
    forename = indexes.MultiValueField(
        faceted=True,
        null=True)
    gender = indexes.MultiValueField(
        faceted=True,
        null=True)
    # todo institutions are also people, not sure this is right
    institutions = indexes.MultiValueField(model_attr='id',
                                           faceted=True,
                                           null=True)
    titles = indexes.MultiValueField(
        faceted=True,
        null=True
    )
    medievalgaelicforename = indexes.MultiValueField(
        faceted=True,
        null=True)
    startdate = indexes.IntegerField(
        faceted=True,
        null=True)
    daterange = indexes.CharField(

        faceted=True,
        null=True)
    documenttype = indexes.MultiValueField(

        faceted=True,
        null=True
    )
    documentcategory = indexes.MultiValueField(

        faceted=True,
        null=True)
    grantorcategory = indexes.MultiValueField(

        faceted=True,
        null=True
    )
    placedatemodern = indexes.MultiValueField(

        faceted=True,
        null=True
    )
    language = indexes.MultiValueField(

        faceted=True,
        null=True)
    sourcesfeatures = indexes.MultiValueField(

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
        # model_attr='assoc_factoid_person__facttransaction__spiritualbenefits__name',
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
        # model_attr='assoc_factoid_person__facttransaction__transactiontype__name',
        faceted=True,
        null=True
    )
    transfeatures = indexes.MultiValueField(
        # model_attr='fassoc_factoid_person__facttransaction__helper_tickboxes__name',
        faceted=True,
        null=True
    )
    possoffice = indexes.MultiValueField(
        # model_attr='assoc_factoid_person__poss_office__name',
        faceted=True,
        null=True
    )
    possunfreepersons = indexes.MultiValueField(

        faceted=True,
        null=True
    )
    posslands = indexes.MultiValueField(

        faceted=True,
        null=True
    )
    possrevkind = indexes.MultiValueField(

        faceted=True,
        null=True
    )
    possrevsilver = indexes.MultiValueField(

        faceted=True,
        null=True
    )
    privileges = indexes.MultiValueField(

        faceted=True,
        null=True
    )
    # Not sure this is relevant ->
    #  'querypath' : 'helper_places__name',	 #if using the explosded version..
    places = indexes.MultiValueField(

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
    tenendasoptions = indexes.MultiValueField(
        faceted=True,
        null=True
    )

    # model_attr='assoc_factoid_person__facttransaction__exemptions__name',
    exemptionoptions = indexes.MultiValueField(
        faceted=True,
        null=True
    )
    sicutclause = indexes.MultiValueField(
        # model_attr='assoc_factoid_person__facttransaction__sicutclauses__name',
        faceted=True,
        null=True
    )
    returnsrenders = indexes.MultiValueField(
        # model_attr='assoc_factoid_person__facttransaction__returnsrenders__name',
        faceted=True,
        null=True
    )
    nominalrenders = indexes.MultiValueField(
        # model_attr='assoc_factoid_person__facttransaction__rendernominal__name',
        faceted=True
    )
    renderdates = indexes.MultiValueField(
        # model_attr='assoc_factoid_person__facttransaction__renderdates__name',
        faceted=True,
        null=True
    )
    returnsmilitary = indexes.MultiValueField(
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


class PersonIndex(PomsFields, indexes.Indexable):
    """

    """

    def prepare(self, obj):
        self.prepared_data = super(PersonIndex, self).prepare(obj)

        self.prepared_data[
            'surname'
        ] = obj.helper_searchbigsur
        self.prepared_data[
            'forename'
        ] = obj.forename
        if obj.genderkey:
            self.prepared_data[
                'gender'
            ] = obj.genderkey.name
        if obj.medievalgaelicforename:
            self.prepared_data[
                'medievalgaelicforename'
            ] = obj.medievalgaelicforename.name

        self.prepared_data[
            'startdate'] = obj.floruitstartyr
        self.prepared_data[
            'daterange'] = obj.helper_daterange

        # Get charters
        charters = poms_models.Charter.objects.filter(
            factoid__people=obj
        ).distinct()
        if charters.count() > 0:
            documenttype = list()
            documentcategory = list()
            grantor_category = list()
            placedatemodern = list()
            languages = list()
            sourcesfeatures = list()

            for c in charters:
                if c.chartertypekey:
                    documenttype.append(c.chartertypekey.name)
                documentcategory.append(c.hammondnumber)
                if c.grantor_category:
                    grantor_category.append(c.grantor_category.name)
                placedatemodern.append(c.placedatemodern)
                if c.language:
                    languages.append(c.language.name)
                if c.helper_tickboxes:
                    sourcesfeatures.append(c.helper_tickboxes.name)

            self.prepared_data['documenttype'] = [d for d in set(documenttype)]
            self.prepared_data['documentcategory'] =[d for d in set(documentcategory)]
            self.prepared_data['grantorcategory'] = [d for d in set(grantor_category)]
            self.prepared_data['placedatemodern'] = [d for d in set(placedatemodern)]
            self.prepared_data['language'] = [l for l in set(languages)]
            self.prepared_data['sourcesfeatures'] = [d for d in set(sourcesfeatures)]

        self.prepared_data['possunfreepersons'] = list(
            poms_models.Poss_Unfree_persons.objects.filter(
                factoid__people=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['posslands'] = list(
            poms_models.Poss_Lands.objects.filter(
                factoid__people=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['possrevkind'] = list(
            poms_models.Poss_Revenues_kind.objects.filter(
                factoid__people=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['possrevsilver'] = list(
            poms_models.Poss_Revenues_kind.objects.filter(
                factoid__people=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['privileges'] = list(
            poms_models.Privileges.objects.filter(
                factoid__people=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['places'] = list(
            poms_models.Place.objects.filter(
                person=obj
            ).distinct().values_list('name', flat=True)
        )

        return self.prepared_data

    # privileges = indexes.MultiValueField(
    #     model_attr='factoids__poss_privileges__name',
    #     faceted=True,
    #     null=True
    # )
    # Not sure this is relevant ->
    #  'querypath' : 'helper_places__name',	 #if using the explosded version..
    # places = indexes.MultiValueField(
    #     model_attr='relatedplace__name',
    #     faceted=True,
    #     null=True
    # )


    def prepare_roles(self, obj):
        return list(poms_models.Role.objects.filter(
            assochelperperson__person=obj
        ).distinct().values_list('name', flat=True))


    def prepare_relationshiptypes(self, obj):
        return list(poms_models.Relationshiptype.objects.filter(
            factrelationship__people=obj
        ).distinct().values_list('name', flat=True))


    def prepare_spiritualbenefits(self, obj):
        return list(poms_models.Proanimagenerictypes.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True))


    def prepare_transactiontypes(self, obj):
        return list(poms_models.Transactiontype.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True))


    def prepare_transfeatures(self, obj):
        return list(poms_models.TransTickboxes.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True)
                    )


    def prepare_possoffice(self, obj):
        return list(
            poms_models.Poss_Office.objects.filter(
                assocfactoidposs_office__factoid__people=obj
            ).distinct().values_list('name', flat=True)
        )


    def prepare_tenendasoptions(self, obj):
        return list(
            poms_models.Tenendasclauseoptions.objects.filter(
                facttransaction__people=obj
            ).distinct().values_list('name', flat=True)
        )


    def prepare_exemptionoptions(self, obj):
        return list(poms_models.Exemptiontype.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True)
                    )


    def prepare_sicutclause(self, obj):
        return list(poms_models.Sicutclausetype.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True))


    def prepare_returnsrenders(self, obj):
        return list(poms_models.Returns_renders.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True))


    def prepare_nominalrenders(self, obj):
        return list(poms_models.Nominalrendertype.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True))


    def prepare_renderdates(self, obj):
        return list(poms_models.Renderdate.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True))


    def prepare_returnsmilitary(self, obj):
        return list(poms_models.Returns_military.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True))


    def prepare_commonburdens(self, obj):
        return list(poms_models.CommonBurdens.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True))


    def prepare_legalpertinents(self, obj):
        return list(poms_models.LegalPertinents.objects.filter(
            facttransaction__people=obj
        ).distinct().values_list('name', flat=True))


    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter()


    def get_model(self):
        return poms_models.Person
