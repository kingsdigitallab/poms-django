from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from kdl_ldap.signal_handlers import \
    register_signal_handlers as kdl_ldap_register_signal_hadlers
from pomsapp.views import admin_overview

from utils.adminextra import poms_custom_admin_views

kdl_ldap_register_signal_hadlers()
# from wagtail.wagtailadmin import urls as wagtailadmin_urls
# from wagtail.wagtailcore import urls as wagtail_urls
# from wagtail.wagtaildocs import urls as wagtaildocs_urls


"""
OLD URLS FILE, WILL BE REMOVED AS UPDATED AND ADDED

from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to, direct_to_template

from django.conf import settings
try:
	prefix = settings.URL_PREFIX
except:
	prefix = ""

urlpatterns = patterns('',)	 # setting up


if not settings.LIVE_SERVER:
	from django.contrib import admin
	admin.autodiscover()
	from utils.adminextra import poms_custom_admin_views
	

	urlpatterns += patterns('', 
		
		# standard admin urls	
		url(r'^'+prefix+'admin/', include(admin.site.urls) ),	# <=== NEW SYNTAX				 
		# urlurl(r'^'+prefix+'admin/(.*)', admin.site.root, name='adminroot'),
		url	

		)




# 2012-10-09
# I had to split up the urls for STG, since there the system is still set up to work under the /db prefix
# After the live site has been moved onto a subdomain, all the code has been updated accordingly (so /db isn't needed 
anymore)
# ps: LABS and DJFACET are *not* available on STG, because data entry site and db are not optimized for them

if not settings.STAGE_SERVER:
	urlpatterns += patterns('',
		# home dir is a redirect
		url(r'^'+prefix+'$', redirect_to, {'url': '/search/'}),
		url(r'^'+prefix+'record/',		   include('pomsapp.urls_record')),
		url(r'^'+prefix+'search/',		   include('pomsapp.urls_search')),
		url(r'^'+prefix+'familytrees/',		include('pomsapp.urls_family')),
		url(r'^'+prefix+'map/',		include('pomsapp.urls_map')),
        url(r'^'+prefix+'sna/',            include('sna.urls')),
		url(r'^'+prefix+'labs/', include('labsapp.urls')),
		urlurl(r'^'+prefix+'browse/', include('djfacet.urls')),		
		(r'^robots\.txt$', direct_to_template,
		     {'template': 'robots.txt', 'mimetype': 'text/plain'}),
		)
	from django.contrib import admin
	admin.autodiscover()
	from utils.adminextra import poms_custom_admin_views
	from pomsapp.databrowse_load import *
	from pomsapp.views import admin_overview

	urlpatterns += patterns('', 
		# a customized view for the application admin home					   
		url(r'^'+prefix+'admin/(pomsapp/)$', poms_custom_admin_views.pomsapp), 
		url(r'^'+prefix+'admin/created_possplaces/$', poms_custom_admin_views.created_possplaces),
		url(r'^'+prefix+'admin/missing_possplaces/$', poms_custom_admin_views.missing_possplaces),
		url(r'^'+prefix+'admin/created_docplaces/$', poms_custom_admin_views.created_docplaces),
		url(r'^'+prefix+'admin/missing_docplaces/$', poms_custom_admin_views.missing_docplaces),
		url(r'^'+prefix+'admin/unmarked_factoids/$', poms_custom_admin_views.unmarked_factoids),
		url(r'^'+prefix+'admin/unmarked_factoids/$', poms_custom_admin_views.unmarked_factoids),
		url(r'^'+prefix+'admin/orphan_titles/$', poms_custom_admin_views.orphan_titles),
		url(r'^'+prefix+'admin/orphan_places/$', poms_custom_admin_views.orphan_places),
		url(r'^'+prefix+'admin/orphan_people/$', poms_custom_admin_views.orphan_people),
		url(r'^'+prefix+'admin/orphan_possessions/$', poms_custom_admin_views.orphan_possessions),
		url(r'^'+prefix+'admin/charterscirca/$', poms_custom_admin_views.charterscirca),
		url(r'^'+prefix+'admin/previous_landholder/$', poms_custom_admin_views.previous_landholder),
		url(r'^'+prefix+'admin/contributions/$', poms_custom_admin_views.contributions),
		# standard admin urls	
		url(r'^'+prefix+'admin/', include(admin.site.urls) ),	# <=== NEW SYNTAX				 
		# urlurl(r'^'+prefix+'admin/(.*)', admin.site.root, name='adminroot'),
		urlurl(r'^'+prefix+'databrowse/(.*)', databrowse.site.root, name='databrowsehome'),
		
		# 2012-01-13: HELPDESK app
		url(r'^'+prefix+'helpdesk/', include('helpdesk.urls')),
		
		# REGISTRATION:  TESTING
		url(r'^'+prefix+'accounts/', include('registration.urls')),
	)	        
        
        
else:
	urlpatterns += patterns('',
		url(r'^'+prefix+'$', redirect_to, {'url': '/search/'}),
		#url(r'^'+prefix+'$', redirect_to, {'url': '/search/'}),		
		url(r'^'+prefix+'record/',		   include('pomsapp.urls_record')),
		url(r'^'+prefix+'search/',		   include('pomsapp.urls_search')),
		url(r'^'+prefix+'familytrees/',		include('pomsapp.urls_family')),
		url(r'^'+prefix+'map/',            include('pomsapp.urls_map')),
        url(r'^'+prefix+'sna/',            include('sna.urls')),
		# Start Neil screwing things he doesn't fully comprehend
        url(r'^'+prefix+'labs/', include('labsapp.urls')),
        urlurl(r'^'+prefix+'browse/', include('djfacet.urls')),
        (r'^robots\.txt$', direct_to_template,
                     {'template': 'robots.txt', 'mimetype': 'text/plain'}),
        )
		# End of Neil screwing
		#(Bar the comments below!)


		#url(r'^'+prefix+'labs/', redirect_to, {'url': '/db/search/'}),
		#urlurl(r'^'+prefix+'browse/', redirect_to, {'url': '/db/search/'}),
		#) 







if settings.LOCAL_SERVER:	   # === > unstable stuff, available on demand..
	urlpatterns += patterns('', 
		url(r'^'+prefix+'accounts/', include('registration.backends.default.urls')),					
		url(r'^'+prefix+'test/peoplerobbie', 'pomsapp.scripts.peoplerobbie.index' ),
		url(r'^'+prefix+'test/index', 'pomsapp.scripts.test.index' ),
		url(r'^'+prefix+'test/dosomething', 'pomsapp.scripts.test.dosomething' ),		
				

	)




if settings.LOCAL_SERVER:     # ===> static files on local machine
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        (r'^media/uploads/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        )




"""

admin.autodiscover()

# url(r'^wagtail/', include(wagtailadmin_urls)),
#     url(r'^documents/', include(wagtaildocs_urls)),
# url(r'', include(wagtail_urls)),

# todo assuming this is because of /db/ prefix, will remove
# when wagtail rationalises site
try:
    prefix = settings.URL_PREFIX
except:
    prefix = ""

urlpatterns = [
    url(r'^accounts/', include('registration.backends.model_activation.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # a customized view for the application admin home
    url(r'^' + prefix + 'admin/(pomsapp/)$', poms_custom_admin_views.pomsapp),
    url(r'^' + prefix + 'admin/created_possplaces/$', poms_custom_admin_views.created_possplaces),
    url(r'^' + prefix + 'admin/missing_possplaces/$', poms_custom_admin_views.missing_possplaces),
    url(r'^' + prefix + 'admin/created_docplaces/$', poms_custom_admin_views.created_docplaces),
    url(r'^' + prefix + 'admin/missing_docplaces/$', poms_custom_admin_views.missing_docplaces),
    url(r'^' + prefix + 'admin/unmarked_factoids/$', poms_custom_admin_views.unmarked_factoids),
    url(r'^' + prefix + 'admin/unmarked_factoids/$', poms_custom_admin_views.unmarked_factoids),
    url(r'^' + prefix + 'admin/orphan_titles/$', poms_custom_admin_views.orphan_titles),
    url(r'^' + prefix + 'admin/orphan_places/$', poms_custom_admin_views.orphan_places),
    url(r'^' + prefix + 'admin/orphan_people/$', poms_custom_admin_views.orphan_people),
    url(r'^' + prefix + 'admin/orphan_possessions/$', poms_custom_admin_views.orphan_possessions),
    url(r'^' + prefix + 'admin/charterscirca/$', poms_custom_admin_views.charterscirca),
    url(r'^' + prefix + 'admin/previous_landholder/$', poms_custom_admin_views.previous_landholder),
    url(r'^' + prefix + 'admin/contributions/$', poms_custom_admin_views.contributions),
    url(r'^admin/', include(admin.site.urls)),

    # REGISTRATION:  TESTING
    url(r'^' + prefix + 'accounts/', include('registration.urls')),
    url(r'^' + prefix + 'overview/', admin_overview),
    url(r'^' + prefix + 'record/', include('pomsapp.urls_record')),
    url(r'^' + prefix + 'search/', include('pomsapp.urls_search')),
    url(r'^' + prefix + 'familytrees/', include('pomsapp.urls_family')),
    url(r'^' + prefix + 'map/', include('pomsapp.urls_map')),
    url(r'^' + prefix + 'sna/', include('sna.urls')),
    # todo removed for now
    # url(r'^' + prefix + 'labs/', include('labsapp.urls')),
    # This replace djfacet with haystack
    url(r'^search/', include('haystack.urls')),

]

# -----------------------------------------------------------------------------
# Django Debug Toolbar URLS
# -----------------------------------------------------------------------------
try:
    if settings.DEBUG:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/',
                include(debug_toolbar.urls)),
        ]
except ImportError:
    pass

# -----------------------------------------------------------------------------
# Static file DEBUGGING
# -----------------------------------------------------------------------------
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import os.path

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/',
                          document_root=os.path.join(settings.MEDIA_ROOT,
                                                     'images'))
