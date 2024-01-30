from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from kdl_ldap.signal_handlers import \
    register_signal_handlers as kdl_ldap_register_signal_hadlers
from pomsapp.views import admin_overview
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from utils.adminextra import poms_custom_admin_views
import pomsapp.views_family as views_family


kdl_ldap_register_signal_hadlers()

admin.autodiscover()

prefix = ""

urlpatterns = [
    url(r'^accounts/', include('registration.backends.model_activation.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^' + prefix + 'admin/(pomsapp/)$', poms_custom_admin_views.pomsapp),
    url(r'^' + prefix + 'admin/created_possplaces/$',
        poms_custom_admin_views.created_possplaces, name='created_possplaces'),
    url(r'^' + prefix + 'admin/missing_possplaces/$',
        poms_custom_admin_views.missing_possplaces, name='missing_possplaces'),
    url(r'^' + prefix + 'admin/created_docplaces/$',
        poms_custom_admin_views.created_docplaces, name='created_docplaces'),
    url(r'^' + prefix + 'admin/missing_docplaces/$',
        poms_custom_admin_views.missing_docplaces, name='missing_docplaces'),
    url(r'^' + prefix + 'admin/unmarked_factoids/$',
        poms_custom_admin_views.unmarked_factoids, name='unmarked_factoids'),
    url(r'^' + prefix + 'admin/orphan_titles/$',
        poms_custom_admin_views.orphan_titles, name='orphan_titles'),
    url(r'^' + prefix + 'admin/orphan_places/$',
        poms_custom_admin_views.orphan_places, name='orphan_places'),
    url(r'^' + prefix + 'admin/orphan_people/$',
        poms_custom_admin_views.orphan_people, name='orphan_people'),
    url(r'^' + prefix + 'admin/orphan_possessions/$',
        poms_custom_admin_views.orphan_possessions, name='orphan_possessions'),
    url(r'^' + prefix + 'admin/charterscirca/$',
        poms_custom_admin_views.charterscirca, name='charters_circa'),
    url(r'^' + prefix + 'admin/previous_landholder/$',
        poms_custom_admin_views.previous_landholder,
        name='previous_landholders'),
    url(r'^' + prefix + 'admin/contributions/$',
        poms_custom_admin_views.contributions, name='contributions'),
    url(r'^admin/', admin.site.urls),

    # REGISTRATION:  TESTING
    url(r'^' + prefix + 'accounts/', include('registration.urls')),
    url(r'^' + prefix + 'overview/', admin_overview),
    url(r'^' + prefix + 'record/', include('pomsapp.urls_record')),
    url(r'^' + prefix + 'search/', include('pomsapp.urls_browse')),
    # url(r'^' + prefix + 'familytrees/', include('pomsapp.urls_family')),
    url(r'^' + prefix + 'information/familytrees/$',
        views_family.familytrees, name='familytrees'),
    url(r'^' + prefix + 'information/familytrees/(?P<image_id>\d+)/$',
        views_family.familytrees, name='familytrees'),
    url(r'^' + prefix + 'map/', include('pomsapp.urls_map')),
    url(r'^' + prefix + 'sna/', include('sna.urls')),
    # todo removed for now
    # url(r'^' + prefix + 'labs/', include('labsapp.urls')),
    url(r'^select2/', include('django_select2.urls')),

    url(r'^wagtail/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'', include(wagtail_urls)),
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
