# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url, patterns, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views import defaults as default_views

from django.http import HttpResponse
from shop.views.auth import PasswordResetConfirm
from cms.sitemaps import CMSSitemap
from cms.models.pagemodel import Page

def render_robots(request):
    permission = 'noindex' in settings.ROBOTS_META_TAGS and 'Disallow' or 'Allow'
    return HttpResponse('User-Agent: *\n%s: /\n' % permission, content_type='text/plain')

i18n_urls = (
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirm.as_view(template_name='myshop/pages/password-reset-confirm.html'),
        name='password_reset_confirm'),
    url(r'^', include('cms.urls')),
)

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    # this must go before require_login urls
    #url(settings.ADMIN_URL, include(admin.site.urls)),

    #url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    #url(r'^', include('cms.urls')),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # User management
    url(r'^users/', include("maxoshop_project.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    ## Your stuff: custom urls includes go here
    url(r'^robots\.txt$', render_robots),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}, name='sitemap'),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    #url(r'^shop/', include('maxoshop_project.maxoshop.urls', namespace='shop')),
]

if settings.USE_I18N:
    urlpatterns += i18n_patterns('', *i18n_urls)
else:
    urlpatterns += i18n_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
        url(r'^500/$', default_views.server_error),
    ]


