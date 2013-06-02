"""
Integration tests for tenant template loading.
"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.integration.test_project.settings'

from django.test import TestCase



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
