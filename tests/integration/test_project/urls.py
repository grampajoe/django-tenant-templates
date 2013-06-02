try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django 1.3
    from django.conf.urls.defaults import patterns, url

from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
)
