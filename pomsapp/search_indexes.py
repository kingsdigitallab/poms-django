"""Haystack search indexes to replace DJFacet"""
from django.conf import settings as settings
from django.db.models import Q
from haystack import indexes
import pomsapp.models as poms_models

# save each person/source on index to force rerunning of
# floruit/firmdate calculations


"""
Replacing the DJFacet result types with four indexes:

#   label = interface name / uniquename = internal name / infospace: a Model
or a QuerySet instance
result_types = [{'label': 'factoid__sourcekeys',
                 'uniquename': 'factoid',
                 'infospace': Factoid},

                {'label': 'Sources',
                 'uniquename': 'source',  # at the moment the name can't be
                 changed cause the js uses iT!
                 'infospace': Source},

                {'label': 'People and Institutions',
                 'uniquename': 'people',
                 'infospace': Person,
                 'isdefault': True  },

                    {   'label' : 'Places',
                         'uniquename' : 'place',
                         'infospace' : Place    },
                    ]
"""

"""
    Use this to limit how many records will be indexed in a partial index
    it's done by id rather than absolute count so <500 id may not equal
    500 records.  For testing only.
    """
PARTIAL_INDEX_MAX_ID = 500

"""
Find a string date range that date falls within
Ranges defined by Matthew Hammond as:

1093-1124
1124-1153
1153-1165
1165-1214
1214-1249
1249-1286
1286-1296
1296-1314 
'1314-29'
'1329-1371'
'1371-1406'?

"""
DATE_RANGES = [
    ['1093-1124', 1093, 1124],
    ['1124-1153', 1124, 1153],
    ['1153-1165', 1153, 1165],
    ['1165-1214', 1165, 1214],
    ['1214-1249', 1214, 1249],
    ['1249-1286', 1249, 1286],
    ['1286-1296', 1286, 1296],
    ['1296-1314', 1296, 1314],
    ['1314-1329', 1314, 1329],
    ['1329-1371', 1329, 1371],
    ['1371-1406', 1371, 1406],
    ['1371-1390', 1371, 1390],
    ['1390-1406', 1390, 1406],
]


def getDateRange(start_date, end_date=0):
    ranges = []
    if start_date:
        for range in DATE_RANGES:
            if end_date > 0:
                if ((start_date >= range[1] and start_date <= range[2])
                        or (end_date >= range[1] and end_date <= range[2])):
                    ranges.append(range[0])
            elif start_date > 0:
                if (start_date >= range[1] and start_date <= range[2]):
                    ranges.append(range[0])
    return ranges


class PomsIndex(indexes.SearchIndex):
    """ Base object with fields common to all result types  """


    object_id = indexes.IntegerField(model_attr='id')
    index_type = indexes.CharField(faceted=True, )
    text = indexes.CharField(document=True, use_template=True)
    # these are single fields used in different result types
    # so that they can be sorted

    # Person
    surname = indexes.CharField(null=True, default='')
    forename = indexes.CharField(null=True, default='')
    persondisplayname = indexes.CharField(faceted=True, null=True, default='')
    standardmedievalname = indexes.CharField(null=True, default='')
    moderngaelicname = indexes.CharField(null=True, default='')

    # Factoid
    description = indexes.CharField(faceted=True, null=True, default='')
    inferred_type = indexes.CharField(faceted=True, null=True, default='')
    source = indexes.CharField(null=True, default='')

    # source
    calendar_number = indexes.CharField(null=True, default='')
    hammondnumber = indexes.IntegerField(null=True)
    hammondnumb2 = indexes.IntegerField(null=True)
    hammondnumb3 = indexes.IntegerField(null=True)

    # place
    place_name = indexes.CharField(faceted=True, null=True, default='')
    place_parent = indexes.CharField(faceted=True, null=True, default='')

    # Extra fields for map display
    charter_id = indexes.IntegerField(null=True)
    source_tradid = indexes.CharField(null=True, default='')
    place_types = indexes.MultiValueField(
        null=True)

    surnames = indexes.MultiValueField(
        faceted=True,
        null=True)
    forenames = indexes.MultiValueField(
        faceted=True,
        null=True)
    gender = indexes.MultiValueField(
        faceted=True,
        null=True)
    # todo institutions are also people, not sure this is right
    institutions = indexes.MultiValueField(
        faceted=True,
        null=True)
    titles = indexes.MultiValueField(
        faceted=True,
        null=True
    )
    medievalgaelicforename = indexes.MultiValueField(
        faceted=True,
        null=True)

    medievalgaelicsurname = indexes.MultiValueField(
        faceted=True,
        null=True)

    moderngaelicforename = indexes.MultiValueField(
        faceted=True,
        null=True)

    # moderngaelicsurname = indexes.MultiValueField(
    #    faceted=True,
    #    null=True)

    startdate = indexes.IntegerField(
        faceted=True,
        null=True)
    daterange = indexes.MultiValueField(
        faceted=True,
        null=True
    )
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
    #  'querypath' : 'helper_places__name',  #if using the explosded version..
    places = indexes.MultiValueField(

        faceted=True,
        null=True
    )

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

    def prepare(self, obj):
        self.prepared_data = super().prepare(obj)
        return self.prepared_data
    #
    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return None;


# , indexes.Indexable
class PersonIndex(PomsIndex):
    """Index to replace DJFacet person result type    """


    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        if settings.PARTIAL_INDEX:
            index_q = self.get_model().objects.filter(
                id__lt=PARTIAL_INDEX_MAX_ID
            ).order_by('pk')
        else:
            index_q = self.get_model().objects.filter().order_by(
                'pk'
            )
        return index_q

    def prepare(self, obj):

        self.prepared_data = super(PersonIndex, self).prepare(obj)
        self.prepared_data['index_type'] = 'person'

        self.prepared_data[
            'titles'] = list(poms_models.TitleType.objects.filter(
            facttitle__people=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'surnames'
        ] = obj.helper_searchbigsur
        self.prepared_data[
            'forenames'
        ] = obj.forename
        if obj.helper_searchbigsur is not None:
            self.prepared_data[
                'surname'
            ] = obj.helper_searchbigsur
        else:
            self.prepared_data[
                'surname'
            ] = ''
        self.prepared_data[
            'persondisplayname'
        ] = obj.persondisplayname

        self.prepared_data[
            'forename'
        ] = obj.forename
        if obj.genderkey:
            self.prepared_data[
                'gender'
            ] = obj.genderkey.name
            if obj.genderkey.id == 5:
                self.prepared_data[
                    'institutions'] = [obj.persondisplayname]

        if obj.medievalgaelicforename:
            self.prepared_data[
                'medievalgaelicforename'
            ] = obj.medievalgaelicforename.name
        if obj.standardmedievalname:
            self.standardmedievalname = obj.standardmedievalname
        if obj.moderngaelicname:
            self.moderngaelicname = obj.moderngaelicname

        self.prepared_data[
            'medievalgaelicsurname'
        ] = obj.medievalgaelicsurname

        if obj.moderngaelicforename:
            self.prepared_data[
                'moderngaelicforename'
            ] = obj.moderngaelicforename.name

        # self.prepared_data[
        #    'moderngaelicsurname'
        # ] = obj.moderngaelicsurname

        if obj.floruitstartyr:
            if obj.floruitstartyr > 0:
                self.prepared_data[
                    'startdate'] = obj.floruitstartyr
            else:
                self.prepared_data[
                    'startdate'] = obj.floruitendyr

        self.prepared_data[
            'daterange'] = getDateRange(obj.floruitstartyr, obj.floruitendyr)

        # Get charters
        charters = poms_models.Charter.objects.filter(
            factoids__people=obj
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

            self.prepared_data['documenttype'] = [d for d in set(
            documenttype)]
            self.prepared_data['documentcategory'] = [d for d in
                                                      set(documentcategory)]
            self.prepared_data['grantorcategory'] = [d for d in
                                                     set(grantor_category)]
            self.prepared_data['placedatemodern'] = [d for d in
                                                     set(placedatemodern)]
            self.prepared_data['language'] = [l for l in set(languages)]
            self.prepared_data['sourcesfeatures'] = [d for d in
                                                     set(sourcesfeatures)]

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
            poms_models.Poss_Revenues_silver.objects.filter(
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
                factoid__people=obj
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

    def get_model(self):
        return poms_models.Person


class FactoidIndex(PomsIndex, indexes.Indexable):
    """Index to replace DJFacet person result type    """

    def prepare(self, obj):
        # force save of the object if auto_save
        #if AUTO_SAVE:
        #    obj.save()
        self.prepared_data = super(FactoidIndex, self).prepare(obj)
        self.prepared_data['index_type'] = 'factoid'
        self.prepared_data[
            'description'] = obj.shortdesc
        self.prepared_data['inferred_type'] = obj.inferred_type
        source = obj.sourcekey
        if source:
            self.prepared_data['source'] = source.__str__()
            self.prepared_data['hammondnumber'] = source.hammondnumber
            self.prepared_data['hammondnumb2'] = source.hammondnumb2
            self.prepared_data['hammondnumb3'] = source.hammondnumb3

        self.prepared_data[
            'surnames'
        ] = list(poms_models.Person.objects.filter(
            factoids=obj
        ).distinct().values_list('helper_searchbigsur', flat=True))

        self.prepared_data[
            'forenames'
        ] = list(poms_models.Person.objects.filter(
            factoids=obj
        ).distinct().values_list('forename', flat=True))

        self.prepared_data[
            'gender'
        ] = list(poms_models.Gender.objects.filter(
            person__factoids=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'medievalgaelicforename'
        ] = list(poms_models.MedievalGaelicForename.objects.filter(
            person__factoids=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'moderngaelicforename'
        ] = list(poms_models.ModernGaelicForename.objects.filter(
            person__factoids=obj
        ).distinct().values_list('name', flat=True))

        # self.prepared_data[
        #    'moderngaelicsurname'
        # ] = list(poms_models.Person.objects.filter(
        #    factoids=obj
        # ).distinct().values_list('moderngaelicsurname', flat=True))

        # self.prepared_data[
        #    'moderngaelicsurname'
        # ] = list(poms_models.Person.objects.filter(
        #    factoids=obj
        # ).distinct().values_list('moderngaelicsurname', flat=True))

        # if 'transaction' in obj.inferred_type:
        #     # facttransaction__from_year
        #     ft =poms_models.FactTransaction.objects.get(id=obj.id)
        #     startdate = ft.from_year

        # elif 'title / occupation' in obj.inferred_type:
        # elif 'possession' in obj.inferred_type:
        # elif 'relationship' in obj.inferred_type:

        self.prepared_data[
            'startdate'] = obj.from_year

        self.prepared_data[
            'daterange'] = getDateRange(obj.from_year)

        self.prepared_data[
            'titles'] = list(poms_models.TitleType.objects.filter(
            facttitle=obj
        ).distinct().values_list('name', flat=True))

        # Get charters
        charters = poms_models.Charter.objects.filter(
            factoids=obj
        ).distinct()

        """
                charter_id = indexes.IntegerField(null=True)
            source_tradid = indexes.CharField(null=True, default='')
            place_types = indexes.MultiValueField(
                null=True)
                """

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

            self.prepared_data['documenttype'] = [d for d in set(
            documenttype)]
            self.prepared_data['documentcategory'] = [d for d in
                                                      set(documentcategory)]
            self.prepared_data['grantorcategory'] = [d for d in
                                                     set(grantor_category)]
            self.prepared_data['placedatemodern'] = [d for d in
                                                     set(placedatemodern)]
            self.prepared_data['language'] = [l for l in set(languages)]
            self.prepared_data['sourcesfeatures'] = [d for d in
                                                     set(sourcesfeatures)]

        self.prepared_data['possunfreepersons'] = list(
            poms_models.Poss_Unfree_persons.objects.filter(
                factoid=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['posslands'] = list(
            poms_models.Poss_Lands.objects.filter(
                factoid=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['possrevkind'] = list(
            poms_models.Poss_Revenues_kind.objects.filter(
                factoid=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['possrevsilver'] = list(
            poms_models.Poss_Revenues_silver.objects.filter(
                factoid=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['privileges'] = list(
            poms_models.Privileges.objects.filter(
                factoid=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['places'] = list(
            poms_models.Place.objects.filter(
                helper_factoids=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['roles'] = list(
            poms_models.Role.objects.filter(
                assochelperperson__person__factoids=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data['relationshiptypes'] = list(
            poms_models.Relationshiptype.objects.filter(
                factrelationship=obj
            ).distinct().values_list('name', flat=True))

        # todo is this right? assochelperperson__person__id

        self.prepared_data[
            'institutions'] = list(
            poms_models.Institution.objects.filter(
                factoids=obj
            ).distinct().values_list('persondisplayname', flat=True))

        self.prepared_data[
            'spiritualbenefits'] = list(
            poms_models.Proanimagenerictypes.objects.filter(
                facttransaction=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'spiritualbenefits'] = list(
            poms_models.Transactiontype.objects.filter(
                facttransaction=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'transactiontypes'] = list(
            poms_models.Transactiontype.objects.filter(
                facttransaction=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'transfeatures'] = list(
            poms_models.TransTickboxes.objects.filter(
            facttransaction=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'possoffice'] = list(
            poms_models.Poss_Office.objects.filter(
                factoid=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data[
            'tenendasoptions'] = list(
            poms_models.Tenendasclauseoptions.objects.filter(
                facttransaction=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data[
            'exemptionoptions'] = list(
            poms_models.Exemptiontype.objects.filter(
                facttransaction=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data[
            'sicutclause'] = list(poms_models.Sicutclausetype.objects.filter(
            facttransaction=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'returnsrenders'] = list(
            poms_models.Returns_renders.objects.filter(
                facttransaction=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'nominalrenders'] = list(
            poms_models.Nominalrendertype.objects.filter(
                facttransaction=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'renderdates'] = list(poms_models.Renderdate.objects.filter(
            facttransaction=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'returnsmilitary'] = list(
            poms_models.Returns_military.objects.filter(
                facttransaction=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'legalpertinents'] = list(
            poms_models.LegalPertinents.objects.filter(
                facttransaction=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'commonburdens'] = list(poms_models.CommonBurdens.objects.filter(
            facttransaction=obj
        ).distinct().values_list('name', flat=True))

        return self.prepared_data

    def get_model(self):
        return poms_models.Factoid

# , indexes.Indexable
class SourceIndex(PomsIndex):
    """Index to replace DJFacet person result type    """

    def prepare(self, obj):
        # force save of the object if auto_save
        self.prepared_data = super().prepare(obj)
        print("Indexing SourceIndex: " + str(obj.pk) + "\n")
        # import pdb;
        # pdb.set_trace()
        self.prepared_data['index_type'] = 'source'
        self.prepared_data['calendar_number'] = obj.hammondnumber
        self.prepared_data['description'] = obj.description
        self.prepared_data['hammondnumber'] = obj.hammondnumber
        self.prepared_data['hammondnumb2'] = obj.hammondnumb2
        self.prepared_data['hammondnumb3'] = obj.hammondnumb3

        self.prepared_data[
            'surnames'
        ] = list(poms_models.Person.objects.filter(
            factoids__sourcekey=obj
        ).distinct().values_list('helper_searchbigsur', flat=True))

        self.prepared_data[
            'forenames'
        ] = list(poms_models.Person.objects.filter(
            factoids__sourcekey=obj
        ).distinct().values_list('forename', flat=True))

        self.prepared_data[
            'gender'
        ] = list(poms_models.Gender.objects.filter(
            person__factoids__sourcekey=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'medievalgaelicforename'
        ] = list(poms_models.MedievalGaelicForename.objects.filter(
            person__factoids__sourcekey=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'moderngaelicforename'
        ] = list(poms_models.ModernGaelicForename.objects.filter(
            person__factoids__sourcekey=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'startdate'] = obj.from_year

        self.prepared_data[
            'daterange'] = getDateRange(obj.from_year)

        self.prepared_data[
            'titles'] = list(poms_models.TitleType.objects.filter(
            facttitle__sourcekey=obj
        ).distinct().values_list('name', flat=True))

        # Get charters
        charters = poms_models.Charter.objects.filter(
            factoids__sourcekey=obj
        ).distinct()

        if charters.count() > 0:
            documenttype = list()
            documentcategory = list()
            grantor_category = list()
            placedatemodern = list()
            languages = list()
            sourcesfeatures = list()
            places = list(
                poms_models.Place.objects.filter(
                    helper_factoids__sourcekey=obj
                ).distinct().values_list('name', flat=True)
            )

            for c in charters:
                if c.placefk:
                    places.append(c.placefk.name)
                if c.chartertypekey:
                    documenttype.append(c.chartertypekey.name)
                documentcategory.append(c.hammondnumber)
                if c.grantor_category:
                    grantor_category.append(c.grantor_category.name)
                placedatemodern.append(c.placedatemodern)
                if c.language:
                    languages.append(c.language.name)
                """
                Source features
                """

                if c.ischirograph is True:
                    sourcesfeatures.append('Chirograph')
                if c.letterpatent is True:
                    sourcesfeatures.append('Letter Patent')
                if c.origcontemp is True:
                    sourcesfeatures.append('Original (contemporary)')
                if c.orignoncontemp is True:
                    sourcesfeatures.append('Original (non-contemporary)')
                if c.duporigcontemp is True:
                    sourcesfeatures.append('Duplicate Original (contemporary)')
                if c.duporignoncontemp is True:
                    sourcesfeatures.append(
                        'Duplicate Original (non-contemporary)')

            self.prepared_data['documenttype'] = [d for d in set(documenttype)]
            self.prepared_data['documentcategory'] = [d for d in
                                                      set(documentcategory)]
            self.prepared_data['grantorcategory'] = [d for d in
                                                     set(grantor_category)]
            self.prepared_data['placedatemodern'] = [d for d in
                                                     set(placedatemodern)]
            self.prepared_data['language'] = [l for l in set(languages)]
            self.prepared_data['sourcesfeatures'] = [d for d in
                                                     set(sourcesfeatures)]

            self.prepared_data['places'] = places

        self.prepared_data['possunfreepersons'] = list(
            poms_models.Poss_Unfree_persons.objects.filter(
                factoid__sourcekey=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['posslands'] = list(
            poms_models.Poss_Lands.objects.filter(
                factoid__sourcekey=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['possrevkind'] = list(
            poms_models.Poss_Revenues_kind.objects.filter(
                factoid__sourcekey=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['possrevsilver'] = list(
            poms_models.Poss_Revenues_silver.objects.filter(
                factoid__sourcekey=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['privileges'] = list(
            poms_models.Privileges.objects.filter(
                factoid__sourcekey=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['roles'] = list(
            poms_models.Role.objects.filter(
                assochelperperson__person__factoids__sourcekey=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data['relationshiptypes'] = list(
            poms_models.Relationshiptype.objects.filter(
                factrelationship__sourcekey=obj
            ).distinct().values_list('name', flat=True))

        # todo is this right? assochelperperson__person__id

        self.prepared_data[
            'institutions'] = list(
            poms_models.Institution.objects.filter(
                factoids__sourcekey=obj
            ).distinct().values_list('persondisplayname', flat=True))

        self.prepared_data[
            'spiritualbenefits'] = list(
            poms_models.Proanimagenerictypes.objects.filter(
                facttransaction__sourcekey=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'spiritualbenefits'] = list(
            poms_models.Transactiontype.objects.filter(
                facttransaction__sourcekey=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'transactiontypes'] = list(
            poms_models.Transactiontype.objects.filter(
                facttransaction__sourcekey=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'transfeatures'] = list(poms_models.TransTickboxes.objects.filter(
            facttransaction__sourcekey=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'possoffice'] = list(
            poms_models.Poss_Office.objects.filter(
                factoid__sourcekey=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data[
            'tenendasoptions'] = list(
            poms_models.Tenendasclauseoptions.objects.filter(
                facttransaction__sourcekey=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data[
            'exemptionoptions'] = list(
            poms_models.Exemptiontype.objects.filter(
                facttransaction__sourcekey=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data[
            'sicutclause'] = list(poms_models.Sicutclausetype.objects.filter(
            facttransaction__sourcekey=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'returnsrenders'] = list(
            poms_models.Returns_renders.objects.filter(
                facttransaction__sourcekey=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'nominalrenders'] = list(
            poms_models.Nominalrendertype.objects.filter(
                facttransaction__sourcekey=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'renderdates'] = list(poms_models.Renderdate.objects.filter(
            facttransaction__sourcekey=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'returnsmilitary'] = list(
            poms_models.Returns_military.objects.filter(
                facttransaction__sourcekey=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'legalpertinents'] = list(
            poms_models.LegalPertinents.objects.filter(
                facttransaction__sourcekey=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'commonburdens'] = list(poms_models.CommonBurdens.objects.filter(
            facttransaction__sourcekey=obj
        ).distinct().values_list('name', flat=True))

        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        if settings.PARTIAL_INDEX:
            return self.get_model().objects.filter(
                Q(id__lt=PARTIAL_INDEX_MAX_ID),
                Q(hammondnumb2__gt=0) | Q(hammondnumber__gt=0) | Q(
                    hammondnumb3__gt=0)
            )
        else:
            return self.get_model().objects.filter(
                Q(hammondnumb2__gt=0) | Q(hammondnumber__gt=0) | Q(
                    hammondnumb3__gt=0)
            )

    def get_model(self):
        return poms_models.Source


class PlaceIndex(PomsIndex, indexes.Indexable):
    """Index to replace DJFacet place result type    """

    def prepare(self, obj):
        self.prepared_data = super(PlaceIndex, self).prepare(obj)
        self.prepared_data['index_type'] = 'place'
        self.prepared_data[
            'place_name'] = obj.name
        if obj.parent:
            self.prepared_data[
                'place_parent'] = obj.parent.name
        self.prepared_data[
            'surnames'
        ] = list(poms_models.Person.objects.filter(
            helper_places=obj
        ).distinct().values_list('helper_searchbigsur', flat=True))

        self.prepared_data[
            'forenames'
        ] = list(poms_models.Person.objects.filter(
            helper_places=obj
        ).distinct().values_list('forename', flat=True))

        # find the earliest date for all data related to this place
        # and the latest for startdate and range
        startdates = []
        early_person = poms_models.Person.objects.filter(
            helper_places=obj
        ).order_by('floruitstartyr')
        if early_person.count() > 0:
            if early_person[0].floruitstartyr is not None:
                startdates.append(early_person[0].floruitstartyr)
        early_factoid = poms_models.Factoid.objects.filter(
            helper_places=obj
        ).order_by('from_year')
        if early_factoid.count() > 0:
            if early_factoid[0].from_year is not None:
                startdates.append(early_factoid[0].from_year)
        if len(startdates) > 0:
            startdates.sort()
            self.prepared_data[
                'startdate'] = startdates[0]

        enddates = []
        end_person = poms_models.Person.objects.filter(
            helper_places=obj
        ).order_by('-floruitstartyr')
        if end_person.count() > 0 and end_person[0].floruitstartyr is not None:
            enddates.append(end_person[0].floruitstartyr)
        end_factoid = poms_models.Factoid.objects.filter(
            helper_places=obj
        ).order_by('-from_year')
        if end_factoid.count() > 0 and end_factoid[0].from_year is not None:
            enddates.append(end_factoid[0].from_year)
        if len(enddates) > 0:
            enddates.sort(reverse=True)
            if len(startdates) > 0:
                self.prepared_data[
                    'daterange'
                ] = getDateRange(
                    startdates[0],
                    enddates[-1]
                )

        self.prepared_data[
            'gender'
        ] = list(poms_models.Gender.objects.filter(
            person__helper_places=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'medievalgaelicforename'
        ] = list(poms_models.MedievalGaelicForename.objects.filter(
            person__helper_places=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'moderngaelicforename'
        ] = list(poms_models.ModernGaelicForename.objects.filter(
            person__helper_places=obj
        ).distinct().values_list('name', flat=True))

        # self.prepared_data[
        #    'moderngaelicsurname'
        # ] = list(poms_models.Person.objects.filter(
        #    helper_places=obj
        # ).distinct().values_list('moderngaelicsurname', flat=True))

        # self.prepared_data[
        #    'moderngaelicsurname'
        # ] = list(poms_models.Person.objects.filter(
        #    helper_places=obj
        # ).distinct().values_list('moderngaelicsurname', flat=True))

        self.prepared_data[
            'titles'] = list(poms_models.TitleType.objects.filter(
            facttitle__helper_places=obj
        ).distinct().values_list('name', flat=True))
        self.prepared_data['places'] = [obj.name]

        # Get charters
        charters = poms_models.Charter.objects.filter(
            factoids__helper_places=obj
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
            self.prepared_data['documentcategory'] = [d for d in
                                                      set(documentcategory)]
            self.prepared_data['grantorcategory'] = [d for d in
                                                     set(grantor_category)]
            self.prepared_data['placedatemodern'] = [d for d in
                                                     set(placedatemodern)]
            self.prepared_data['language'] = [l for l in set(languages)]
            self.prepared_data['sourcesfeatures'] = [d for d in
                                                     set(sourcesfeatures)]

        self.prepared_data['possunfreepersons'] = list(
            poms_models.Poss_Unfree_persons.objects.filter(
                factoid__helper_places=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['posslands'] = list(
            poms_models.Poss_Lands.objects.filter(
                factoid__helper_places=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['possrevkind'] = list(
            poms_models.Poss_Revenues_kind.objects.filter(
                factoid__helper_places=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['possrevsilver'] = list(
            poms_models.Poss_Revenues_silver.objects.filter(
                factoid__helper_places=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['privileges'] = list(
            poms_models.Privileges.objects.filter(
                factoid__helper_places=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data['places'] = [obj.name]

        self.prepared_data['roles'] = list(
            poms_models.Role.objects.filter(
                assochelperperson__person__helper_places=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data['relationshiptypes'] = list(
            poms_models.Relationshiptype.objects.filter(
                factrelationship__helper_places=obj
            ).distinct().values_list('name', flat=True))

        # todo is this right? assochelperperson__person__id

        self.prepared_data[
            'institutions'] = list(
            poms_models.Institution.objects.filter(
                factoids__helper_places=obj
            ).distinct().values_list('persondisplayname', flat=True))

        self.prepared_data[
            'spiritualbenefits'] = list(
            poms_models.Proanimagenerictypes.objects.filter(
                facttransaction__helper_places=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'spiritualbenefits'] = list(
            poms_models.Transactiontype.objects.filter(
                facttransaction__helper_places=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'transactiontypes'] = list(
            poms_models.Transactiontype.objects.filter(
                facttransaction__helper_places=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'transfeatures'] = list(poms_models.TransTickboxes.objects.filter(
            facttransaction__helper_places=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'possoffice'] = list(
            poms_models.Poss_Office.objects.filter(
                factoid__helper_places=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data[
            'tenendasoptions'] = list(
            poms_models.Tenendasclauseoptions.objects.filter(
                facttransaction__helper_places=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data[
            'exemptionoptions'] = list(
            poms_models.Exemptiontype.objects.filter(
                facttransaction__helper_places=obj
            ).distinct().values_list('name', flat=True)
        )

        self.prepared_data[
            'sicutclause'] = list(poms_models.Sicutclausetype.objects.filter(
            facttransaction__helper_places=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'returnsrenders'] = list(
            poms_models.Returns_renders.objects.filter(
                facttransaction__helper_places=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'nominalrenders'] = list(
            poms_models.Nominalrendertype.objects.filter(
                facttransaction__helper_places=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'renderdates'] = list(poms_models.Renderdate.objects.filter(
            facttransaction__helper_places=obj
        ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'returnsmilitary'] = list(
            poms_models.Returns_military.objects.filter(
                facttransaction__helper_places=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'legalpertinents'] = list(
            poms_models.LegalPertinents.objects.filter(
                facttransaction__helper_places=obj
            ).distinct().values_list('name', flat=True))

        self.prepared_data[
            'commonburdens'] = list(poms_models.CommonBurdens.objects.filter(
            facttransaction__helper_places=obj
        ).distinct().values_list('name', flat=True))

        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        queryset = self.get_model().objects.all()
        if settings.PARTIAL_INDEX and (self.get_model().objects.all().count() > 500):
            return queryset.filter(pk__lt=500)
        else:
            return queryset

    def get_model(self):
        return poms_models.Place
