'''
Production settings for the Gritty Project

'''
from . import base

DEBUG = False

TEMPLATE_DEBUG = False

WSGI_APPLICATION = 'gritty.wsgi_production.application'

ALLOWED_HOSTS = ['*']

# TO-DO
DATABASES = {}

SECRET_KEY = None