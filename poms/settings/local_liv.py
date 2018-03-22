from .base import *  # noqa

ALLOWED_HOSTS = ['poms.kdl.kcl.ac.uk']

INTERNAL_IPS = INTERNAL_IPS + ['']

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': 'app_poms_liv',
        'USER': 'app_poms',
        'PASSWORD': '',
        'HOST': ''
    },
}

SECRET_KEY = ''
