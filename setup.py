import os
from setuptools import setup

from django_tenant_templates import version


PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
requires = open(os.path.join(PACKAGE_ROOT, 'requirements.txt')).readlines()


setup(
    name='django-tenant-templates',
    version=version,
    description='Tenant-aware templating for Django.',
    author='Joe Friedl',
    author_email='joe@joefriedl.net',
    packages=('django_tenant_templates',),
    install_requires=requires,
    license='MIT',
)
