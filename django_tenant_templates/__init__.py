"""
Django Tenant Templates
"""
from threading import local as _local


version = '0.5'


local = _local()
local.tenant_slug = None
