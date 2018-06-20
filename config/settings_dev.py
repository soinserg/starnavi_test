from .settings_common import *

SECRET_KEY = '8wms8dqa4vjl#+dhr!zgeu)c^)+j2#=qiood-nc+spaowvp0*5'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'starnavi_test',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
