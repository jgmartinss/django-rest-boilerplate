import os

from .base import *


DEBUG = config('DEBUG', default=False, cast=bool)

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': config('DATABASE_URL', default='sqlite:///db.sqlite3', cast=db_url),
}

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware', )

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
