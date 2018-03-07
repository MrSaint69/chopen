"""
Django settings for Chopen project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd0vy02-g#nq@lg!s%5v$w(jilj@af791#1-3k9y7ea3c)djj!w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'chopen',
    'web_app',
    'digitizer',
    'ion_channel',
    'account',
    'api',
    # 'fitter',
    'formtools',
    'rest_framework',
    'homepage',

    # 'wagtail.wagtailforms',
    # 'wagtail.wagtailredirects',
    # 'wagtail.wagtailembeds',
    # 'wagtail.wagtailsites',
    # 'wagtail.wagtailusers',
    # 'wagtail.wagtailsnippets',
    # 'wagtail.wagtaildocs',
    # 'wagtail.wagtailimages',
    # 'wagtail.wagtailsearch',
    # 'wagtail.wagtailadmin',
    # 'wagtail.wagtailcore',
    #
    # 'modelcluster',
    # 'taggit',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # 'wagtail.wagtailcore.middleware.SiteMiddleware',
    # 'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'web_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'web_app', 'templates'),
                 os.path.join(BASE_DIR,'ion_channel', 'templates'),
                 os.path.join(BASE_DIR,'digitizer', 'templates'),
                 os.path.join(BASE_DIR,'account', 'templates')],
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


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Disable irritating django.db.backends logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class':'django.utils.log.NullHandler',
#             },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['null'],  # Quiet by default!
#             'propagate': False,
#             'level':'DEBUG',
#         },
#     },
# }

WSGI_APPLICATION = 'web_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# CHANNELWORM_DB = os.path.join(BASE_DIR, 'channelworm/db.sqlite3')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'channelworm': {
    #     'NAME': 'CHANNELWORM_DB',
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'USER': 'channelworm',
    #     'PASSWORD': 'veryPriv@ate'
    # }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Pycharm detected this
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# TEMPLATE_DIRS = (
#     os.path.join(PROJECT_ROOT, 'templates').replace('\\', '/'),
# )

# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )

STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi','static')
# STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'web_app', 'static'),
    os.path.join(BASE_DIR, 'ion_channel', 'static'),
    os.path.join(BASE_DIR, 'digitizer', 'static'),
)

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'
# initialize as empty so we can do `settings.configure()`
DEFAULT_INDEX_TABLESPACE = ''
DEFAULT_TABLESPACE = ''
ABSOLUTE_URL_OVERRIDES = {}

# WAGTAIL_SITE_NAME = 'OpenWorm'
