from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '94.130.99.236'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'golf_db',
        'USER': 'golf',
        'PASSWORD': 'alfyk6Q9yxSj',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
