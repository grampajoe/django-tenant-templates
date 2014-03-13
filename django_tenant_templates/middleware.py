"""
Middleware!
"""
from django_tenant_templates import local


class TenantMiddleware(object):
    """Middleware for enabling tenant-aware template loading."""
    slug_property_name = 'tenant_slug'

    def process_request(self, request):
        local.tenant_slug = getattr(request, self.slug_property_name, None)
