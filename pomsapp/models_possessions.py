from django.db import models
from utils.myutils import blank_or_string
import utils.modelextra.mymodels as mymodels
import mptt


#########################
# POSSESSIONS and PRIVILEGES
#########################

# NEWWWWWW *****************

# 2010-11-12: added the helper_name field, although we still dont use it!
class Privileges(mymodels.PomsModel):
    """(Privileges : TODO: we'll have to create
    adequate subclasses also here....)"""
    name = models.CharField(max_length=765, null=True,
                            blank=True, verbose_name="name",)
    nameextension = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="name extension",)
    notes = models.TextField(null=True, blank=True,
                             verbose_name="notes",)
    parent = models.ForeignKey('self', null=True, blank=True,
                               verbose_name="parent",
                               related_name='children')
    extraid = models.IntegerField(
        null=True, blank=True, verbose_name="useful unused field",)
    place = models.ForeignKey(
        'Place', null=True, blank=True,
        verbose_name="related place (not used)",)
    util_topancestor = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="root ancestor - utility field",)
    helper_name = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="helper name used for diplay purposes",)

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        # Call the "real" save() method.
        super(Privileges, self).save(force_insert, force_update)
        name = self.get_root().name
        self.util_topancestor = name
        # Call the "real" save() method.
        super(Privileges, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Privileges"
        ordering = ['tree_id', 'lft', 'name', ]

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

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_privileges_change', args=(self.id,))
        # return "/%sadmin/pomsapp/person/%s" % (django_settings.URL_PREFIX,
        # self.id)
    get_admin_url.allow_tags = True

    def __unicode__(self):
        return self.__nameandparent__()
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 3

    def __str__(self):
        return self.__unicode__()


# doesn't appear in the admin!
# 2010-11-12: added the helper_name field, although we still dont use it!
class PossessionNew(mymodels.PomsModel):
    """Superclass of all the possessions. We don't register it with
    MPTT as we do that with its subclasses"""
    name = models.CharField(max_length=765, null=True,
                            blank=True, verbose_name="name",)
    nameextension = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="name extension",)
    extraid = models.IntegerField(
        null=True, blank=True, verbose_name="useful unused field",)
    place = models.ForeignKey(
        'Place', null=True, blank=True, verbose_name="related place",)
    notes = models.TextField(null=True, blank=True,
                             verbose_name="notes",)
    util_topancestor = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="root ancestor - utility field",)
    helper_name = models.CharField(
        max_length=765, null=True, blank=True,
        verbose_name="helper name used for diplay purposes",)

    table_group = 'Possessions & Privileges [in progress]'
    table_order = 2

    class Meta:
        verbose_name_plural = "Possessions"

    # these TWO methods wouldn't work on this class - I just put it here so
    # that it's inherited
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
    # 10 NOV: testing the dynamic properties behaviour => doesn't work with
    # autocomplete!! damn
    name_and_parent = property(__nameandparent__)

    def show_ancestors_tree(self):
        exit = ""
        for el in self.get_ancestors():
            exit += "%s>>>" % (blank_or_string(el.name))
        exit += blank_or_string(self.name)
        return exit

    def get_right_subclass(self):
        # once you get a possessionNew instance, it's useful to know quickly
        # what subclass it is...
        try:
            sbcls = ["Poss_Alms", self.poss_alms]
        except BaseException:
            try:
                sbcls = ["Poss_Lands", self.poss_lands]
            except BaseException:
                try:
                    sbcls = ["Poss_Objects", self.poss_objects]
                except BaseException:
                    try:
                        sbcls = ["Poss_Revenues_silver",
                                 self.poss_revenues_silver]
                    except BaseException:
                        try:
                            sbcls = ["Poss_Revenues_kind",
                                     self.poss_revenues_kind]
                        except BaseException:
                            try:
                                sbcls = ["Poss_General", self.poss_general]
                            except BaseException:
                                try:
                                    sbcls = ["Poss_Office", self.poss_office]
                                except BaseException:
                                    try:
                                        sbcls = ["Poss_Unfree_persons",
                                                 self.poss_unfree_persons]
                                    except BaseException:
                                        sbcls = None
        return sbcls
    get_right_subclass.allow_tags = True

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Poss_Alms(PossessionNew):
    """(Poss Alms description)"""
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        # Call the "real" save() method.
        super(Poss_Alms, self).save(force_insert, force_update)
        name = self.get_root().name
        self.util_topancestor = name
        # Call the "real" save() method.
        super(Poss_Alms, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Alms"
        ordering = ['tree_id', 'lft', ]

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_poss_alms_change', args=(self.id,))
    get_admin_url.allow_tags = True

    def __unicode__(self):
        return self.__nameandparent__()

    def __str__(self):
        return self.__unicode__()
        # return self.show_ancestors_tree()
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 4


class Poss_Lands(PossessionNew):
    """(Lands description)"""
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        # Call the "real" save() method.
        super(Poss_Lands, self).save(force_insert, force_update)
        name = self.get_root().name
        self.util_topancestor = name
        # Call the "real" save() method.
        super(Poss_Lands, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Lands"
        ordering = ['tree_id', 'lft']

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_poss_lands_change', args=(self.id,))
    get_admin_url.allow_tags = True

    def __unicode__(self):
        return self.__nameandparent__()

    def __str__(self):
        return self.__unicode__()
        # return self.show_ancestors_tree()
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 5


class Poss_Objects(PossessionNew):
    """(Objects description)"""
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        # Call the "real" save() method.
        super(Poss_Objects, self).save(force_insert, force_update)
        name = self.get_root().name
        self.util_topancestor = name
        # Call the "real" save() method.
        super(Poss_Objects, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Objects"
        ordering = ['tree_id', 'lft']

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_poss_objects_change', args=(self.id,))
    get_admin_url.allow_tags = True

    def __unicode__(self):
        return self.__nameandparent__()
        # return self.show_ancestors_tree()

    def __str__(self):
        return self.__unicode__()
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 6


class Poss_Revenues_silver(PossessionNew):
    """(Revenues in silver description)"""
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        # Call the "real" save() method.
        super(Poss_Revenues_silver, self).save(force_insert, force_update)
        name = self.get_root().name
        self.util_topancestor = name
        # Call the "real" save() method.
        super(Poss_Revenues_silver, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Revenues in silver"
        ordering = ['tree_id', 'lft']

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_poss_revenues_silver_change', args=(self.id,))
    get_admin_url.allow_tags = True

    def __unicode__(self):
        return self.__nameandparent__()

    def __str__(self):
        return self.__unicode__()
        # return self.show_ancestors_tree()
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 7


class Poss_Revenues_kind(PossessionNew):
    """(Lands description)"""
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        # Call the "real" save() method.
        super(Poss_Revenues_kind, self).save(force_insert, force_update)
        name = self.get_root().name
        self.util_topancestor = name
        # Call the "real" save() method.
        super(Poss_Revenues_kind, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Revenues in kind"
        ordering = ['tree_id', 'lft']

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_poss_revenues_kind_change', args=(self.id,))
    get_admin_url.allow_tags = True

    def __unicode__(self):
        return self.__nameandparent__()

    def __str__(self):
        return self.__unicode__()
        # return self.show_ancestors_tree()
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 8


class Poss_General(PossessionNew):
    """(Lands description)"""
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        # Call the "real" save() method.
        super(Poss_General, self).save(force_insert, force_update)
        name = self.get_root().name
        self.util_topancestor = name
        # Call the "real" save() method.
        super(Poss_General, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Possession general"
        ordering = ['tree_id', 'lft']

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_poss_general_change', args=(self.id,))
    get_admin_url.allow_tags = True

    def __unicode__(self):
        return self.__nameandparent__()
        # return self.show_ancestors_tree()
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 9

    def __str__(self):
        return self.__unicode__()


class Poss_Office(PossessionNew):
    """(Lands description)"""
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        # Call the "real" save() method.
        super(Poss_Office, self).save(force_insert, force_update)
        name = self.get_root().name
        self.util_topancestor = name
        # Call the "real" save() method.
        super(Poss_Office, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Office"
        ordering = ['tree_id', 'lft']

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_poss_office_change', args=(self.id,))
    get_admin_url.allow_tags = True

    def __unicode__(self):
        return self.__nameandparent__()
        # return self.show_ancestors_tree()
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 10

    def __str__(self):
        return self.__unicode__()


class Poss_Unfree_persons(PossessionNew):
    """(Lands description)"""
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    def save(self, force_insert=False, force_update=False):
        # create the util_topancestor field
        # Call the "real" save() method.
        super(Poss_Unfree_persons, self).save(force_insert, force_update)
        name = self.get_root().name
        self.util_topancestor = name
        # Call the "real" save() method.
        super(Poss_Unfree_persons, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Unfree persons"
        ordering = ['tree_id', 'lft']

    def get_admin_url(self):
        from django.core import urlresolvers
        return urlresolvers.reverse(
            'admin:pomsapp_poss_unfree_persons_change', args=(self.id,))
    get_admin_url.allow_tags = True

    def __unicode__(self):
        return self.__nameandparent__()
        # return self.show_ancestors_tree()
    table_group = 'Possessions & Privileges [in progress]'
    table_order = 11

    def __str__(self):
        return self.__unicode__()


mptt.register(Poss_Alms,)
mptt.register(Poss_Unfree_persons,)
mptt.register(Poss_Revenues_silver,)
mptt.register(Poss_Revenues_kind,)
mptt.register(Poss_General,)
mptt.register(Poss_Office,)
mptt.register(Poss_Objects,)
mptt.register(Poss_Lands,)
mptt.register(Privileges, )  # order_insertion_by='name'
