try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django 1.3
    from django.conf.urls.defaults import patterns, url

from django.views.generic import TemplateView

from .views import error_500


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^error_500$', error_500),
)
