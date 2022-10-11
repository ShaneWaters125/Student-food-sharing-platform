"""
Django settings for agileProject project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-15z!ko+!^x9c3go2&v5)vbmz*$%t_ljweco*--$-pci7o8ad1&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # our own added apps
    'recipesApp',
    'users',
    'crispy_forms',
    'formtools'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # whitenoise for static files - allows save CSS when debug is False
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'agileProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'agileProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {

        # Settings for local postgres DB - create server in PGAdmin4 and set password as admin
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'agile',
        'USER': 'postgres',
        'PASSWORD': 'SWSCswsc',
        'HOST': 'localhost',

        # Settings for uni postgres DB server

        # 'NAME': 'csm2020_21_22_wilson',  # your database name
        # 'USER': 'wilson',  # default
        # 'PASSWORD': 'l0TcSyW3',  # your password
        # 'HOST': 'db.dcs.aber.ac.uk',  # default
        #
        # 'TEST': {
        #     'NAME': 'test',  # for unit test
        # },

        'PORT': '',  # default
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

# Enable whitenoise in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'recipes-home'
LOGIN_URL = 'login'

# setting for send email to change password
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "csm2020agile@gmail.com"
EMAIL_HOST_PASSWORD = "agile2020"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# log path
LOG_PATH = os.path.join(BASE_DIR, 'log')
# if the path does not exist，then create
if not os.path.isdir(LOG_PATH):
    os.mkdir(LOG_PATH)
#setting for log
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "default": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file': {
            'level': "INFO",
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH,'django.log'),
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 5,
            'formatter': 'default',
            'encoding': 'utf-8',
        },
    },
    "loggers": {
        "django": {
            'handlers': ['file'],
            "level": "INFO",
        },
    },
}