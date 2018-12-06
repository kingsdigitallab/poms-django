#
#     Autocomplete feature for admin panel
#
#     Most of the code has been written by Jannis Leidel, then updated a bit
#     for django_extensions, finally reassembled and extended by Mikele Pasin.
#
#     http://jannisleidel.com/2008/11/autocomplete-form-widget-foreignkey-model-fields/
#    http://code.google.com/p/django-command-extensions/
#    http://magicrebirth.wordpress.com/
#
#     to_string_function, Satchmo adaptation and some comments added by emes
#     (Michal Salaban)
#


#  ==============
#  HOW-TO
#  ==============

# 1.Put this file somewhere in your application folder

# 2.Add the 'autocomplete' folder with the media files to your usual media
# folder

# 3.Add the 'admin/autocomplete' folder to your templates folder

# 4.Add the extrafilters.py file in the templatetags directory
# of your application (or just add its contents to
#   your custom template tags if you already have some).
# All is needed is the 'cut' filter, for making the code used in the
# inline-autocomplete form javascript friendly

# 5. When defining your models admin, import the relevant admin and use it:
#  .....
# from myproject.mypackage.autocomplete_admin import FkAutocompleteAdmin
#  .....
#  .....
# class Admin (FkAutocompleteAdmin):
# 	related_search_fields = { 'person': ('name',)}
#  .....


#  ==============
# TROUBLE SHOOTING:
#  ==============

# ** sometimes things don't work cause you have to add
# 'from django.conf.urls.defaults import *' to the modules where
#  you use the autocomplete
# ** if you're using the inline-autocompletion, make sure that
# the main admin class the inline belong to is a
# subclass FkAutocompleteAdmin
# ** you may need to hack it a bit to make it work for you -
# it's been done in a rush!


#  ==============
# the code now....
#  ==============

import functools
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.apps import apps
# remove deprecated - now -dead method
# from django.utils.text import truncate_words
from django.utils.text import Truncator
from django.template.loader import render_to_string
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
import operator
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import admin
from django.db import models
from django.db.models.query import QuerySet
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _
from django.utils.text import get_text_list
# added by mikele
# from django.conf.urls.defaults import *
from django.conf.urls import url
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from six.moves import reduce
import six





# ===========
# MPTT TREE + AUTOCOMPLETE
# using the autocomplete admin with other custom admin classes: just
# mix and match as you like....
#  e.g. in my case I used it with the admin for trees provided by FeinCms:


try:
    from utils.mpttextra import feincms_tree_editor

    #  just merging the effects of the two classes..
    class AutocompleteTreeEditor(
        ForeignKeyAutocompleteAdmin, feincms_tree_editor.TreeEditor):
        def __init__(self, *args, **kwargs):
            super(AutocompleteTreeEditor, self).__init__(*args, **kwargs)
except ImportError:
    raise Exception("Could not load feincms_tree_editor.........")
