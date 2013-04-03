# -*- coding: utf-8 -*-
from reporteaccidentes import settings_local
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_PARENT_PATH = os.path.abspath(os.path.join(PROJECT_PATH, "../.."))

DEBUG = settings_local.DEBUG
TEMPLATE_DEBUG = DEBUG
ADMINS = settings_local.ADMINS
MANAGERS = ADMINS
DATABASES = settings_local.DATABASES
ROOT_URLCONF = 'reporteaccidentes.urls'
TIME_ZONE = 'America/Montevideo'
LANGUAGE_CODE = 'es'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
STATIC_URL = "/reporteaccidentes/static/"
STATICFILES_DIRS = settings_local.STATICFILES_DIRS
MEDIA_ROOT = settings_local.MEDIA_ROOT
MEDIA_URL = '/media/'
STATIC_ROOT = settings_local.STATIC_ROOT
TEMPLATE_DIRS = (
      os.path.join(PROJECT_PATH, 'templates/'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'reporteaccidentes.accidentes'
)
