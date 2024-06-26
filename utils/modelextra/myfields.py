"""
Django Extensions additional model fields
"""

#import datetime
from django.utils import timezone
import re
from django.db.models import DateTimeField, SlugField
from django.template.defaultfilters import slugify
from django.utils import timezone

try:
    import uuid
except ImportError:
    from django_extensions.utils import uuid  # noqa

# todo removed
# from south.modelsinspector import add_introspection_rules


class CreationDateTimeField(DateTimeField):
    """ CreationDateTimeField

    By default, sets editable=True, blank=True, default=datetime.now
    """

    def __init__(self, *args, **kwargs):
        now = timezone.now()
        kwargs.setdefault('editable', True)
        kwargs.setdefault('blank', True)
        kwargs.setdefault('blank', True)
        kwargs.setdefault('default', timezone.now())
        DateTimeField.__init__(self, *args, **kwargs)

    def get_internal_type(self):
        return "DateTimeField"


class ModificationDateTimeField(CreationDateTimeField):
    """ ModificationDateTimeField

    By default, sets editable=True, blank=True, default=datetime.now

    Sets value to datetime.now() on each save of the model.
    """

    def pre_save(self, model, add):
        value = timezone.now()
        setattr(model, self.attname, value)
        return value

    def get_internal_type(self):
        return "DateTimeField"


class AutoSlugField(SlugField):
    """ AutoSlugField

    By default, sets editable=False, blank=True.

    Required arguments:

    populate_from
        Specifies which field the slug is populated from.

    Optional arguments:

    separator
        Defines the used separator (default: '-')

    overwrite
        If set to True, overwrites the slug on every save (default: False)

    Inspired by SmileyChris' Unique Slugify snippet:
    http://www.djangosnippets.org/snippets/690/
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('blank', True)
        kwargs.setdefault('editable', False)

        populate_from = kwargs.pop('populate_from', None)
        if populate_from is None:
            raise ValueError("missing 'populate_from' argument")
        else:
            self._populate_from = populate_from
        self.separator = kwargs.pop('separator', u'-')
        self.overwrite = kwargs.pop('overwrite', False)
        super(AutoSlugField, self).__init__(*args, **kwargs)

    def _slug_strip(self, value):
        """
        Cleans up a slug by removing slug separator characters that occur at
        the beginning or end of a slug.

        If an alternate separator is used, it will also replace any instances
        of the default '-' separator with the new separator.
        """
        re_sep = '(?:-|%s)' % re.escape(self.separator)
        value = re.sub('%s+' % re_sep, self.separator, value)
        return re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)

    def create_slug(self, model_instance, add):
        # get fields to populate from and slug field to set
        populate_field = model_instance._meta.get_field(self._populate_from)
        slug_field = model_instance._meta.get_field(self.attname)
        if add or self.overwrite:
            # slugify the original field content and set next step to 2
            slug = slugify(getattr(model_instance, populate_field.attname))
            next = 2
        else:
            # get slug from the current model instance and calculate next
            # step from its number, clean-up
            slug = self._slug_strip(getattr(model_instance, self.attname))
            next = slug.split(self.separator)[-1]
            if next.isdigit():
                slug = self.separator.join(slug.split(self.separator)[:-1])
                next = int(next)
            else:
                next = 2

        # strip slug depending on max_length attribute of the slug field
        # and clean-up
        slug_len = slug_field.max_length
        if slug_len:
            slug = slug[:slug_len]
        slug = self._slug_strip(slug)
        original_slug = slug

        # exclude the current model instance from the queryset used in finding
        # the next valid slug
        queryset = model_instance.__class__._default_manager.all()
        if model_instance.pk:
            queryset = queryset.exclude(pk=model_instance.pk)

        # increases the number while searching for the next valid slug
        # depending on the given slug, clean-up
        while not slug or queryset.filter(**{self.attname: slug}):
            slug = original_slug
            end = '%s%s' % (self.separator, next)
            end_len = len(end)
            if slug_len and len(slug) + end_len > slug_len:
                slug = slug[:slug_len - end_len]
                slug = self._slug_strip(slug)
            slug = '%s%s' % (slug, end)
            next += 1
        return slug

    def pre_save(self, model_instance, add):
        value = self.create_slug(model_instance, add)
        setattr(model_instance, self.attname, value)
        return value

    def get_internal_type(self):
        return "SlugField"


#  NOT USED


# class UUIDVersionError(Exception):
#     pass

# class UUIDField(CharField):
#     """ UUIDField
#
#     By default uses UUID version 1 (generate from
# host ID, sequence number and current time)
#
#     The field support all uuid versions which are
# natively supported by the uuid python module.
#     For more information see: http://docs.python.org/lib/module-uuid.html
#     """
#
#     def __init__(self, verbose_name=None, name=None,
# auto=True, version=1, node=None, clock_seq=None,
# namespace=None, **kwargs):
#         kwargs['max_length'] = 36
#         if auto:
#             kwargs['blank'] = True
#             kwargs.setdefault('editable', False)
#         self.auto = auto
#         self.version = version
#         if version==1:
#             self.node, self.clock_seq = node, clock_seq
#         elif version==3 or version==5:
#             self.namespace, self.name = namespace, name
#         CharField.__init__(self, verbose_name, name, **kwargs)
#
#     def get_internal_type(self):
#         return CharField.__name__
#
#     def create_uuid(self):
#         if not self.version or self.version==4:
#             return uuid.uuid4()
#         elif self.version==1:
#             return uuid.uuid1(self.node, self.clock_seq)
#         elif self.version==2:
#             raise UUIDVersionError("UUID version 2 is not supported.")
#         elif self.version==3:
#             return uuid.uuid3(self.namespace, self.name)
#         elif self.version==5:
#             return uuid.uuid5(self.namespace, self.name)
#         else:
#             raise UUIDVersionError("UUID version %s is not
# valid." % self.version)
#
#     def pre_save(self, model_instance, add):
#         if self.auto and add:
#             value = unicode(self.create_uuid())
#             setattr(model_instance, self.attname, value)
#             return value
#         else:
#             value = super(UUIDField, self).pre_save(model_instance, add)
#             if self.auto and not value:
#                 value = unicode(self.create_uuid())
#                 setattr(model_instance, self.attname, value)
#         return value
