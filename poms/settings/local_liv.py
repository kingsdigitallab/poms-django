from .base import *  # noqa

ALLOWED_HOSTS = ['poms.kdl.kcl.ac.uk','poms-os.kdl.kcl.ac.uk', 'poms.app.cch.kcl.ac.uk']

SECRET_KEY = '@*@£$%(@RRfsdg3%wer£$%^^GASEGBBDFRRasa5'

INTERNAL_IPS = ['0.0.0.0', '127.0.0.1', '::1', '10.0.2.2']


DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': 'app_poms_stg',
        'USER': 'app_poms',
        'PASSWORD': 'app_poms',
        'HOST': 'db',
        'STORAGE_ENGINE': 'INNODB'
    },
}

