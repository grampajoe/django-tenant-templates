"""
Template loaders.
"""
from django.template.loaders.filesystem import Loader as FileSystemLoader
from django.template.loaders.app_directories import Loader as AppLoader

from django_tenant_templates import local


class TenantLoaderMixin(object):
    """Mixin for making template loaders tenant-aware."""
    def get_template_sources(self, template_name, template_dirs=None):
        if (
                not template_name.startswith('./') and
                hasattr(local, 'tenant_slug') and
                local.tenant_slug is not None
        ):
            template_name = '%s/%s' % (local.tenant_slug, template_name)

        return super(TenantLoaderMixin, self).get_template_sources(
            template_name,
            template_dirs,
        )


class TenantFileSystemLoader(TenantLoaderMixin, FileSystemLoader):
    """Loads templates from the filesystem."""


class TenantAppLoader(TenantLoaderMixin, AppLoader):
    """Loads templates from apps."""
