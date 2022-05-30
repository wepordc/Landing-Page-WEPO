"""
Django settings for wepo project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from decouple import config
import dj_database_url 
from dotenv import load_dotenv, find_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
"""BASE_DIR = Path(__file__).resolve().parent.parent.parent"""
BASE_DIR = Path(__file__).resolve().parent.parent.parent
"""BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__,os.pardir))))"""
DEBUG = True
#load_dotenv(find_dotenv)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
load_dotenv(find_dotenv())
# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']


AUTH_USER_MODEL = 'accounts.Profile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'user_visit',
    'django_generate_secret_key',
    'django_extensions',
    
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user_visit.middleware.UserVisitMiddleware',
]

ROOT_URLCONF = 'wepo.urls'


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

WSGI_APPLICATION = 'wepo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3', conn_max_age=600, ssl_require=False)
}
#db_from_env = dj_database_url.config(conn_max_age=600)
#DATABASES['default'].update(db_from_env)
CREDENTIALS = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wepo_bdd',
        'USER': 'root',
        'PASSWORD': 'Pourquoipasnous?@',
        'PORT': '3306',
        'HOST': 'localhost',
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

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'



STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.django.
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

##Love