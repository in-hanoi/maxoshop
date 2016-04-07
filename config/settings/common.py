## -*- coding: utf-8 -*-
"""
Django settings for maxoshop project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import absolute_import, unicode_literals
from decimal import Decimal
from django.utils.translation import ugettext_lazy as _

import environ

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('maxoshop_project')

env = environ.Env()

SHOP_TUTORIAL = 'i18n'
if SHOP_TUTORIAL not in ('simple', 'i18n', 'polymorphic',):
    raise ImproperlyConfigured("Environment DJANGO_SHOP_TUTORIAL has an invalid value `{}`".format(SHOP_TUTORIAL))



# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'polymorphic',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'djangocms_admin_style',
    'django.contrib.messages',
    'django.contrib.staticfiles',
		'django.contrib.sitemaps',
		'email_auth',
		# CMS
    'djangocms_text_ckeditor',
    'django_select2',
    'cmsplugin_cascade',
    #'cmsplugin_cascade.clipboard',
    'cmsplugin_cascade.sharable',
    'cmsplugin_cascade.extra_fields',
    'cmsplugin_cascade.segmentation',
    'cms_bootstrap3',
    'djng',
		#
    'adminsortable2',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django_fsm',
    'fsm_admin',
    'menus',
    'treebeard',
    'compressor',
    'sekizai',
    'sass_processor',
    'django_filters',
    'filer',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'parler',
    'post_office',
    'haystack',

    # Django-shop
    'shop',
    'shop_stripe',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',

)
THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
)

# Apps specific for this project go here.
LOCAL_APPS = (
    #'maxoshop_project.users',  # custom users app, load before cms
    # Your stuff: custom apps go here
    #'maxoshop_project.maxoshop',  # custom users app
    'maxoshop_project.myshop',  # custom users app
)

# Apps to load last
LAST_APPS = (
    'cms',
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + LAST_APPS

# MIDDLEWARE CONFIGURATION
# Middlewares are processed in reverse order.
# ------------------------------------------------------------------------------

MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'cms.middleware.utils.ApphookReloadMiddleware',
    'djng.middleware.AngularUrlMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
		#'email_auth.middleware.EmailAuthMiddleware',
    'shop.middleware.CustomerMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
		'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'maxoshop_project.contrib.sites.migrations',
		#'maxoshop': 'maxoshop.migrations_{}'.format(polymorphic)
		#'maxoshop': 'maxoshop.migrations_polymorphic',
    'myshop': 'myshop.migrations.{}'.format(SHOP_TUTORIAL)
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# DEBUG TOOLBAR
# ------------------------------------------------------------------------------
# See: http://django-debug-toolbar.readthedocs.org/en/1.0/installation.html#explicit-setup
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Thuy Dang""", 'write.thuy@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
		# DATABASE_URL=psql://urser:un-githubbedpassword@127.0.0.1:8458/database
    #'default': env.db("DATABASE_URL", default="postgres:///maxoshop_project"),
		'default': env.db("DATABASE_URL", default="psql://maxo:maxopw@127.0.0.1:5432/maxoshop_project"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', "English"),
    ('de', "Deutsch"),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
								'django.template.context_processors.csrf',
                'django.contrib.messages.context_processors.messages',
								'sekizai.context_processors.sekizai',
								'cms.context_processors.cms_settings',
								'shop.context_processors.customer',
								'shop_stripe.context_processors.public_keys',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
    ('bower_components', ROOT_DIR('bower_components')),
    ('node_modules', ROOT_DIR('node_modules')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Custom user app defaults
# Select the correct user model
#AUTH_USER_MODEL = 'users.User'
AUTH_USER_MODEL = 'email_auth.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'


# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'

# Your common stuff: Below this line define 3rd party library settings

SECURE_PROXY_SSL_HEADER = (u'HTTP_X_FORWARDED_PROTO', u'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         }
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s %(module)s] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

SILENCED_SYSTEM_CHECKS = ('auth.W004')

############################################
# settings for sending mail

EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@example.com'
EMAIL_HOST_PASSWORD = 'smtp-secret-password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'My Shop <no-reply@example.com>'
EMAIL_REPLY_TO = 'info@example.com'
EMAIL_BACKEND = 'post_office.EmailBackend'

############################################
# settings for third party Django apps

NODE_MODULES_URL = STATIC_URL + 'node_modules/'

SASS_PROCESSOR_INCLUDE_DIRS = (
    ROOT_DIR('node_modules'),
)

COERCE_DECIMAL_TO_STRING = True

COMPRESS_ENABLED = False

FSM_ADMIN_FORCE_PERMIT = True

PARLER_DEFAULT_LANGUAGE = 'de'

PARLER_LANGUAGES = {
    1: (
        {'code': 'de'},
        {'code': 'en'},
    ),
    'default': {
        'fallbacks': ['de', 'en'],
    },
}

ROBOTS_META_TAGS = ('noindex', 'nofollow')

############################################
# settings for django-restframework and plugins

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'shop.rest.money.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # can be disabled for production environments
    ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #   'rest_framework.authentication.TokenAuthentication',
    # ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12,
}

SERIALIZATION_MODULES = {'json': b'shop.money.serializers'}


############################################
# settings for storing session data

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_SAVE_EVERY_REQUEST = True


############################################
# settings for storing files and images

FILER_ADMIN_ICON_SIZES = ('16', '32', '48', '80', '128')

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

FILER_DUMP_PAYLOAD = False

FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

THUMBNAIL_HIGH_RESOLUTION = False

THUMBNAIL_OPTIMIZE_COMMAND = {
    'gif': '/opt/local/bin/optipng {filename}',
    'jpeg': '/opt/local/bin/jpegoptim {filename}',
    'png': '/opt/local/bin/optipng {filename}'
}

THUMBNAIL_PRESERVE_EXTENSIONS = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


############################################
# settings for django-cms and its plugins

CMS_TEMPLATES = (
    ('maxoshop/pages/default.html', _("Default Page")),
)

CMS_LANGUAGES = {
    'default': {
        'fallbacks': ['en', 'de'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
    1: ({
        'public': True,
        'code': 'en',
        'hide_untranslated': False,
        'name': 'English',
        'redirect_on_fallback': True,
    }, {
        'public': True,
        'code': 'de',
        'hide_untranslated': False,
        'name': 'Deutsch',
        'redirect_on_fallback': True,
    },)
}

CMS_CACHE_DURATIONS = {
    'content': 600,
    'menus': 3600,
    'permissions': 86400,
}

CMS_PERMISSION = False

CMS_PLACEHOLDER_CONF = {
    'Main Content Container': {
        'plugins': ['BootstrapRowPlugin', 'SimpleWrapperPlugin', 'SegmentPlugin'],
        'text_only_plugins': ['TextLinkPlugin'],
        'parent_classes': {'BootstrapRowPlugin': []},
        'require_parent': False,
        'glossary': {
            'breakpoints': ['xs', 'sm', 'md', 'lg'],
            'container_max_widths': {'xs': 750, 'sm': 750, 'md': 970, 'lg': 1170},
            'fluid': False,
            'media_queries': {
                'xs': ['(max-width: 768px)'],
                'sm': ['(min-width: 768px)', '(max-width: 992px)'],
                'md': ['(min-width: 992px)', '(max-width: 1200px)'],
                'lg': ['(min-width: 1200px)'],
            },
        },
    },
}

CMSPLUGIN_CASCADE_PLUGINS = ('cmsplugin_cascade.segmentation', 'cmsplugin_cascade.generic',
    'cmsplugin_cascade.link', 'shop.cascade', 'cmsplugin_cascade.bootstrap3',)

CMSPLUGIN_CASCADE = {
    'dependencies': {
        'shop/js/admin/shoplinkplugin.js': 'cascade/js/admin/linkpluginbase.js',
    },
    'alien_plugins': ('TextPlugin', 'TextLinkPlugin',),
    'bootstrap3': {
        'template_basedir': 'angular-ui',
    },
    'plugins_with_extra_fields': (
        'BootstrapButtonPlugin',
        'BootstrapRowPlugin',
        'SimpleWrapperPlugin',
        'HorizontalRulePlugin',
        'ExtraAnnotationFormPlugin',
    ),
    'segmentation_mixins': (
        ('shop.cascade.segmentation.EmulateCustomerModelMixin', 'shop.cascade.segmentation.EmulateCustomerAdminMixin'),
    ),
}

CMSPLUGIN_CASCADE_LINKPLUGIN_CLASSES = (
    'shop.cascade.plugin_base.CatalogLinkPluginBase',
    'cmsplugin_cascade.link.plugin_base.LinkElementMixin',
    'shop.cascade.plugin_base.CatalogLinkForm',
)

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'skin': 'moono',
    'toolbar': 'CMS',
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
}

SELECT2_CSS = 'bower_components/select2/dist/css/select2.min.css'
SELECT2_JS = 'bower_components/select2/dist/js/select2.min.js'


#############################################
# settings for full index text search (Haystack)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://localhost:9200/',
        'INDEX_NAME': 'shop-de',
    },
    'en': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://localhost:9200/',
        'INDEX_NAME': 'shop-en',
    },
}

HAYSTACK_ROUTERS = ('shop.search.routers.LanguageRouter',)

############################################
# settings for django-shop and its plugins
SHOP_APP_LABEL = 'myshop'

SHOP_VALUE_ADDED_TAX = Decimal(19)
SHOP_DEFAULT_CURRENCY = 'EUR'
SHOP_CART_MODIFIERS = (
		'maxoshop_project.myshop.polymorphic_modifiers.MyShopCartModifier' if SHOP_TUTORIAL == 'polymorphic'
    else 'shop.modifiers.defaults.DefaultCartModifier',
    'shop.modifiers.taxes.CartExcludedTaxModifier',
    'maxoshop_project.myshop.modifiers.PostalShippingModifier',
    'maxoshop_project.myshop.modifiers.CustomerPickupModifier',
    'maxoshop_project.myshop.modifiers.StripePaymentModifier',
    'shop.modifiers.defaults.PayInAdvanceModifier',
)
SHOP_EDITCART_NG_MODEL_OPTIONS = "{updateOn: 'default blur', debounce: {'default': 2500, 'blur': 0}}"

SHOP_ORDER_WORKFLOWS = (
    'shop.payment.defaults.PayInAdvanceWorkflowMixin',
    'shop.payment.defaults.CommissionGoodsWorkflowMixin',
    'shop_stripe.payment.OrderWorkflowMixin',
)

SHOP_STRIPE = {
    'PUBKEY': 'pk_test_stripe_secret',
    'APIKEY': 'sk_test_stripe_secret',
    'PURCHASE_DESCRIPTION': _("Thanks for purchasing at MyShop"),
}

for priv_attr in ('SHOP_STRIPE', 'DATABASES'):
    try:
        from . import private_settings
        vars()[priv_attr].update(getattr(private_settings, priv_attr))
    except AttributeError:
        continue
    except KeyError:
        vars()[priv_attr] = getattr(private_settings, priv_attr)
    except ImportError:
        break



