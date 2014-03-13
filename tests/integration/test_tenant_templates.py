"""
Integration tests for tenant template loading.
"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.integration.test_project.settings'

import requests

from django.test import TestCase, LiveServerTestCase
from django.test.utils import override_settings


class TestTenantTemplates(TestCase):
    """Tests for loading tenant-specific templates."""
    def test_no_tenant(self):
        """Test that template loading falls through without a tenant."""
        response = self.client.get('/')

        self.assertEqual(response.content, b'no\n')

    def test_filesystem_loader(self):
        """Test finding a tenant template with the filesystem loader."""
        response = self.client.get('/?tenant=filesystem')

        self.assertEqual(response.content, b'filesystem\n')

    def test_app_loader(self):
        """Test finding a tenant template with the app loader."""
        response = self.client.get('/?tenant=app')

        self.assertEqual(response.content, b'app\n')


@override_settings(DEBUG=False, ALLOWED_HOSTS=['localhost'])
class TestTenantErrorTemplates(LiveServerTestCase):
    """Tests for loading templates in error handlers."""
    def test_no_tenant(self):
        """Test the default template for an error handler."""
        response = requests.get('%s/error_500' % self.live_server_url)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content, b'no 500\n')

    def test_filesystem_loader(self):
        """Test finding a filesystem template for an error handler."""
        response = requests.get('%s/error_500?tenant=filesystem' % self.live_server_url)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content, b'filesystem 500\n')

    def test_app_loader(self):
        """Test finding an app template for an error handler."""
        response = requests.get('%s/error_500?tenant=app' % self.live_server_url)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content, b'app 500\n')
