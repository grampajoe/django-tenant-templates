"""
Django Tenant Templates
"""
from threading import local as _local


version = '0.2'


local = _local()
local.tenant_slug = None
