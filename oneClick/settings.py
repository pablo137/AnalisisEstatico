"""
Django settings for oneClick project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import environ

env = environ.Env()

environ.Env.read_env()
    


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

MESSAGE_STORAGE= "django.contrib.messages.storage.cookie.CookieStorage"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    # bootstrap 5
    'crispy_forms',
    'crispy_bootstrap5',

    # dependencias de django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #nuevas apps
    'store',
    'cloudinary_storage',
]

# Variables globales de bootstrap5
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oneClick.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oneClick.wsgi.application'


# Database LOCAL
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_oneclick',
#         'USER' :'postgres',
#         'PASSWORD' : '123',
#         'HOST' : 'localhost',
#         'PORT' : 5432
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

############################ RENDER DATABASE

# import dj_database_url
# DATABASES = {'default': dj_database_url.config(default='postgres://USER:PASSWORD@HOST:PORT/NAME', conn_max_age=600 , test_options={'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'db_oneclick',
#     'USER' :'postgres',
#     'PASSWORD' : '123',
#     'HOST' : 'localhost',
#     'PORT' : 5432})}

########################### END RENDER DATABASE

# DATABASE DEFECTO
# DATABASES = {

#     'default': dj_database_url.parse(env('DATABASE_URL'))

# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
if not DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    ]
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Variable de redireccion de login y logout
LOGIN_REDIRECT_URL = 'perfil'
LOGOUT_REDIRECT_URL = 'home'

#CLOUDINARY
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dexh8g1vv',
    'API_KEY': '353423878312923',
    'API_SECRET': 'G06U-ir4m2SY0B_aqnKjRVe_owc'
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Configuracion de correo electronico
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '523a1a06ac16bd'
EMAIL_HOST_PASSWORD = '6b3b31c114347d'
EMAIL_PORT = '2525'