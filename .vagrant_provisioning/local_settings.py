from .base import *  # noqa

DEBUG = True

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': 'poms',
        'USER': 'app_poms',
        'PASSWORD': 'app_poms',
        'ADMINUSER': 'postgres',
        'HOST': 'localhost'
    },
}

# 10.0.2.2 is the default IP for the VirtualBox Host machine
INTERNAL_IPS = ['0.0.0.0', '127.0.0.1', '::1', '10.0.2.2']

SECRET_KEY = '12345'

FABRIC_USER = ''

# -----------------------------------------------------------------------------
# Django Debug Toolbar
# http://django-debug-toolbar.readthedocs.org/en/latest/
# -----------------------------------------------------------------------------

try:
    import debug_toolbar  # noqa

    INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar']
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware']
    DEBUG_TOOLBAR_PATCH_SETTINGS = True
except ImportError:
    pass

LOGGING['loggers']['poms'] = {}
LOGGING['loggers']['poms']['handlers'] = ['console']
LOGGING['loggers']['poms']['level'] = logging.DEBUG
