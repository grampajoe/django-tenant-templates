class TenantMiddleware(object):
    """Add tenant information to the request."""
    def process_request(self, request):
        request.tenant_slug = request.GET.get('tenant', 'default')
