# Django settings for test_project project.
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    },
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8%&n%y*+x=hqypq58zuxx@7tfehdgar9gq-&-q6f1g(j!vbksz'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django_tenant_templates.loaders.TenantFileSystemLoader',
    'django_tenant_templates.loaders.TenantAppLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'tests.integration.test_project.middleware.TenantMiddleware',
    'django_tenant_templates.middleware.TenantMiddleware',
)

ROOT_URLCONF = 'tests.integration.test_project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'tests.integration.test_project.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# This is just for LiveServerTestCase
STATIC_URL = 'static/'

INSTALLED_APPS = (
    'tests.integration.test_app',
)
