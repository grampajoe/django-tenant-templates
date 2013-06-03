"""
Unit tests for template loaders.
"""
import unittest
import mock

# Hack around Django's app_directories.Loader cache-apps-on-import behavior.
# Use our test project's settings to keep INSTALLED_APPS consistent. This is
# very unfortunate, but necessary. lol dependent tests :(
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.integration.test_project.settings'

from django_tenant_templates.loaders import TenantLoaderMixin


class FakeBaseLoader(object):
    """A fake base loader.

    Proxies calls to get_template_sources to a spy.
    """
    get_sources_spy = mock.Mock()
    get_template_sources = get_sources_spy


class FakeLoader(TenantLoaderMixin, FakeBaseLoader):
    """A fake loader."""


class TestTenantLoaderMixin(unittest.TestCase):
    """Tests for the tenant loader mixin."""
    def setUp(self):
        self.loader = FakeLoader()

    @mock.patch('django_tenant_templates.loaders.local', spec=True)
    def test_loader(self, local):
        """Test the loader."""
        local.tenant_slug = 'test'

        self.loader.get_template_sources('test.html', mock.sentinel.dirs)

        self.loader.get_sources_spy.assert_called_with(
            'test/test.html',
            mock.sentinel.dirs,
        )

    @mock.patch('django_tenant_templates.loaders.local', spec=True)
    def test_loader_no_slug(self, local):
        """Test the loader with no tenant slug."""
        local.tenant_slug = None

        self.loader.get_template_sources('test.html', mock.sentinel.dirs)

        self.loader.get_sources_spy.assert_called_with(
            'test.html',
            mock.sentinel.dirs,
        )

    @mock.patch('django_tenant_templates.loaders.local', spec=object)
    def test_loader_missing_slug(self, local):
        """Test the loader when the tenant slug is missing.

        This happens when an unhandled exception is raised before
        TenantMiddleware can run.
        """
        self.loader.get_template_sources('test.html', mock.sentinel.dirs)

        self.loader.get_sources_spy.assert_called_with(
            'test.html',
            mock.sentinel.dirs,
        )

    @mock.patch('django_tenant_templates.loaders.local', spec=True)
    def test_loader_explicit_default(self, local):
        """Test explicitly loading a non-tenant template."""
        local.tenant_slug = 'test'

        self.loader.get_template_sources('./test.html', mock.sentinel.dirs)

        self.loader.get_sources_spy.assert_called_with(
            './test.html',
            mock.sentinel.dirs,
        )
