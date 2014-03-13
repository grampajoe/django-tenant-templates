Django Tenant Templates
=======================

Tenant-aware templating for Django.

Overview
--------

A tenant is a set of application configurations and behaviors that runs
alongside other tenants in the same server process.

One of the first challenges when building a multitenant Web app is loading
different templates for each tenant without making developers' lives harder.
Django Tenant Templates provies utilities for making templating in Django
tenant-aware without getting in the way of normal Django development.

Installation and Usage
----------------------

Install `django-tenant-templates` from PyPI::

    pip install django-tenant-templates

Add the tenant middleware class to your Django settings::

    MIDDLEWARE_CLASSES = (
        ...
        'django_tenant_templates.middleware.TenantMiddleware',
        ...
    )

Add one or more of the tenant template loaders. They should be placed before
the standard Django loaders::

    TEMPLATE_LOADERS = (
        'django_tenant_templates.loaders.TenantFileSystemLoader',
        ...
    )

Now all you need to do is set `request.tenant_slug` somewhere before
`TenantMiddleware` is called, and put your tenant-specific templates in
a subdirectory whose name is the value of `request.tenant_slug`.

After that, all template names will get prefixed with `request.tenant_slug`
and a forward slash. If `request.tenant_slug` is `'my_tenant'`,
`'customers/customer_list.html'` becomes
`'my_tenant/customers/customer_list.html'`.

To fall back to non-tenant template loading, make sure to include other
template loaders after the tenant loaders in `settings.TEMPLATE_LOADERS`.

If you want to explicitly load a non-tenant template, prefix the template name
with './'. This allows you to extend a non-tenant template with the same name
as the tenant template, which can be useful for things like overriding only
part of a base template rather than replacing the whole thing.

Middleware
----------

**TRIGGER WARNING: This section contains references to thread locals.**

The `django_tenant_templates.middleware.TenantMiddleware` class is what makes
the tenant template loaders work. It looks for `request.tenant_slug` and
places it in thread local storage. The template loaders then use the
thread local to figure out where they should look for templates.

How you get the value you assign to `request.tenant_slug` is up to you,
but it should be a valid directory name for whatever filesystem you're using.
For example::

    # Middleware that runs before TenantMiddleware
    class ExampleMiddleware(object):
        def process_request(self, request):
            # Get the tenant slug from an HTTP header.
            request.tenant_slug = request.META.get('HTTP_X_TENANT_ID', None)

You can change the `request` attribute `TenantMiddleware` looks for by using
a custom subclass::

    class CustomTenantMiddleware(TenantMiddleware):
        slug_attribute_name = 'fart'

Django Tenant Templates' template loaders would then use the value of
`request.fart` as the tenant slug.

Loaders
-------

Django Tenant Templates provides a few template loaders that correspond to
the loaders provided by Django. They all live in the
`django_tenant_templates.loaders` module.

Each loader does essentially the same thing: a tenant slug is prefixed to the
template name, then the template is looked up normally. For example, if the
tenant slug is `'my_tenant'`, the template name `customers/customer_list.html`
will be translated to `my_tenant/customers/customer_list.html`.

TenantFileSystemLoader
~~~~~~~~~~~~~~~~~~~~~~

Finds templates using `settings.TEMPLATE_DIRS`. See
`django.template.loaders.filesystem.Loader`.

TenantAppLoader
~~~~~~~~~~~~~~~

Finds templates in each of your `INSTALLED_APPS`. See
`django.template.loaders.app_directories.Loader`.

TenantLoaderMixin
~~~~~~~~~~~~~~~~~

A mixin that adds tenant-awareness to template loading. Use this to create
custom template loaders.
