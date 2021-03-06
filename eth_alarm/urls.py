# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.views.generic import (
    TemplateView,
    RedirectView,
)


urlpatterns = patterns(
    '',
    url(
        r'^$', TemplateView.as_view(template_name='home.html'),
        name="site-index",
    ),
    url(
        r'^source/$', RedirectView.as_view(pattern_name='source-v070', permanent=False),
        name="source-latest",
    ),
    url(
        r'^source/v0\.7\.0/$', TemplateView.as_view(template_name='source-v0.7.0.html'),
        name="source-v070",
    ),
    url(
        r'^source/v0\.6\.0/$', TemplateView.as_view(template_name='source-v0.6.0.html'),
        name="source-v060",
    ),
    url(
        r'^source/v0\.5\.0/$', TemplateView.as_view(template_name='source-v0.5.0.html'),
        name="source-v050",
    ),
    url(
        r'^source/v0\.4\.0/$', TemplateView.as_view(template_name='source-v0.4.0.html'),
        name="source-v040",
    ),
    url(
        r'^source/v0\.3\.0/$', TemplateView.as_view(template_name='source-v0.3.0.html'),
        name="source-v030",
    ),
    url(
        r'^source/v0\.2\.0/$', TemplateView.as_view(template_name='source-v0.2.0.html'),
        name="source-v020",
    ),
    url(
        r'^source/v0\.1\.0/$', TemplateView.as_view(template_name='source-v0.1.0.html'),
        name="source-v010",
    ),
    url(
        r'^bug-bounty/$', TemplateView.as_view(template_name='bug_bounty.html'),
        name="bug-bounty",
    ),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
