"""
Unit tests for middleware.
"""
import unittest
import mock

from django_tenant_templates.middleware import TenantMiddleware


@mock.patch('django_tenant_templates.middleware.local')
class TestTenantMiddleware(unittest.TestCase):
    """Tests for tenant middleware."""
    def setUp(self):
        self.middleware = TenantMiddleware()

    def test_get_tenant_slug(self, local):
        """Test getting the tenant slug from the request."""
        request = mock.Mock()

        self.middleware.process_request(request)

        self.assertEqual(local.tenant_slug, request.tenant_slug)

    def test_tenant_slug_name(self, local):
        request = mock.Mock()

        self.middleware.slug_property_name = 'fart'

        self.middleware.process_request(request)

        self.assertEqual(local.tenant_slug, request.fart)
