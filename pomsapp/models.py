from django.db.models.fields.related import ManyToOneRel
from django.contrib.admin import widgets
from django.conf.urls import *  # noqa
from django.contrib.gis.db.models import *  # noqa
from django.utils.translation import ugettext_lazy as _
# from settings import print
from django.contrib.admin.sites import site

from pomsapp.actions_models import *  # noqa
#
# ASSOCIATIONs
#
from pomsapp.models_associations import *  # noqa
#
# AUTHORITY LISTS
#
from pomsapp.models_authlists import *  # noqa
#
# POSSESSIONS and PRIVILEGES
#
from pomsapp.models_possessions import *  # noqa


#  TEMP
# from pomsapp.models_possessions_legacy import *


#
# MAIN DOMAIN OBJECTS
#
class Person(mymodels.PomsModel):
    persondisplayname = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Surface name", )
    standardmedievalname = models.CharField(
        max_length=255, null=True, blank=True,
        verbose_name="Medieval gaelic name", )
    moderngaelicname = models.CharField(
        max_length=255, null=True, blank=True,
        verbose_name="Modern gaelic name", )
    persondescription = models.TextField(
        null=True, blank=True, verbose_name="biography", )

    floruitstartpre = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name="pre-modifier", )
    floruitstartyr = models.IntegerField(
        null=True, blank=True, verbose_name="from year", )
    floruitstartpost = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name="post-modifier", )
    floruitendpre = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name="pre-modifier", )
    floruitendyr = models.IntegerField(
        null=True, blank=True, verbose_name="to year", )
    floruitendpost = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name="post-modifier", )
    florlowkey = models.ForeignKey(
        'Floruit', null=True, blank=True,
        verbose_name="FROM  :: century", related_name='flor_lowKey', )
    florhikey = models.ForeignKey(
        'Floruit', null=True, blank=True,
        verbose_name="TO  :: century", related_name='flor_hiKey', )

    genderkey = models.ForeignKey(
        'Gender', null=True, blank=True,
        verbose_name="Gender", default=3)

    forename = models.CharField(
        max_length=765, verbose_name="Forename", null=True, blank=True, )
    surname = models.CharField(
        max_length=765, verbose_name="Surname", null=True, blank=True, )
    sonof = models.CharField(
        max_length=765, verbose_name="SonOf", null=True, blank=True, )
    patronym = models.CharField(
        max_length=765, verbose_name="Patronym", null=True, blank=True, )
    ofstring = models.CharField(
        max_length=765, verbose_name="ofString", null=True, blank=True, )
    placeandinst = models.CharField(
        max_length=765, verbose_name="Place/ institutional",
        null=True, blank=True, )
    datestring = models.CharField(
        max_length=765, verbose_name="Dates", null=True, blank=True, )
    # mikele: 4dec09
    searchsurname = models.CharField(
        max_length=765,
        verbose_name="Normalized field including surnames\
                     stripped of non-interesting particles, for searching "
                     "purposes only",
        null=True,
        blank=True, )
    # mikele: 18/1/10
    moderngaelicforename = models.ForeignKey(
        ModernGaelicForename, null=True, blank=True,
        verbose_name="modern gaelic forename", )
    moderngaelicsurname = models.CharField(
        blank=True, max_length=100, verbose_name="modern gaelic surname")
    medievalgaelicforename = models.ForeignKey(
        MedievalGaelicForename, null=True, blank=True,
        verbose_name="medieval gaelic forename", )
    medievalgaelicsurname = models.CharField(
        blank=True, max_length=100, verbose_name="medieval gaelic surname")

    relatedplace = models.ForeignKey(
        'Place',
        null=True,
        blank=True,
        verbose_name="Related place [reference\
                     extracted from place-institutional]",
        help_text="Experimental Feature: this value has\
                  been extracted from the place/institutional field below")

    # 2010-11-17: new helper table to facilitate querying places' hierarchies
    # from person (for FB specifically)
    helper_places = models.ManyToManyField(
        'Place',
        verbose_name="helper M2M table used to speed up searched\
                     in FB, from all persons to all places",
        related_name='helper_persons')

    # new 17/6/2010 :: default=True doesn't seem to work... well who cares!
    helper_floruits = models.BooleanField(
        default=True, verbose_name="Calculate floruits automatically\
                                   (warning: saving time can take longer)",
        help_text="Using all primary transactions where person has role:\
                  Grantor, Beneficiary, Addressor, Addressee, "
                  "Party 1, Party 2, Party 3, Consentor, Dated by hand of,\
                  Inspector, Scribe, Sealer, Signatory, "
                  "Witness")
    helper_merge = models.BooleanField(
        default=False, verbose_name="Keep as main record in\
                                    \'merge\' operation",
        help_text="Tick to indicate that other person-records will have\
                  to be merged into this record, "
                  "and not otherwise")
    # mikele: 29June2010
    helper_bigsurname = models.CharField(
        max_length=765,
        verbose_name="Field that displays a combination surname, sonOf,\
                     Patronym, ofString, Place-inst, for the FB "
                     "only",
        null=True, blank=True, )
    helper_searchbigsur = models.CharField(
        max_length=765, verbose_name="Same as field above, but normalized",
        null=True, blank=True, )

    helper_keywordsearch = models.CharField(
        max_length=765, verbose_name="Field for the keyword search",
        null=True, blank=True, )
    helper_totfactoids = models.IntegerField(
        blank=True, null=True,
        verbose_name="Field that speeds up searches of people by tot number\
                     of factoids associated to them. MIND that "
                     "it's not updated automatically, you need to\
                     manually run fixture 8 instead!", )

    helper_daterange = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name="helper field for date ranges - automatically generated\
                     so to accommodate a fixed date-range "
                     "search facet (todo: supersede via a proper\
                     extension of the faceted browser)")

    # NJ Hack to indicate presence of family relationship in Gephi
    has_family = models.NullBooleanField(blank=True, null=True)
    has_grantor = models.NullBooleanField(blank=True, null=True)

    ponelink = models.URLField(
        blank=True,
        verbose_name="Link to PoNE")

    ponelink_sureness = models.CharField(
        blank=True,
        max_length=3,
        choices=PONELINK_SURENESS,
        verbose_name="Degree of certainty",
        default="pro")  #

    def how_many_factoids(self):
        num = 0
        num += len(self.getassocfactoids())
        num += len(self.getassocfactoidproanimas())
        num += len(self.assocfactoidwitness())
        return num

    how_many_factoids.allow_tags = True

    # Replacing old _set many to many calls with these functions

    def getassocfactoidproanimas(self):
        return AssocFactoidProanima.objects.filter(person=self)

    def getassocfactoids(self):
        return AssocFactoidPerson.objects.filter(person=self)

    def assocfactoidwitness(self):
        return AssocFactoidWitness.objects.filter(person=self)

    def how_many_sources(self):
        """helper method: shows how many unique sources mention a person"""
        sources = []
        for x in self.getassocfactoids():
            try:
                s = x.factoid.sourcekey
                sources.append(s)
            except BaseException:
                pass
        for x in self.getassocfactoidproanimas():
            try:
                s = x.factoid.sourcekey
                sources.append(s)
            except BaseException:
                pass
        for x in self.assocfactoidwitness():
            try:
                s = x.factoid.sourcekey
                sources.append(s)
            except BaseException:
                pass
        return len(list(set(sources)))

    how_many_sources.allow_tags = True

    def nice_floruits(self):
        """Mind that we're using the html representation of the 'x' sign """

        if self.floruitstartyr and self.floruitendyr:
            return "%s &times; %s" % (self.floruitstartyr, self.floruitendyr)
        elif self.floruitstartyr and not self.floruitendyr:
            return "%s &times;" % (self.floruitstartyr)
        elif not self.floruitstartyr and self.floruitendyr:
            return "&times; %s" % (self.floruitendyr)
        else:
            return ""

    def get_association_factoids(self, whattype="", ordering=None):
        """
        Get all factoid-association instances (not the factoids!).
        Valid types are possession, relationship, title/occupation,
        transaction ; or proanima and witness
        Ordering is expressed in the form of a list of attributes
        """
        if not whattype:
            # return ALL  [this supersedes what used to be called
            # get_all_associations]
            return list(self.getassocfactoids()) +\
                list(self.getassocfactoidproanimas()) + list(
                self.assocfactoidwitness())

        elif whattype in ['possession', 'relationship',
                          'title/occupation', 'transaction']:
            if not ordering:
                return self.getassocfactoids().filter(
                    factoid__inferred_type=whattype)
            else:
                return self.getassocfactoids().filter(
                    factoid__inferred_type=whattype).order_by(*ordering)

        elif whattype == "proanima":
            if not ordering:
                return self.getassocfactoidproanimas()
            else:
                return self.getassocfactoidproanimas().order_by(*ordering)

        elif whattype == "witness":
            if not ordering:
                return self.assocfactoidwitness()
            else:
                return self.assocfactoidwitness().order_by(*ordering)
        else:
            print("Valid factoid types are: 'possession', 'relationship',"
                  "'title/occupation', 'transaction', 'proanima', 'witness'"
                  )
            return []

    get_association_factoids.allow_tags = True

    def get_factoids(self, whattype="", ordering=None):
        """
        Get all factoids (not the associations!).
        Valid types are possession, relationship, title/occupation,
        transaction ; or proanima and witness
        Returs the right subclass of Factoids, depending on what requested.
        """
        if not whattype:
            return list(self.factoids.all(
            )) + list(self.factoidsproanima.all()) +\
                list(self.factoidswitness.all())
        elif whattype in ['possession', 'relationship',
                          'title/occupation', 'transaction']:
            if not ordering:
                factoid_set = self.factoids.filter(inferred_type=whattype)
            else:
                factoid_set = self.factoids.filter(
                    inferred_type=whattype).order_by(*ordering)
            # returns the right factoid type
            return [f.get_right_subclass()[1]
                    for f in factoid_set if f.get_right_subclass]

        elif whattype == "proanima":
            if not ordering:
                return self.factoidsproanima.all()
            else:
                return self.factoidsproanima.all().order_by(*ordering)
            return [f.get_right_subclass()[1]
                    for f in factoid_set if f.get_right_subclass]

        elif whattype == "witness":
            if not ordering:
                factoid_set = self.factoidswitness.all()
            else:
                factoid_set = self.factoidswitness.all().order_by(*ordering)
            return [f.get_right_subclass()[1]
                    for f in factoid_set if f.get_right_subclass]

        else:
            # return ALL  [this supersedes also get_all_associations]
            print("Valid factoid types are: 'possession', 'relationship',\
                  'title/occupation', 'transaction', 'proanima', 'witness'")
            return []

    get_factoids.allow_tags = True

    def get_commonFactoids(self, p2, count_only=False):
        """
        Get the factoids where two people both appear at the same time

        >>> p = Person.objects.get(pk=2323)
        >>> p.get_commonFactoids( Person.objects.get(pk=5718))

        2012-08-17: added count only option

        """
        if count_only:
            return Factoid.objects.filter(
                assochelperperson__person__id=self.id).filter(
                assochelperperson__person__id=p2.id).distinct().count()
        else:
            common = Factoid.objects.filter(
                assochelperperson__person__id=self.id).filter(
                assochelperperson__person__id=p2.id).distinct()
            if common:
                return [f.get_right_subclass()[1]
                        for f in common if f.get_right_subclass]
            else:
                return []

    def get_factoidRole(self, factoid):
        """
        >>> p1 = Person.objects.get(pk=41)
        >>> p2 = Person.objects.get(pk=7)
        >>> factoids = p1.get_commonFactoids(p2)
        >>> f1 =factoids[0]
        >>> f1
        <FactTransaction: id[42197], from source [4/32/24
        (_Dunf. Reg._, no. 211)] >
        >>> p1.get_factoidRole(f1)
        [<Role: Sealer>]
        >>> p2.get_factoidRole(f1)
        [<Role: Party 1>]
        """
        associations = factoid.assochelperperson_set.filter(person=self)
        if associations:
            return [x.role for x in associations if x.role]
        else:
            return []

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_person_change', args=(self.id,))
        # return "/%sadmin/pomsapp/person/%s" % (django_settings.URL_PREFIX,
        # self.id)

    get_admin_url.allow_tags = True

    def get_databrowse_url(self):
        return "/%sdatabrowse/pomsapp/person/objects/%s" % (
            django_settings.URL_PREFIX, self.id)

    get_databrowse_url.allow_tags = True

    # returns all associations form a person:  method useful for template
    # rendering

    @models.permalink
    def get_absolute_url(self):
        return ('person_detail', [str(self.id)])

    def save(self, force_insert=False, force_update=False,
             calculate_floruits=False):
        # create the searchsurname field
        if EXTRA_SAVING_ACTIONS:
            super(Person, self).save(force_insert, force_update)
            self = create_helper_surnames(self)
            if self.helper_floruits:
                # update 'floruitstartyr' and  'floruitendyr'
                self = build_floruits(self)
            self = create_helperKeywordsearch(self)
            self = create_helperDateRange(self)
        super(Person, self).save(
            force_insert, force_update)  # Call the "real" save() method.

    class Meta:
        ordering = ["persondisplayname"]

    class Admin(FkAutocompleteAdmin):  # admin.ModelAdmin
        # related_search_fields = { 'genderkey': ('name',), }
        related_search_fields = {'relatedplace': ('name',), }

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj = createPersonSurface_name(obj)
            obj.save()

        actions = ['merge_people_action']

        def merge_people_action(self, request, queryset):
            persons_to_merge = []
            main_persons = []
            for obj in queryset:
                if obj.helper_merge:  # identify the person
                    main_persons.append(obj)
                else:
                    persons_to_merge.append(obj)
            if len(main_persons) == 1:
                feedback = merge_persons_inner(main_persons[
                    0], persons_to_merge)
                self.message_user(request, "Records %s succesfully\
                    merged into [%s]" % (
                    feedback[1], feedback[0]))
            if len(main_persons) == 0:
                self.message_user(
                    request,
                    "ERROR detected: you selected %s but none of these\
                    records are marked as 'main'!" %
                    persons_to_merge)
            if len(main_persons) > 1:
                self.message_user(
                    request, "ERROR detected: you selected %s as MAIN\
                    persons, only one is allowed!" % main_persons)

        merge_people_action.short_description = "Merge selected people"

        list_display = ('id', 'persondisplayname', 'forename',
                        'surname', 'editedrecord', 'review', 'updated_at',)
        # list_editable = ('persondisplayname',)
        # filter_horizontal = ('location',)
        # radio_fields = {"ltbrole": admin.VERTICAL}
        list_filter = ['created_at', 'updated_at',
                       'created_by__username', 'editedrecord', 'review', ]
        search_fields = ['persondisplayname', 'id']
        date_hierarchy = 'created_at'
        fieldsets = [
            ('Administration',
             {'fields':
              ['helper_merge', 'editedrecord', 'review', 'internal_notes',
               ('created_at', 'created_by'),
               ('updated_at', 'updated_by')
               ],
              'classes': ['collapse']
              }
             ),
            ('Names in headline form (automatically generated)',
             {'fields':
              ['persondisplayname', 'standardmedievalname',
               'moderngaelicname', ]
              }
             ),
            ('',
             {'fields':
              ['genderkey', 'persondescription', 'relatedplace']}),
            ('Name components',
             {'fields':
              ['forename', 'surname', 'sonof', 'patronym',
               'ofstring', 'placeandinst', 'datestring']
              }
             ),
            ('Medieval Gaelic Name components',
             {'fields':
              ['medievalgaelicforename', 'medievalgaelicsurname']
              }
             ),
            ('Modern Gaelic Name components',
             {'fields':
              ['moderngaelicforename', 'moderngaelicsurname']
              }
             ),
            ('Floruits',
             {'fields':  # to be ORDERED
              ['helper_floruits',
               ('florlowkey', 'floruitstartpre',
                'floruitstartyr', 'floruitstartpost'),
               ('florhikey', 'floruitendpre', 'floruitendyr',
                'floruitendpost'), ]}),
            ('Links to PoNE',
             {'fields':  # to be ORDERED
              ['ponelink', 'ponelink_sureness']
              }),
        ]

    def __str__(self):
        return self.persondisplayname

    def __unicode__(self):
        return self.persondisplayname

    table_order = 5


class Institution_Manager(models.Manager):
    def get_query_set(self):
        return super(Institution_Manager, self).get_query_set().filter(
            genderkey__id=5)


class Institution(Person):
    objects = Institution_Manager()

    class Meta:
        proxy = True


class PersonNoInstitutions_Manager(models.Manager):
    def get_query_set(self):
        return super(PersonNoInstitutions_Manager,
                     self).get_query_set().exclude(genderkey__id=5)


class PersonNoInstitutions(Person):
    objects = PersonNoInstitutions_Manager()

    class Meta:
        proxy = True


class Source(mymodels.PomsModel):
    """Metaclass for MAtrix, CHartes etc.. at the moment we're using
    only Charters"""
    # sourcekey = models.IntegerField() --> automatically created
    source_tradid = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="Trad. ID", )
    # sourcetypekey = models.IntegerField()  --> not nec. cause we have
    # subclasses
    description = models.TextField(
        null=True, blank=True, verbose_name="description", )
    sourcefordataentry = models.TextField(
        null=True, blank=True, verbose_name="source for data entry", )
    # otherprintedsources = models.TextField(blank=True)  --> never used
    # manuscriptsource = models.TextField(blank=True)  --> never used

    hammondnumber = models.IntegerField(
        null=True, blank=True, verbose_name="calendar number #1", )
    hammondnumb2 = models.IntegerField(
        null=True, blank=True, verbose_name="#2", )
    hammondnumb3 = models.IntegerField(
        null=True, blank=True, verbose_name="#3", )
    hammondext = models.CharField(
        max_length=300, null=True, blank=True, verbose_name="ext.", )

    mofa_flag = models.NullBooleanField()

    notes = models.TextField(null=True, blank=True, verbose_name="notes", )
    # I put at this level the date info specs
    # new dates 15/1/10
    firmdate = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="Firm date [preview]",
        help_text="Field automatically composed from the fields above.\
                  Please do not modify it directly, but instead "
                  "modify the from/to options above.")
    has_firmdate = models.BooleanField(
        default=False, verbose_name="Has firm date")
    has_firmdayonly = models.BooleanField(
        default=False, verbose_name="DAY only firmdate")
    undated = models.BooleanField(default=False, verbose_name="undated")
    eitheror = models.BooleanField(default=False, verbose_name="either/or")
    from_modifier = models.CharField(
        blank=True, max_length=3, choices=DATE_MODIFIERS,
        verbose_name="date of charter  - FROM", help_text="modifier")  # exa
    from_weekday = models.IntegerField(
        blank=True, null=True, choices=WEEKDAY_CHOICES, verbose_name="",
        help_text="weekday")
    from_day = models.IntegerField(
        blank=True, null=True, choices=DAY_CHOICES, verbose_name="",
        help_text="day", )
    from_modifier2 = models.CharField(
        blank=True, max_length=3, choices=DATE_MODIFIERS2,
        help_text="modifier2", verbose_name="", )
    from_month = models.IntegerField(
        blank=True, null=True, choices=MON_CHOICES, verbose_name="",
        help_text="month")
    from_season = models.IntegerField(
        blank=True, null=True, choices=SEASON_CHOICES, help_text="season",
        verbose_name="", )
    from_year = models.IntegerField(
        blank=True, null=True, verbose_name="",
        help_text="enter a year in numbers")
    to_modifier = models.CharField(
        blank=True, max_length=3, choices=DATE_MODIFIERS,
        verbose_name="date of charter  - TO", help_text="modifier")
    to_weekday = models.IntegerField(
        blank=True, null=True, choices=WEEKDAY_CHOICES, help_text="weekday",
        verbose_name="", )
    to_day = models.IntegerField(
        blank=True, null=True, choices=DAY_CHOICES, help_text="day",
        verbose_name="", )
    to_modifier2 = models.CharField(
        blank=True, max_length=3, choices=DATE_MODIFIERS2,
        help_text="modifier2", verbose_name="", )
    to_month = models.IntegerField(
        blank=True, null=True, choices=MON_CHOICES, help_text="month",
        verbose_name="", )
    to_season = models.IntegerField(
        blank=True, null=True, choices=SEASON_CHOICES, help_text="season",
        verbose_name="", )
    to_year = models.IntegerField(
        blank=True, null=True, verbose_name="",
        help_text="enter a year in numbers")
    # end ======== new dates 15/1/10
    probabledate = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="prob date", )
    datingnotes = models.TextField(
        null=True, blank=True, verbose_name="dating notes", )

    language = models.ForeignKey(
        Language, null=True, blank=True, verbose_name="language",
        default=1)
    # 2010-08-18 => new inferred grantor category
    grantor_category = models.ForeignKey(
        GrantorCategory, null=True, blank=True,
        verbose_name="grantor category")

    helper_hammond = models.CharField(
        max_length=50,
        verbose_name="We store here the results of get_hammondnumber(),\
        for faster ordering", null=True,
        blank=True, )
    helper_keywordsearch = models.TextField(
        verbose_name="Field for the keyword search", null=True, blank=True,)
    helper_daterange = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name="helper field for date ranges - automatically generated\
                     so to accommodate a fixed date-range "
                     "search facet (todo: supersede via a proper extension\
                     of the faceted browser)")
    helper_totfactoids = models.IntegerField(
        blank=True, null=True,
        verbose_name="Field that speeds up searches of sources by tot\
                     number of factoids associated to them. MIND "
                     "that it's not updated automatically, you need\
                     to manually run fixture 8 instead!", )

    def get_right_subclass(self):
        # once you get a source instance, it's useful to know quickly what
        # subclass it is...
        try:
            sbcls = ["charter", self.charter]
        except BaseException:
            sbcls = None
        return sbcls

    get_right_subclass.allow_tags = True

    def get_hammondnumber(self):
        # creates a nice representation of the HN...
        try:
            nice_hn = "%s/%s/%s %s" % (
                self.hammondnumber or '0', self.hammondnumb2 or '0',
                self.hammondnumb3 or '0', self.hammondext)
        except BaseException:
            print(
                "++++++ GET_HAMMONDNUMBER(): Problems creating the\
                hammond number ++++++")
            nice_hn = "Problems creating the H number"
        return nice_hn

    get_hammondnumber.allow_tags = True

    def get_factoids(self, whattype="", ordering=None):
        """
        Get all factoids (not the associations!).
        Valid types are possession, relationship, title/occupation,
        transaction
        Returs the right subclass of Factoids, depending on what requested.
        """
        if not whattype:
            return self.factoids.all()
        elif whattype in ['possession', 'relationship', 'title/occupation',
                          'transaction']:
            if not ordering:
                factoid_set = self.factoids.filter(inferred_type=whattype)
            else:
                factoid_set = self.factoids.filter(
                    inferred_type=whattype).order_by(*ordering)
            # returns the right factoid type
            return [f.get_right_subclass()[1]
                    for f in factoid_set if f.get_right_subclass]

        else:
            # return ALL  [this supersedes also get_all_associations]
            print("Valid factoid types are: 'possession', 'relationship'," +
                  "'title/occupation', 'transaction'")
            return []

    get_factoids.allow_tags = True

    @models.permalink
    def get_absolute_url(self):
        return ('source_detail', [str(self.id)])

    class Meta:
        pass

    def __str__(self):
        out = "%s/%s/%s %s (%s)" % (self.hammondnumber or '0',
                                    self.hammondnumb2 or '0',
                                    self.hammondnumb3 or '0',
                                    self.hammondext,
                                    self.source_tradid)
        return out

    def __unicode__(self):
        return self.__str__()

    table_order = 4


class Charter(Source):
    chartertypekey = models.ForeignKey(
        'Chartertype', blank=True, null=True, verbose_name="document type")

    ischirograph = models.BooleanField(
        default=False, verbose_name="Chirograph?")
    doctypenotes = models.TextField(blank=True,
                                    verbose_name="Doc type notes")
    placedatemodern = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="Place (modern)", )
    placedatedoc = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="Place (document)", )
    placefk = models.ForeignKey(
        'Place', null=True, blank=True, verbose_name="Place", )

    letterpatent = models.BooleanField(
        default=False, verbose_name="referred to as letter patent")
    origcontemp = models.BooleanField(
        default=False, verbose_name="Original (contemporary)")
    duporigcontemp = models.BooleanField(
        default=False, verbose_name="Duplicate Original (contemporary)")
    orignoncontemp = models.BooleanField(
        default=False, verbose_name="Original (non-contemporary)")
    duporignoncontemp = models.BooleanField(
        default=False, verbose_name="Duplicate Original (non-contemporary)")

    helper_hnumber = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="h-number",
        help_text="A helper field that conflates al the\
        hNumbers, for better alpha searching", )
    helper_copydates = models.BooleanField(
        default=True,
        verbose_name="Copy dates to related Factoids?",
        help_text="(excluding non-primary transactions)")

    helper_tickboxes = models.ManyToManyField(
        'DocTickboxes', blank=True,
        verbose_name="normalization of tickboxes",
        help_text="Helper field used for the faceted\
                  search - see actionsmodels", )

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_charter_change', args=(self.id,))
        # return "/%sadmin/pomsapp/charter/%s" %
        # (django_settings.URL_PREFIX_EXTRA, self.id)

    get_admin_url.allow_tags = True

    def get_databrowse_url(self):
        return "/%sdatabrowse/pomsapp/charter/objects/%s" % (
            django_settings.URL_PREFIX_EXTRA, self.id)

    get_databrowse_url.allow_tags = True

    def save(self, force_insert=False, force_update=False):
        """fills out the helper_hnumber field"""
        if EXTRA_SAVING_ACTIONS:
            super(Charter, self).save(force_insert, force_update)
            handle_tickboxes(self)
            temp = self.get_hammondnumber()

            self.helper_hnumber = temp
            self.helper_hammond = temp
            self.firmdate = create_firmdate(self)
            if self.helper_copydates:
                copy_charter_dates2factoids(self)
            if not self.grantor_category:
                assign_grantorCategory(self)
            self = create_helperKeywordsearch(self)
            self = create_helperDateRange(self)
        super(Charter, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Documents"
        verbose_name = "Document"
        ordering = ['id']

    class Admin(NoLookupsForeignKeyAutocompleteAdmin):
        related_search_fields = {'placefk': ('name',), }

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()

        list_display = (
            'source_tradid', 'placedatemodern', 'hammondnumber',
            'hammondnumb2', 'hammondnumb3', 'hammondext',
            'helper_hnumber',
            'editedrecord', 'review', 'updated_by', 'updated_at',)
        # raw_id_fields = ('chartertypekey',)
        # filter_horizontal = ('location',)
        # radio_fields = {"ltbrole": admin.VERTICAL}

        list_filter = ['created_at', 'updated_at', 'created_by__username',
                       'editedrecord', 'review', 'undated', 'has_firmdate']
        search_fields = ['source_tradid', 'placedatemodern',
                         'hammondnumber', 'hammondnumb2', 'hammondnumb3',
                         'hammondext', 'id']
        fieldsets = [
            ('Administration',
             {'fields':
              ['editedrecord', 'review', 'internal_notes',
               ('created_at', 'created_by'),
               ('updated_at', 'updated_by')
               ],
              'classes': ['collapse']
              }),
            ('ID',
             {'fields':
              ['source_tradid', (
                  'hammondnumber', 'hammondnumb2', 'hammondnumb3',
                  'hammondext', 'mofa_flag'), ]
              }),
            ('Description',
             {'fields':
              ['chartertypekey', ('ischirograph', 'letterpatent',),
               'language', 'doctypenotes',
               'description', 'sourcefordataentry']
              }),
            ('Dates',
             {'fields':
              [('has_firmdate', 'has_firmdayonly', 'undated', 'eitheror'),
               ('from_modifier', 'from_weekday', 'from_day',
                'from_modifier2', 'from_month', 'from_season', 'from_year'),
               ('to_modifier', 'to_weekday', 'to_day',
                'to_modifier2', 'to_month', 'to_season', 'to_year'),
               'firmdate', 'probabledate', 'datingnotes', 'helper_copydates']
              }),
            ('Place date',
             {'fields':
              ['placedatemodern', 'placedatedoc', 'placefk']
              }),
            ('Other info',
             {'fields':
              [('origcontemp', 'duporigcontemp', 'orignoncontemp',
                'duporignoncontemp'), 'notes']
              }),

        ]

        # 11/6/10: firmdate is readonly
        class Media:
            js = ("js/admin_fixes/admin_fixes.js",)

    def __str__(self):
        #     if self.source_tradid:
        # italic_name = self.source_tradid.replace("_", "<i>", 1)
        # italic_name = italic_name.replace("_", "</i>", 1)
        # out = "Document %s/%s/%s %s (%s)" % (self.hammondnumber,
        # self.hammondnumb2, self.hammondnumb3, self.hammondext,
        # self.source_tradid)
        out = "Document %s/%s/%s %s (%s)" % (
            self.hammondnumber or '0', self.hammondnumb2 or '0',
            self.hammondnumb3 or '0', self.hammondext,
            self.source_tradid)
        return out

    def __unicode__(self):
        return self.__str__()

    table_order = 1


#
# SEALS
#
# add links on Matrix page: 'add transaction for this matrix'
# ===> explore how to pass data from one admin view to another one
class Matrix(Source):
    shape = models.ForeignKey(
        'MatrixShape', null=True, blank=True, verbose_name="matrix shape", )
    owner = models.ForeignKey(
        'Person', null=True, blank=True, verbose_name="Owner", )
    identifier = models.CharField(max_length=100, verbose_name="identifier")
    image_desc = models.TextField(
        blank=True, null=True, verbose_name="image description (obverse)")
    image_desc_rev = models.TextField(
        blank=True, null=True, verbose_name="image description (reverse)")
    legend_obv = models.TextField(
        blank=True, null=True, verbose_name="legend (obverse)")
    legend_rev = models.TextField(
        blank=True, null=True, verbose_name="legend (reverse)")
    catalogue = models.CharField(
        blank=True, null=True, max_length=300, verbose_name="catalogue")

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_matrix_change', args=(self.id,))
        # return "/%sadmin/pomsapp/matrix/%s" %
        # (django_settings.URL_PREFIX_EXTRA, self.id)

    get_admin_url.allow_tags = True

    def get_databrowse_url(self):
        return "/%sdatabrowse/pomsapp/matrix/objects/%s" % (
            django_settings.URL_PREFIX_EXTRA, self.id)

    get_databrowse_url.allow_tags = True

    @models.permalink
    def get_absolute_url(self):
        return ('matrix_detail', [str(self.id)])

    class Admin(NoLookupsForeignKeyAutocompleteAdmin):
        related_search_fields = {'owner': ('persondisplayname',), }

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()

        list_display = ('identifier', 'shape', 'catalogue',
                        'editedrecord', 'review', 'updated_by', 'updated_at',)
        search_fields = ('id',)
        list_filter = ('shape', 'created_at', 'updated_at',
                       'created_by__username', 'editedrecord', 'review',)
        fieldsets = [
            ('Administration',
             {'fields':
              ['editedrecord', 'review', 'internal_notes',
               ('created_at', 'created_by'),
               ('updated_at', 'updated_by')
               ],
              'classes': ['collapse']
              }),
            ('Main info',
             {'fields':
              ['owner', 'identifier', 'shape', 'image_desc',
               'image_desc_rev', 'legend_obv', 'legend_rev']
              }),
            ('Other info',
             {'fields':
              ['catalogue', 'notes']
              }),
        ]

    class Meta:
        verbose_name_plural = "Matrixes"

    def __str__(self):
        return "%s %s" % ("Matrix", self.identifier)


# add links on Seal page: 'add transaction for this seal'


class Seal(Source):
    """(Seal description)"""
    charter_field = models.ForeignKey(
        'Charter', verbose_name="charter", blank=True, null=True,
        db_column='charter_id')
    matrix_field = models.ForeignKey(
        'Matrix',
        verbose_name="matrix",
        db_column='matrix_id')
    color = models.ForeignKey(
        'SealColor', verbose_name="seal color", blank=True, null=True, )
    att_type_surv = models.ForeignKey(
        'AttachmentType', related_name="surv_attach_of",
        verbose_name="Attachment type",
        blank=True, null=True, )
    # att_type_notsurv = models.ForeignKey('AttachmentType',
    # related_name = "nonsurv_attach_of",
    # verbose_name="Attachment type (not surviving)", blank=True, null=True,)
    # twosided = models.BooleanField(default=False, verbose_name="two sided?")
    countersealed = models.BooleanField(
        default=False, verbose_name="countersealed?")
    archive = models.CharField(
        max_length=200, verbose_name="archive", blank=True, null=True, )
    archiverefnumber = models.CharField(
        max_length=100, verbose_name="archive ref number",
        blank=True, null=True, )
    conditionnote = models.TextField(
        verbose_name="condition note", blank=True, null=True, )

    # new 21 Jun 2010
    scranlink = models.URLField(
        verbose_name="Link to Scran.ac.uk", blank=True, null=True, )

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_seal_change', args=(self.id,))
        # return "/%sadmin/pomsapp/seal/%s" %
        # (django_settings.URL_PREFIX_EXTRA, self.id)

    get_admin_url.allow_tags = True

    def get_databrowse_url(self):
        return "/%sdatabrowse/pomsapp/seal/objects/%s" % (
            django_settings.URL_PREFIX_EXTRA, self.id)

    get_databrowse_url.allow_tags = True

    class Admin(NoLookupsForeignKeyAutocompleteAdmin):
        related_search_fields = {'charter_field': (
            'hammondnumber', 'hammondnumb2', 'hammondnumb3'), }

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()

        list_display = ('matrix_field', 'color', 'countersealed',
                        'editedrecord', 'review', 'updated_by',
                        'updated_at',)
        search_fields = ('id',)
        list_filter = ('matrix_field', 'color', 'created_at', 'updated_at',
                       'created_by__username', 'editedrecord', 'review',)
        fieldsets = [
            ('Administration',
             {'fields':
              ['editedrecord', 'review', 'internal_notes',
               ('created_at', 'created_by'),
               ('updated_at', 'updated_by')
               ],
              'classes': ['collapse']
              }),
            ('',
             {'fields':
              ['charter_field', ]
              }),
            ('Seal info',
             {'fields':
              ['matrix_field', 'color', 'att_type_surv', 'countersealed',
               'archive', 'archiverefnumber', 'conditionnote']
              }),
            ('Links',
             {'fields':
              ['scranlink']
              }),
        ]

    class Meta:
        verbose_name_plural = "Seals"

    def __str__(self):
        return "%s %s" % ("Seal", self.id)


# END SEALS ==========================================
# ================================
# SOME ASSOCIATIONs that NEED TO BE HERE....
# ================================


class ExtraTitleCreationFrom(forms.ModelForm):
    # HACK: I'm using the admin ForeignKeyRawIdWidget which needs a 'rel'
    # instance to be passed to it. I thus create this directly using the
    # ManyToOneRel class and a model/model_field combination. The resulting
    # title object (selected by the user) is then extracted directly from the
    # request object in the TransactionFactoid code (as it used to be)
    # todo ehall rawid widget broken by upgrade, this may not work
    title = forms.ModelChoiceField(
        required=False, queryset=TitleType.objects.all(),
        empty_label="(Nothing)",
        label="title [warning: creates a new title-factoid]",
        widget=widgets.ForeignKeyRawIdWidget(
            ManyToOneRel(TitleType, 'id', 'id'), site))
    bygraceofgod = forms.BooleanField(required=False, label="by grace of..")
    byanotherdivineinvocation = forms.BooleanField(
        required=False, label="by another divine..")


#
# new extended inline that lets create Title factoids on the fly!
# inline used on Transaction factoids only
# admin.TabularInline     InlineAutocompleteAdmin
class AssocPersonInline_extended(InlineAutocompleteAdmin):

    model = AssocFactoidPerson
    verbose_name = 'Associated person'
    verbose_name_plural = 'Associated people'
    # raw_id_fields = ('person', ) #'person', TOFIX
    extra = 20
    related_search_fields = {
        'person': ('persondisplayname',),
        'role': ('name',),
    }
    # this form is just added to the normal inline
    form = ExtraTitleCreationFrom
    # formset = MyFormset


# inline used on non transaction factoids
# admin.TabularInline  InlineAutocompleteAdmin
class AssocPersonInline(InlineAutocompleteAdmin):
    model = AssocFactoidPerson
    verbose_name = 'Associated person'
    verbose_name_plural = 'Associated people'
    extra = 4
    related_search_fields = {
        'person': ('persondisplayname',),
        'role': ('name',),
    }


class AssocWitnessInline(InlineAutocompleteAdmin):
    model = AssocFactoidWitness
    # raw_id_fields = ('person',)
    verbose_name = 'Associated witness'
    verbose_name_plural = 'Associated witnesses'
    extra = 10
    # exclude = ['role']    # role is assigned by default
    related_search_fields = {
        'person': ('persondisplayname',),
    }
    form = ExtraTitleCreationFrom


class AssocProanimaInline(InlineAutocompleteAdmin):
    model = AssocFactoidProanima
    # raw_id_fields = ('person',)
    verbose_name = 'Associated ProAnima person'
    verbose_name_plural = 'Associated ProAnima people'
    extra = 2
    # exclude = ['role']
    related_search_fields = {
        'person': ('persondisplayname',),
    }
    form = ExtraTitleCreationFrom


# ================================
# FACTOIDS
# ================================
class Factoid(mymodels.PomsModel):
    inferred_type = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="inferred type",)
    sourcekey = models.ForeignKey('Source', verbose_name="Document",
                                  related_name='factoids')
    people = models.ManyToManyField(
        Person, through='AssocFactoidPerson', related_name='factoids',
        verbose_name="associated people", )
    # I put them here even though they're used only by specific Factoids!
    witnesses = models.ManyToManyField(
        Person, through='AssocFactoidWitness', related_name='factoidswitness',
        verbose_name="witnesses", )
    proanimapeople = models.ManyToManyField(
        Person, through=AssocFactoidProanima, related_name='factoidsproanima',
        verbose_name="pro anima people", )

    helper_places = models.ManyToManyField(
        'Place',
        verbose_name="helper M2M table used to speed up searched in FB,\
                     from all factoids to all places (bypassing "
                     "the possessions)",
        related_name="helper_factoids")
    poss_alms = models.ManyToManyField(
        Poss_Alms, through='AssocFactoidPoss_alms', verbose_name="alms", )
    poss_unfreep = models.ManyToManyField(
        Poss_Unfree_persons, through='AssocFactoidPoss_unfreep',
        verbose_name="unfree persons", )
    poss_revsilver = models.ManyToManyField(
        Poss_Revenues_silver, through='AssocFactoidPoss_revenuesilver',
        verbose_name="revenue in silver", )
    poss_revkind = models.ManyToManyField(
        Poss_Revenues_kind, through='AssocFactoidPoss_revenuekind',
        verbose_name="revenue in kind", )
    poss_pgeneral = models.ManyToManyField(
        Poss_General, through='AssocFactoidPoss_pgeneral',
        verbose_name="possessions in general", )
    poss_office = models.ManyToManyField(
        Poss_Office, through='AssocFactoidPoss_office',
        verbose_name="office", )
    poss_objects = models.ManyToManyField(
        Poss_Objects, through='AssocFactoidPoss_objects',
        verbose_name="objects", )
    poss_lands = models.ManyToManyField(
        Poss_Lands, through='AssocFactoidPoss_lands',
        verbose_name="lands", )
    poss_privileges = models.ManyToManyField(
        Privileges, through='AssocFactoidPrivileges',
        verbose_name="privileges", )

    shortdesc = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="short description", )
    # new dates 15/1/10
    has_firmdate = models.BooleanField(
        default=False, verbose_name="Has firm date")  # new 11/6/10
    has_firmdayonly = models.BooleanField(
        default=False, verbose_name="DAY only firmdate")
    firmdate = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="Firm date [preview]",
        help_text="Field automatically composed from the fields above.\
                  Please do not modify it directly, but instead "
                  "modify the from/to options above.")
    undated = models.BooleanField(default=False, verbose_name="undated")
    eitheror = models.BooleanField(default=False, verbose_name="either/or")
    from_modifier = models.CharField(
        blank=True, max_length=3, choices=DATE_MODIFIERS,
        verbose_name="date of factoid  - FROM", help_text="modifier")  # exa
    from_weekday = models.IntegerField(
        blank=True, null=True, choices=WEEKDAY_CHOICES, verbose_name="",
        help_text="weekday")
    from_day = models.IntegerField(
        blank=True, null=True, choices=DAY_CHOICES, verbose_name="",
        help_text="day", )
    from_modifier2 = models.CharField(
        blank=True, max_length=3, choices=DATE_MODIFIERS2,
        help_text="modifier2", verbose_name="", )
    from_month = models.IntegerField(
        blank=True, null=True, choices=MON_CHOICES, verbose_name="",
        help_text="month")
    from_season = models.IntegerField(
        blank=True, null=True, choices=SEASON_CHOICES, help_text="season",
        verbose_name="", )
    from_year = models.IntegerField(
        blank=True, null=True, verbose_name="",
        help_text="enter a year in numbers")
    to_modifier = models.CharField(
        blank=True, max_length=3, choices=DATE_MODIFIERS,
        verbose_name="date of factoid  - TO", help_text="modifier")
    to_weekday = models.IntegerField(
        blank=True, null=True, choices=WEEKDAY_CHOICES, help_text="weekday",
        verbose_name="", )
    to_day = models.IntegerField(
        blank=True, null=True, choices=DAY_CHOICES, help_text="day",
        verbose_name="", )
    to_modifier2 = models.CharField(
        blank=True, max_length=3, choices=DATE_MODIFIERS2,
        help_text="modifier2", verbose_name="", )
    to_month = models.IntegerField(
        blank=True, null=True, choices=MON_CHOICES, help_text="month",
        verbose_name="", )
    to_season = models.IntegerField(
        blank=True, null=True, choices=SEASON_CHOICES, help_text="season",
        verbose_name="", )
    to_year = models.IntegerField(
        blank=True, null=True, verbose_name="",
        help_text="enter a year in numbers")
    # end ======== new dates 15/1/10
    probabledate = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="probable date", )
    datingnotes = models.TextField(
        null=True, blank=True, verbose_name="dating notes", )
    notes = models.TextField(null=True, blank=True, verbose_name="notes", )
    # problems should go into the 'internal notes' field...
    problems = models.TextField(
        null=True, blank=True, verbose_name="problems", )
    # UNUSED
    sourceref = models.CharField(
        max_length=300, null=True, blank=True,
        verbose_name="source reference (unused for now)", )
    # 2012-08-20 updated
    helper_floruits = models.BooleanField(
        default=True, verbose_name="Calculate floruits automatically\
                                   (warning: saving time can take longer)",
        help_text="DISABLED: please re-save persons individually in order to\
                  update their floruits (or ask the db "
                  "administrator to do that for you as a batch operation)")
    # help_text="DISABLED Using all primary transactions where person has
    # role: Grantor, Beneficiary, Addressor,
    # Addressee, Party 1, Party 2, Party 3, Consentor, Dated by hand of,
    # Inspector, Scribe, Sealer, Signatory, Witness")
    # 2010-09-01: the following field conflates all people associations, for
    # faster searching...
    helper_people = models.ManyToManyField(
        Person, through='AssocHelperPerson', related_name='helperfactoids',
        verbose_name="associated people - helper field", db_index=True)

    helper_keywordsearch = models.CharField(
        max_length=765, verbose_name="Field for the keyword search",
        null=True, blank=True, )
    helper_daterange = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name="helper field for date ranges - automatically generated\
                     so to accommodate a fixed date-range "
                     "search facet (todo: supersede via a proper extension\
                     of the faceted browser)")

    @models.permalink
    def get_absolute_url(self):
        return ('factoid_detail', [str(self.id)])

    def force_inferred(self):
        """the inferred_type field can be calculated only by running a\
        save on the
        subclass of a factoid. This method retrieves the instance and\
        saves it for you."""
        test = self.get_right_subclass()
        if test:
            self.inferred_type = test[0]
            self.save()

    def get_right_subclass(self):
        # once you get a factois instance, it's useful to know quickly what
        # subclass it is...
        try:
            sbcls = ["possession", self.factpossession]
        except BaseException:
            try:
                sbcls = ["relationship", self.factrelationship]
            except BaseException:
                try:
                    sbcls = ["title/occupation", self.facttitle]
                except BaseException:
                    try:
                        sbcls = ["transaction", self.facttransaction]
                    except BaseException:
                        sbcls = None
        return sbcls

    get_right_subclass.allow_tags = True

    class Meta:
        # ordering = ('id',)
        ordering = ('from_year', 'from_month', 'from_day', 'to_year')

    def __str__(self):
        return self.shortdesc or "no description"


class FactTitle(Factoid):
    """(in poms-linnet this used to be called 'Title')"""
    # factoidkey = models.IntegerField()  --> not needed anymore
    #  there must be a title
    titletypekey = models.ForeignKey('TitleType', verbose_name="title type",)
    # these two are booleans, but's there are some strange '-1' in the db..
    # maybe it'll break
    bygraceofgod = models.BooleanField(
        default=False, blank=True, verbose_name="by grace of God", )
    byanotherdivineinvocation = models.BooleanField(
        default=False, blank=True,
        verbose_name="by another divine invocation", )

    def save(self, force_insert=False, force_update=False):
        """fills out the firmdate field"""
        if EXTRA_SAVING_ACTIONS:
            super(FactTitle, self).save(force_insert, force_update)
            if self.shortdesc == "":
                self.shortdesc = self.titletypekey.name
            self.firmdate = create_firmdate(self)
            self = create_helperKeywordsearch(self)
            self = fix_inferredType(self)
            self = create_helperDateRange(self)
        super(FactTitle, self).save(force_insert, force_update)

    def get_primaryPersons(self):
        """ Get the list of persons """
        valid_assoc1 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="primary"
        )
        valid_assoc2 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="title-holder"
        )
        valid_assoc = valid_assoc1 or valid_assoc2
        if valid_assoc:
            return [v.person for v in valid_assoc]
        else:
            return None

    # ForeignKeyAutocompleteAdmin or AutocompleteModelAdmin
    class Admin(NoLookupsForeignKeyAutocompleteAdmin):
        # raw_id_fields = ('sourcekey', )
        related_search_fields = {'sourcekey': (
            'hammondnumber', 'hammondnumb2', 'hammondnumb3'), }

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            if all_dates_blank(obj):
                x = getattr(obj, 'sourcekey', None)
                if x:
                    copy_dates_over(x, obj)
            obj.save()

        list_display = ('id', 'sourcekey', 'titletypekey', 'shortdesc',
                        'editedrecord', 'review', 'updated_by', 'updated_at',)
        inlines = (AssocPersonInline,)
        list_filter = ['created_at', 'updated_at',
                       'created_by__username', 'editedrecord', 'review', ]
        search_fields = ['shortdesc', 'id']
        fieldsets = [
            ('Administration',
             {'fields':
              ['editedrecord', 'review', 'internal_notes',
               ('created_at', 'created_by'),
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
              ['titletypekey', 'shortdesc', 'bygraceofgod',
               'byanotherdivineinvocation', 'notes']
              }),
            ('Dates',
             {'fields':
              [('has_firmdate', 'has_firmdayonly', 'undated', 'eitheror'),
               ('from_modifier', 'from_weekday', 'from_day',
                'from_modifier2', 'from_month', 'from_season', 'from_year'),
               ('to_modifier', 'to_weekday', 'to_day',
                'to_modifier2', 'to_month', 'to_season', 'to_year'),
               'firmdate', 'probabledate', 'datingnotes', ]
              }),

        ]

        # 11/6/10: firmdate is readonly
        class Media:
            js = ("js/admin_fixes/admin_fixes.js",)

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_facttitle_change', args=(self.id,))
        # return "/%sadmin/pomsapp/facttitle/%s" %
        # (django_settings.URL_PREFIX_EXTRA, self.id)

    get_admin_url.allow_tags = True

    def get_databrowse_url(self):
        return "/%sdatabrowse/pomsapp/facttitle/objects/%s" % (
            django_settings.URL_PREFIX_EXTRA, self.id)

    get_databrowse_url.allow_tags = True

    class Meta:
        verbose_name_plural = "Factoid Title/Occupation"

    def __str__(self):
        return "%s %s %s" % ("id:", self.id, self.shortdesc)

    table_order = 11


class FactRelationship(Factoid):
    """(FactRelationship description)"""
    relationship = models.ForeignKey(
        Relationshiptype, null=True, blank=True,
        verbose_name="relationship", )
    placefielty = models.ForeignKey(
        'Place', null=True, blank=True,
        verbose_name="related place (for fealty relationships)", )

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_factrelationship_change', args=(self.id,))
        # return "/%sadmin/pomsapp/factrelationship/%s" %
        # (django_settings.URL_PREFIX_EXTRA, self.id)

    get_admin_url.allow_tags = True

    def get_databrowse_url(self):
        return "/%sdatabrowse/pomsapp/factrelationship/objects/%s" % (
            django_settings.URL_PREFIX_EXTRA, self.id)

    get_databrowse_url.allow_tags = True

    def get_primaryPersons(self):
        """ Get the list of persons """
        valid_assoc1 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="primary"
        )
        # 2012-06-19: can delete the one above, after updating the roles stuff
        valid_assoc2 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="object (relationship)"
        )
        valid_assoc = valid_assoc1 or valid_assoc2
        if valid_assoc:
            return [v.person for v in valid_assoc]
        else:
            return None

    def get_secondaryPersons(self):
        """ Get the list of persons """
        valid_assoc1 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="secondary"
        )

        # 2012-06-19: can delete the one above, after updating the roles stuff
        valid_assoc2 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="subject (relationship)"
        )
        valid_assoc = valid_assoc1 or valid_assoc2
        if valid_assoc:
            return [v.person for v in valid_assoc]
        else:
            return None

    def save(self, force_insert=False, force_update=False):
        """fills out the firmdate field"""
        if EXTRA_SAVING_ACTIONS:
            super(FactRelationship, self).save(force_insert, force_update)
            self.firmdate = create_firmdate(self)
            self = create_helperKeywordsearch(self)
            self = fix_inferredType(self)
            self = create_helperDateRange(self)
        super(FactRelationship, self).save(force_insert, force_update)

    # ForeignKeyAutocompleteAdmin or AutocompleteModelAdmin
    class Admin(NoLookupsForeignKeyAutocompleteAdmin):
        # raw_id_fields = ('sourcekey', )
        related_search_fields = {
            'sourcekey': ('hammondnumber', 'hammondnumb2', 'hammondnumb3'),
            'placefielty': ('name',), }

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            if all_dates_blank(obj):
                x = getattr(obj, 'sourcekey', None)
                if x:
                    copy_dates_over(x, obj)
            obj.save()

        list_display = ('id', 'sourcekey', 'relationship', 'shortdesc',
                        'editedrecord', 'review', 'updated_by', 'updated_at',)
        # filter_horizontal = ('location',)
        # radio_fields = {"ltbrole": admin.VERTICAL}

        inlines = (AssocPersonInline,)
        list_filter = ['created_at', 'updated_at',
                       'created_by__username', 'editedrecord', 'review', ]
        search_fields = ['id', 'shortdesc']
        fieldsets = [
            ('Administration',
             {'fields':
              ['editedrecord', 'review', 'internal_notes',
               ('created_at', 'created_by'),
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
              ['relationship', 'shortdesc', 'notes', 'placefielty']
              }),
            ('Dates',
             {'fields':
              [('has_firmdate', 'has_firmdayonly', 'undated', 'eitheror'),
               ('from_modifier', 'from_weekday', 'from_day',
                'from_modifier2', 'from_month', 'from_season', 'from_year'),
               ('to_modifier', 'to_weekday', 'to_day',
                'to_modifier2', 'to_month', 'to_season', 'to_year'),
               'firmdate', 'probabledate', 'datingnotes', ]
              }),

        ]

        # 11/6/10: firmdate is readonly
        class Media:
            js = ("js/admin_fixes/admin_fixes.js",)

    class Meta:
        verbose_name_plural = "Factoid Relationship"

    def __str__(self):
        return "id[%s], from source [%s], desc: %s" % (
            self.id, self.sourcekey, self.shortdesc)

    table_order = 12


class FactReference(Factoid):
    """(FactReference description)"""
    reference = models.ForeignKey(
        Referencetype, null=True, blank=True, verbose_name="reference", )
    placefielty = models.ForeignKey(
        'Place', null=True, blank=True,
        verbose_name="related place (for fielty relationships)", )

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_factreference_change', args=(self.id,))
        # return "/%sadmin/pomsapp/FactReference/%s" %
        # (django_settings.URL_PREFIX_EXTRA, self.id)

    get_admin_url.allow_tags = True

    def get_databrowse_url(self):
        return "/%sdatabrowse/pomsapp/factreference/objects/%s" % (
            django_settings.URL_PREFIX_EXTRA, self.id)

    get_databrowse_url.allow_tags = True

    def save(self, force_insert=False, force_update=False):
        """fills out the firmdate field"""
        if EXTRA_SAVING_ACTIONS:
            super(FactReference, self).save(force_insert, force_update)
            self.firmdate = create_firmdate(self)
            self = create_helperKeywordsearch(self)
            self = fix_inferredType(self)
            self = create_helperDateRange(self)
        super(FactReference, self).save(force_insert, force_update)

    # ForeignKeyAutocompleteAdmin or AutocompleteModelAdmin
    class Admin(NoLookupsForeignKeyAutocompleteAdmin):
        # raw_id_fields = ('sourcekey', )
        related_search_fields = {
            'sourcekey': ('hammondnumber', 'hammondnumb2', 'hammondnumb3'),
            'placefielty': ('name',), }

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            if all_dates_blank(obj):
                x = getattr(obj, 'sourcekey', None)
                if x:
                    copy_dates_over(x, obj)
            obj.save()

        list_display = ('id', 'sourcekey', 'reference', 'shortdesc',
                        'editedrecord', 'review', 'updated_by', 'updated_at')
        # filter_horizontal = ('location',)
        # radio_fields = {"ltbrole": admin.VERTICAL}

        inlines = (AssocPersonInline,)
        list_filter = ['created_at', 'updated_at',
                       'created_by__username', 'editedrecord', 'review', ]
        search_fields = ['id', 'shortdesc']
        fieldsets = [
            ('Administration',
             {'fields':
              ['editedrecord', 'review', 'internal_notes',
               ('created_at', 'created_by'),
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
              ['reference', 'shortdesc', 'notes', 'placefielty']
              }),
            ('Dates',
             {'fields':
              [('has_firmdate', 'has_firmdayonly', 'undated', 'eitheror'),
               ('from_modifier', 'from_weekday', 'from_day',
                'from_modifier2', 'from_month', 'from_season', 'from_year'),
               ('to_modifier', 'to_weekday', 'to_day',
                'to_modifier2', 'to_month', 'to_season', 'to_year'),
               'firmdate', 'probabledate', 'datingnotes', ]
              }),

        ]

        # 11/6/10: firmdate is readonly
        class Media:
            js = ("js/admin_fixes/admin_fixes.js",)

    class Meta:
        verbose_name_plural = "Factoid Reference"

    def __str__(self):
        return "id[%s], from source [%s], desc: %s" % (
            self.id, self.sourcekey, self.shortdesc)

    table_order = 12


class FactPossession(Factoid):
    """(FactPossession description)"""

    # the possession relation is in Factoid

    # add a method for showing possessions in a list

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_factpossession_change', args=(self.id,))
        # return "/%sadmin/pomsapp/factpossession/%s" %
        # (django_settings.URL_PREFIX_EXTRA, self.id)

    get_admin_url.allow_tags = True

    def get_databrowse_url(self):
        return "/%sdatabrowse/pomsapp/factpossession/objects/%s" % (
            django_settings.URL_PREFIX_EXTRA, self.id)

    get_databrowse_url.allow_tags = True

    def get_primaryPersons(self):
        """ Get the list of persons """

        valid_assoc1 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="primary"
        )
        # 2012-06-19: can delete the one above, after updating the roles stuff
        valid_assoc2 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="holder (possession)"
        )
        valid_assoc = valid_assoc1 or valid_assoc2
        if valid_assoc:
            return [v.person for v in valid_assoc]
        else:
            return None

    def get_secondaryPersons(self):
        """ Get the list of persons """

        valid_assoc1 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="secondary"
        )
        # 2012-06-19: can delete the one above, after updating the roles stuff
        valid_assoc2 = AssocFactoidPerson.objects.filter(
            factoid=self,
            role__name__icontains="lord (possession)"
        )
        valid_assoc = valid_assoc1 or valid_assoc2
        if valid_assoc:
            return [v.person for v in valid_assoc]
        else:
            return None

    def save(self, force_insert=False, force_update=False):
        """fills out the firmdate field"""
        if EXTRA_SAVING_ACTIONS:
            super(FactPossession, self).save(force_insert, force_update)
            self.firmdate = create_firmdate(self)
            self = create_helperKeywordsearch(self)
            self = fix_inferredType(self)
            self = create_helperDateRange(self)
        super(FactPossession, self).save(force_insert, force_update)

    # ForeignKeyAutocompleteAdmin or AutocompleteModelAdmin
    class Admin(NoLookupsForeignKeyAutocompleteAdmin):
        # raw_id_fields = ('sourcekey', )
        related_search_fields = {'sourcekey': (
            'hammondnumber', 'hammondnumb2', 'hammondnumb3'), }

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            if all_dates_blank(obj):
                x = getattr(obj, 'sourcekey', None)
                if x:
                    copy_dates_over(x, obj)
            obj.save()

        list_display = ('id', 'sourcekey', 'shortdesc',
                        'editedrecord', 'review', 'updated_by', 'updated_at',)
        # filter_horizontal = ('location',)
        # radio_fields = {"ltbrole": admin.VERTICAL}
        inlines = (
            AssocPersonInline, AssocFactoidPrivilegesInline,
            AssocFactoidPoss_almsInline,
            AssocFactoidPoss_unfreepInline, AssocFactoidPoss_revsilverInline,
            AssocFactoidPoss_revkindInline,
            AssocFactoidPoss_pgeneralInline, AssocFactoidPoss_officeInline,
            AssocFactoidPoss_objectsInline,
            AssocFactoidPoss_landsInline,)  # Assoc_FactPossessionInline
        list_filter = ['created_at', 'updated_at',
                       'created_by__username', 'editedrecord', 'review', ]
        search_fields = ['id', 'shortdesc']
        fieldsets = [
            ('Administration',
             {'fields':
              ['editedrecord', 'review', 'internal_notes',
               ('created_at', 'created_by'),
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
              ['shortdesc', 'notes']
              }),
            ('Dates',
             {'fields':
              [('has_firmdate', 'has_firmdayonly', 'undated', 'eitheror'),
               ('from_modifier', 'from_weekday', 'from_day',
                'from_modifier2', 'from_month', 'from_season', 'from_year'),
               ('to_modifier', 'to_weekday', 'to_day',
                'to_modifier2', 'to_month', 'to_season', 'to_year'),
               'firmdate', 'probabledate', 'datingnotes', ]
              }),

        ]

        # 11/6/10: firmdate is readonly
        class Media:
            js = ("js/admin_fixes/admin_fixes.js",)

    class Meta:
        verbose_name_plural = "Factoid Possession"

    def __str__(self):
        return "id[%s], from source [%s]" % (self.id, self.sourcekey)
        # ", ".join(["%s" % p for p in self.possessions.all()]))

    table_order = 13


class FactTransaction(Factoid):
    """The main factoid at the moment"""

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_facttransaction_change', args=(self.id,))
        # return "/%sadmin/pomsapp/facttransaction/%s" %
        # (django_settings.URL_PREFIX_EXTRA, self.id)

    get_admin_url.allow_tags = True

    def get_databrowse_url(self):
        return "/%sdatabrowse/pomsapp/facttransaction/objects/%s" % (
            django_settings.URL_PREFIX_EXTRA, self.id)

    get_databrowse_url.allow_tags = True

    transactiontype = models.ForeignKey(
        Transactiontype, null=True, blank=True,
        verbose_name="type of transaction", )

    isprimary = models.BooleanField(default=False, verbose_name="Primary")
    isdare = models.BooleanField(default=False, verbose_name="Dare?")
    isexchange = models.BooleanField(default=False, verbose_name="Exchange")
    verbsnotspecified = models.BooleanField(
        default=False, verbose_name="verbs not specified?")
    conveth = models.BooleanField(default=False, verbose_name="Conveth?")
    # witnesses
    genericwitnesses = models.BooleanField(
        default=False,
        verbose_name="Witnesses in original, but not copied into cartulary")
    testemeipso = models.BooleanField(
        default=False, verbose_name="teste me ipso")

    # many2many
    tenendas = models.ManyToManyField(
        Tenendasclauseoptions, verbose_name="tenendas", blank=True)
    exemptions = models.ManyToManyField(
        Exemptiontype, verbose_name="exemptions", blank=True)
    tenendasclauseolang = models.TextField(
        blank=True, verbose_name="tenendas orig. languag")
    exemptionclauseolang = models.TextField(
        blank=True, verbose_name="exemptions orig. languag")
    renderdates = models.ManyToManyField(
        Renderdate, verbose_name="render dates", blank=True)
    rendernominal = models.ManyToManyField(
        Nominalrendertype, verbose_name="nominal renders", blank=True)
    sicutclauses = models.ManyToManyField(
        Sicutclausetype,
        verbose_name="sicut clause or equivalent", blank=True)

    previouschartermention = models.BooleanField(
        default=False,
        verbose_name="previous mention of charter")
    previouschirographmention = models.BooleanField(
        default=False,
        verbose_name="previous mention of chirograph")
    perambulation = models.BooleanField(
        default=False, verbose_name="perambulation")
    corroborationsealing = models.BooleanField(
        default=False, verbose_name="corroboration / sealing")
    # added by Matthew 17/2/09 -->
    ismalediction = models.BooleanField(
        default=False, verbose_name="malediction?")
    bothaddressorsmentioned = models.BooleanField(
        default=False, verbose_name="both addressors mentioned")
    warrandice = models.BooleanField(default=False, verbose_name="warrandice")

    # new many2many 5 Jun (translation of 'tickboxOptions')
    legalpertinents = models.ManyToManyField(
        LegalPertinents, verbose_name="additional legal pertinents",
        blank=True)
    returnsmilitary = models.ManyToManyField(
        Returns_military, verbose_name="returns / military", blank=True)
    returnsrenders = models.ManyToManyField(
        Returns_renders, verbose_name="returns / renders", blank=True)
    commonburdens = models.ManyToManyField(
        CommonBurdens, verbose_name="common burdens", blank=True)

    spiritualbenefits = models.ManyToManyField(
        Proanimagenerictypes, verbose_name="Generics",
        blank=True)

    helper_tickboxes = models.ManyToManyField(
        'TransTickboxes', blank=True,
        verbose_name="normalization of tickboxes",
        help_text="Helper field used for the faceted\
                  search - see actionsmodels", )

    def save(self, force_insert=False, force_update=False):
        """fills out the firmdate field"""
        if EXTRA_SAVING_ACTIONS:
            super(FactTransaction, self).save(force_insert, force_update)
            handle_tickboxes(self)
            self.firmdate = create_firmdate(self)
            # calc floruits of related people (fixed on 2012-08-20)
            updateFloruitsFromTransaction(self)
            self = create_helperKeywordsearch(self)
            self = fix_inferredType(self)
            self = fix_spiritualBenefits(self)
            self = create_helperDateRange(self)
        super(FactTransaction, self).save(force_insert, force_update)

    # ForeignKeyAutocompleteAdmin or AutocompleteModelAdmin
    class Admin(NoLookupsForeignKeyAutocompleteAdmin):
        # raw_id_fields = ('sourcekey', )
        related_search_fields = {'sourcekey': (
            'hammondnumber', 'hammondnumb2', 'hammondnumb3'), }

        def save_model(self, request, obj, form, change):
            # adds the user information when the rec is saved
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            # import the dates from the Source if they are left empty
            if all_dates_blank(obj):
                if obj.isprimary is True:
                    x = getattr(obj, 'sourcekey', None)
                    if x:
                        copy_dates_over(x, obj)
            obj.save()
            # previously: if obj.firmdate == "" and obj.datingnotes == "" and
            # obj.probabledate == "" and obj.isprimary == True:

            #  HACK ====>>>>>>>
            # here I'm manually checking if there are title factoids
            # to create on the fly
            # hacking into the POST data directly...
            req = request.POST
            # x = req.items()    # just printing all the items so that I
            # can check them...
            # obj.notes = str(x)
            # temp = ""
            # assoc_fields contains the name of the forms where we're looking
            assoc_fields = [
                'assocfactoidperson', 'assocfactoidwitness',
                'assocfactoidproanima']
            # title = req.get("assocfactoidperson_set-1-title", None)
            # assocfactoidwitness_set-1-person
            # (u'assocfactoidproanima_set-1-person', u'')
            for assoc in assoc_fields:
                tot_forms = req.get(
                    assoc + "_set-TOTAL_FORMS", None)
                for i in range(
                        0, int(tot_forms)):  # foreach check if theres a title
                    # title info
                    stringa_title = assoc + "_set-" + str(i) + "-title"
                    titleid = req.get(stringa_title, None)
                    stringa_grace = assoc + "_set-" + \
                        str(i) + "-bygraceofgod"
                    gracegod = req.get(stringa_grace, None)
                    stringa_divine = assoc + "_set-" + \
                        str(i) + "-byanotherdivineinvocation"
                    divineinvocation = req.get(stringa_divine, None)
                    # the person info
                    stringa_person = assoc + "_set-" + str(i) + "-person"
                    personid = req.get(stringa_person, None)
                    stringa_origlanguage = assoc + \
                        "_set-" + str(i) + "-nameoriglang"
                    originallanguage = req.get(stringa_origlanguage, None)
                    stringa_translation = assoc + \
                        "_set-" + str(i) + "-nametranslation"
                    nametranslation = req.get(stringa_translation, None)
                    stringa_medieval = assoc + "_set-" + \
                        str(i) + "-standardmedievalform"
                    medievalform = req.get(stringa_medieval, None)
                    if titleid:  # then get the right fields and
                        # creates a title factoid
                        # i'm passing the whole obj so that the dates can be
                        # copied over
                        print(
                            "++ Transaction requested to save extra\
                            Title-factoid for title id=[%s]" % titleid)
                        self.create_title_fact(
                            request.user, obj.sourcekey, titleid, gracegod,
                            divineinvocation, obj,
                            personid, originallanguage, nametranslation,
                            medievalform)

        # method for creating a title-factoid on the fly
        def create_title_fact(self, userobj, sourceobj, titleid, gracegod,
                              divineinvocation, obj_for_dates,
                              personid, originallanguage, nametranslation,
                              medievalform):

            # t = FactTitle(sourcekey=sourceobj, firmdate=firmdate,
            # datingnotes=datingnotes, probabledate=probabledate)
            t = FactTitle(sourcekey=sourceobj)
            copy_dates_over(obj_for_dates, t)
            if gracegod:
                t.bygraceofgod = gracegod
            if divineinvocation:
                t.byanotherdivineinvocation = divineinvocation
            t.titletypekey = TitleType.objects.get(pk=titleid)
            t.created_by = userobj
            t.updated_by = userobj
            t.save()
            ass = AssocFactoidPerson(
                factoid=t, nameoriglang=originallanguage,
                nametranslation=nametranslation,
                standardmedievalform=medievalform)
            ass.person = Person.objects.get(pk=personid)
            # old version :::  rol = Role.objects.get(name='Primary')
            rol = Role.objects.get(
                pk=75)  # 2012-08-20: 'title-holder' role by default
            ass.role = rol
            ass.save()
            print("Title-factoid saved! [%s - id=%d]" % (
                str(TitleType.objects.get(pk=titleid)), t.id))

        list_display = ('id', 'sourcekey', 'shortdesc',
                        'editedrecord', 'review', 'updated_by',
                        'updated_at',)
        filter_horizontal = (
            'sicutclauses', 'renderdates', 'rendernominal', 'tenendas',
            'spiritualbenefits', 'exemptions',
            'legalpertinents', 'returnsmilitary',
            'returnsrenders', 'commonburdens')
        # radio_fields = {"ltbrole": admin.VERTICAL}
        inlines = (
            AssocPersonInline_extended, AssocWitnessInline,
            AssocProanimaInline,
            AssocFactoidPrivilegesInline, AssocFactoidPoss_almsInline,
            AssocFactoidPoss_unfreepInline, AssocFactoidPoss_revsilverInline,
            AssocFactoidPoss_revkindInline,
            AssocFactoidPoss_pgeneralInline, AssocFactoidPoss_officeInline,
            AssocFactoidPoss_objectsInline,
            AssocFactoidPoss_landsInline,)

        list_filter = ['isprimary', 'created_at', 'updated_at',
                       'created_by__username', 'editedrecord', 'review', ]
        search_fields = ['shortdesc', 'id']
        fieldsets = [
            ('Administration',
             {'fields':
              ['editedrecord', 'review', 'internal_notes',
               ('created_at', 'created_by'),
               ('updated_at', 'updated_by')
               ],
              'classes': ['collapse']
              }),
            ('Source and transaction type',
             {'fields':
              ['sourcekey', 'transactiontype', ('isprimary', 'isdare',
                                                'verbsnotspecified',
                                                'isexchange', 'conveth')]
              }),
            ('Description',
             {'fields':
              ['shortdesc', 'notes']
              }),
            ('Dates',
             {'fields':
              [('has_firmdate', 'has_firmdayonly', 'undated', 'eitheror'),
               ('from_modifier', 'from_weekday', 'from_day',
                'from_modifier2', 'from_month', 'from_season', 'from_year'),
               ('to_modifier', 'to_weekday', 'to_day',
                'to_modifier2', 'to_month', 'to_season', 'to_year'),
               'firmdate', 'probabledate', 'datingnotes', 'helper_floruits']
              }),
            ('Clauses: tenendas and exemption',
             {'fields': ['tenendas', 'tenendasclauseolang', 'exemptions',
                         'exemptionclauseolang', ],
              'classes': ['collapse']
              }),
            ('Clauses: renders',
             {'fields':
              ['renderdates', 'rendernominal', ],
              'classes': ['collapse']
              }),
            ('Clauses: sicut clause, add. legal pertinents,\
             returns/renders and common burdens',
             {'fields':
              ['sicutclauses', 'legalpertinents', 'returnsmilitary',
               'returnsrenders', 'commonburdens', ],
              'classes': ['collapse']
              }),
            ('Clauses: other tickboxes',
             {'fields':
              [('previouschartermention', 'previouschirographmention'),
               'perambulation', 'ismalediction', 'corroborationsealing',
               'bothaddressorsmentioned',
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

        # 11/6/10: firmdate is readonly
        class Media:
            js = ("js/admin_fixes/admin_fixes.js",)

    class Meta:
        verbose_name_plural = "Factoid Transaction"

    def __str__(self):
        return "id[%s], from source [%s] " % (self.id, self.sourcekey)

    table_order = 15


class PlaceType(mymodels.PomsModel):
    description = models.CharField(max_length=50)

    class Admin(admin.ModelAdmin):
        pass

    def __str__(self):
        return u'%s' % self.description

    class Meta:
        ordering = ['description', ]


# 2010-11-12: added the helper_name field, although we still dont use it!
class Place(mymodels.PomsModel):
    """(Place description)"""
    name = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="name", )
    genericname = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="generic name", )
    articletext = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="article text", )
    specificname = models.CharField(
        max_length=765, null=True, blank=True, verbose_name="specific name", )
    parent = models.ForeignKey(
        'Place', null=True, blank=True, verbose_name="parent place",
        related_name="children", )
    # NJ new field for place tpyes derived from possession names
    place_types = models.ManyToManyField('PlaceType', blank=True)
    # orderno = models.IntegerField(null=True, blank=True,
    # verbose_name="ordering",)
    # lft = models.IntegerField(null=True, blank=True, verbose_name="lft?",)
    # rgt = models.IntegerField(null=True, blank=True, verbose_name="rgt?",)
    notes = models.TextField(null=True, blank=True, verbose_name="notes", )
    util_topancestor = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="root ancestor - utility field", )
    helper_name = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="helper name used for diplay purposes", )
    helper_keywordsearch = models.TextField(
        verbose_name="Field for the keyword search",
        null=True, blank=True, )
    geom = PointField(null=True, blank=True)
    objects = GeoManager()

    @models.permalink
    def get_absolute_url(self):
        return ('place_detail', [str(self.id)])

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_place_change', args=(self.id,))

    get_admin_url.allow_tags = True

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        if EXTRA_SAVING_ACTIONS:
            super(Place, self).save(
                force_insert, force_update)  # Call the "real" save() method.
            name = self.get_root().name
            self.util_topancestor = name
            self = create_helperKeywordsearch(self)
        super(Place, self).save(
            force_insert, force_update)  # Call the "real" save() method.

    # NJ this is a function to replace the invalid relationship
    # specified by the helper_places / helper_factoid m2m
    # relationship
    def assoc_factoids(self):
        ret = []
        # Original simply associated factoids
        for x in (Factoid.objects.filter(
                poss_lands__possessionnew_ptr__place__id=self.id).all()):
            ret.append(x)
        # complex associations
        for x in Factoid.objects.filter(
                assocfactoidprivileges__privilege__place__id=self.id):
            if x not in ret:
                ret.append(x)
        for x in Factoid.objects.filter(
                assocfactoidposs_alms__poss_alms__place__id=self.id):
            if x not in ret:
                ret.append(x)
        for x in Factoid.objects.filter(
                assocfactoidposs_lands__poss_land__place__id=self.id):
            if x not in ret:
                ret.append(x)
        for x in Factoid.objects.filter(
                assocfactoidposs_objects__poss_object__place__id=self.id):
            if x not in ret:
                ret.append(x)
        for x in Factoid.objects.filter(
                assocfactoidposs_revenuesilver__poss_revsilver__place__id=self.id):  # noqa
            if x not in ret:
                ret.append(x)
        for x in Factoid.objects.filter(
                assocfactoidposs_revenuekind__poss_revkind__place__id=self.id):
            if x not in ret:
                ret.append(x)
        for x in Factoid.objects.filter(
                assocfactoidposs_pgeneral__poss_pgeneral__place__id=self.id):
            if x not in ret:
                ret.append(x)
        for x in Factoid.objects.filter(poss_office__place__id=self.id):
            if x not in ret:
                ret.append(x)
        for x in Factoid.objects.filter(
                assocfactoidposs_unfreep__poss_unfree_persons__place__id=self.id):  # noqa
            if x not in ret:
                ret.append(x)

        # return f.distinct()
        return ret

    # =========>>>>>>> the FEINCMS admin!!!!!!!!!!!!!!!!!
    class Admin(AutocompleteTreeEditor):
        # list_display = ('possname',)

        def save_model(self, request, obj, form, change):
            """adds the user information when the rec is saved"""
            if getattr(obj, 'created_by', None) is None:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()

        #  extending TreeAdmin's _actions_column

        def _actions_column(self, page):
            actions = super(Place.Admin, self)._actions_column(page)
            actions.insert(0,
                           u'<a href="add/?parent=%s" title="%s">\
                            <img src="%simg/admin/icon_addlink.gif" '
                           u'alt="%s"></a>' % (
                               page.pk, _('Add child page'),
                               settings.ADMIN_MEDIA_PREFIX,
                               _('Add child page')))
            return actions

        list_display = (
            'name', 'id', 'parent', 'editedrecord', 'review', 'updated_by',
            'updated_at',)
        list_filter = ['updated_at', 'created_by__username',
                       'editedrecord', 'review', 'util_topancestor']
        search_fields = ['id', 'name']
        related_search_fields = {'parent': ('name',), }
        filter_horizontal = ['place_types', ]
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
              ['name', 'genericname', 'articletext',
               'specificname', 'parent', 'notes', 'place_types']
              }),
            ('Geographic',
             {'fields':
              ['geom', ]
              })
        ]

        class Media:
            js = ('/media/static/js/leaflet.js',
                  '/media/static/js/admin_fixes/add_leaflet_field.js')
            css = {
                'all': ('/media/static/css/add_leaflet_field.css',
                        '/media/static/js/leaflet.css'),
            }

    def get_children_by_name(self):
        return sorted(self.get_children(), key=lambda x: x.name)

    def __nameandparent__(self):
        exit = ""
        if self.parent:
            p = self.parent
            exit = "%s>>" % (blank_or_string(p.name))
            # we just go down two levels
            if p.parent:
                exit = "%s>>%s" % (blank_or_string(p.name), exit)
        exit += blank_or_string(self.name)
        return exit

    def show_ancestors_tree(self):
        exit = ""
        for el in self.get_ancestors():
            exit += "%s>>>" % (blank_or_string(el.name))
        exit += blank_or_string(self.name)
        return exit

    def __str__(self):
        return self.__nameandparent__()

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name_plural = "Places"
        ordering = ['tree_id', 'lft', 'name', ]

    table_order = 16


mptt.register(Place, )


# =============================================================================
#  SIGNALS; removed on 2012-06-18 as the save() action addressed the same issue
# =============================================================================

#
# from django.db.models.signals import post_save
#
# for FactPossession, FactRelationship, FactTitle
# def handler_for_factoids(sender, instance, created, **kwargs):
# added 11-Nov-09 to manage the inferred_type field
#   if not instance.inferred_type and EXTRA_SAVING_ACTIONS:
#       try:
#           if instance.get_right_subclass()[0]:
#               instance.inferred_type = instance.get_right_subclass()[0]
#       except:
#           instance.inferred_type = ""
#       instance.save()
#
#
# for FactTransaction only
# def handler_for_transactionfactoids(sender, instance, created, **kwargs):
# added 11-Nov-09 to manage the inferred_type field
#   if not instance.inferred_type and EXTRA_SAVING_ACTIONS:
#       try:
#           if instance.get_right_subclass()[0]:
#               instance.inferred_type = instance.get_right_subclass()[0]
#       except:
#           instance.inferred_type = ""
#       instance.save()
# added 18/1/10 to create Person floruits inference mechanism
# automatic creation of Person floruits
# valid_roles = ['Grantor', 'Beneficiary', 'Addressor', 'Addressee',
# 'Party 1', 'Party 2', 'Party 3', 'Consentor',
# 'Dated by hand of', 'Inspector', 'Scribe', 'Sealer', 'Signatory',
# Witness']
# if instance.isprimary == True and  instance.eitheror == False and
# instance.undated == False:
# print("FLORUITS: found a primary transaction with from-date=[%s]
# to-date=[%s]" % (str(instance.from_year),
# str(instance.to_year)))
# for x in instance.assocfactoidwitness_set.all():
# print("FLORUITS: found a witness..")
# person = build_floruits(x.person, x.has_firmdate, instance.from_year,
# instance.to_year)
# for x in instance.assocfactoidperson_set.all():
# if x.role:
# if x.role.name in valid_roles:
# print("FLORUITS: found associated person with valid role.. *%s*" %
# (x.role.name))
# person = build_floruits(x.person, instance.has_firmdate,
# instance.from_year, instance.to_year)
# pass
#
#
#
# if I add it for 'factoid' it interferes with the others!
# post_save.connect(my_handler_for_inferred_factoid_type, sender=Factoid)
# post_save.connect(handler_for_transactionfactoids, sender=FactTransaction)
# post_save.connect(handler_for_factoids, sender=FactPossession)
# post_save.connect(handler_for_factoids, sender=FactRelationship)
# post_save.connect(handler_for_factoids, sender=FactReference)
# post_save.connect(handler_for_factoids, sender=FactTitle)
#
#
