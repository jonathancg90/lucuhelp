import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DOMAIN = 'http://www.lucuhelp.com'

#DATABASE


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'helpdesk',
        'USER': 'postgres',
        'PASSWORD': '',
        },
    }

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)