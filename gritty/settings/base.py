"""
Base settings for gritty project.

"""
import os
# base dir for the  django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# project dir 
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quest',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gritty.urls'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# path in the url for serving the static files
STATIC_URL = '/static/'

# Location of static files on the file-system
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
    )

# `collectstatic` will put all the static files here
STATIC_ROOT = os.path.join(BASE_DIR,'static_collection')

# Templates directory
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
    )


