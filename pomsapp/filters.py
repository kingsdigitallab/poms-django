##################
#
# BM: This appears redundant?
#
#  Mon 11 Apr 2011 15:44:21 BST
#
#  Mikele: I created this hack for not showing as a filter the non-staff
# users:
#
#  in reality, what this does is select only the Users explicitly associated
# to objects, and show them as filters
#  As a side effect, Staff users only are displayed! (cause they're the only
# ones that created objects)
#  Also, staff users that haven't created any objects are not listed!!!
#
#  The code is modeled on 'AllValuesFilterSpec' in contrib/filterspecs.py
#  check also: http://djangosnippets.org/snippets/1051/
#  and http://my.opera.com/curaloucura/blog/2009/02/17/custom-filter-on-
# django-admin
#
#  soon or later we should create a better version of this!

# -----------------------------------------
#  We use it like this:
# -----------------------------------------


#  form thisfile import StaffUsersSpec

# class MyClass(TimeStampedModel):
#
# 	created_by = models.ForeignKey(User, blank=True, null=True)
# 	updated_by = models.ForeignKey(User, blank=True, null=True)
#
# 	created_by.staffusers = True
# 	updated_by.staffusers = True
#
# 	Admin():
# 		list_filter = ('created_by', 'updated_by') ..... etc....

##################


# todo eh removed may be refactored
# class StaffUsersSpec(FilterSpec):
# 	def __init__(self, f, request, params, model, model_admin):
# 		super(StaffUsersSpec, self).__init__(f, request, params, model,
# model_admin)
# 		# print str(f), str(request)
# 		self.lookup_val = request.GET.get(f.name, None)
# 		self.lookup_choices = model_admin.queryset(request).distinct().
# order_by(f.name).values(f.name)
# 		# print "Lookup choices= ", str(self.lookup_choices)
#
# 	def title(self):
# 		return self.field.verbose_name
#
# 	def choices(self, cl):
# 		yield {'selected': self.lookup_val is None,
# 			   'query_string': cl.get_query_string({}, [self.field.name]),
# 			   'display': _('All')}
# 		for d in self.lookup_choices:
# 			val = smart_text(d[self.field.name])
# 			# print str(val)
# 			#  NOTE:  If the val is not None, get the User name for display
# purposese
# 			if d[self.field.name]:
# 				user = User.objects.get(pk=d[self.field.name])
# 				username = user.username
# 			else:
# 				username = val
# 			yield {'selected': self.lookup_val == val,
# 				   'query_string': cl.get_query_string({self.field.name:
# val}),
# 				   'display': username}
#
# FilterSpec.filter_specs.insert(0, (lambda f: getattr(f, 'staffusers',
# False),
# 								   StaffUsersSpec))


#
#
# class StaffUsersSpec(ChoicesFilterSpec):
# def __init__(self, f, request, params, model, model_admin):
# 	super(StaffUsersSpec, self).__init__(f, request, params, model,
# model_admin)
# 	if isinstance(f, models.ManyToManyField):
# 		self.lookup_title = f.rel.to._meta.verbose_name
# 	else:
# 		self.lookup_title = f.verbose_name
# 	rel_name = f.rel.get_related_field().name
# 	self.lookup_kwarg = '%s__%s__exact' % (f.name, rel_name)
# 	self.lookup_val = request.GET.get(self.lookup_kwarg, None)
#
# 	values_list = model.objects.filter(updated_by__is_staff=True).
# svalues_list(f.name, flat=True)
# 	print str(values_list)
# 	# getting the first char of values
# 	# self.lookup_choices = list(set(val[0] for val in values_list if val))
# 	# self.lookup_choices.sort()
# 	# self.lookup_choices = list(set(values_list))
# 	# self.lookup_choices = model.objects.filter(updated_by__is_staff=True)
#
# # ORIGINAL:
# 	self.lookup_choices = f.get_choices(include_blank=False)
#
# def has_output(self):
# 	return len(self.lookup_choices) > 1
#
# def title(self):
# 	return self.lookup_title
#
# def choices(self, cl):
# 	yield {'selected': self.lookup_val is None,
# 		   'query_string': cl.get_query_string({}, [self.lookup_kwarg]),
# 		   'display': _('All')}
# 	for k, v in self.field.flatchoices:
# 		yield {'selected': smart_text(k) == self.lookup_val,
# 				'query_string': cl.get_query_string({self.lookup_kwarg: k}),
# 				'display': v}
#
#
# FilterSpec.filter_specs.insert(0, (lambda f: getattr(f, 'staffusers', False),
# 							   StaffUsersSpec))

#
#
# class AlphabeticSpec(ChoicesFilterSpec):
#   """
#   Adds filtering by ....
#
#   my_model_field.alphabetic_filter = True
#   """
#
#   def __init__(self, f, request, params, model, model_admin):
# 	  super(AlphabeticSpec, self).__init__(f, request, params, model,
# 												 model_admin)
# 	  self.lookup_kwarg = '%s__istartswith' % f.name
# 	  self.lookup_val = request.GET.get(self.lookup_kwarg, None)
# 	  values_list = model.objects.values_list(f.name, flat=True)
# 	  # getting the first char of values
# 	  self.lookup_choices = list(set(val[0] for val in values_list if val))
# 	  self.lookup_choices.sort()
#
#   def choices(self, cl):
# 	  yield {'selected': self.lookup_val is None,
# 			  'query_string': cl.get_query_string({}, [self.lookup_kwarg]),
# 			  'display': _('All')}
# 	  for val in self.lookup_choices:
# 		  yield {'selected': smart_text(val) == self.lookup_val,
# 				  'query_string': cl.get_query_string({self.lookup_kwarg:
# val}),
# 				  'display': val.upper()}
#   def title(self):
# 	  return _('%(field_name)s that starts with') % \
# 		  {'field_name': self.field.verbose_name}
#
# # registering the filter
# FilterSpec.filter_specs.insert(0, (lambda f: getattr(f, 'alphabetic_filter',
# False),
# 								 AlphabeticSpec))
