"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from myapps.news.views import index, search
from myapps.about.views import subscribe, advertising, announcing, contacts
from .sitemaps import *


sitemaps = {
    'index': IndexSitemap,
    'news': NewsSitemap,
    'photogallery': PhotoGallerySitemap,
    'videonews': VideoNewsSitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    path('', index, name='index'),
    path('press/', include('myapps.news.urls')),
    path('about/', include('myapps.about.urls')),

    path('subscribe/', subscribe, name='subscribe'),
    path('advertising/', advertising, name='advertising'),
    path('announcing/', announcing, name='announcing'),
    path('contacts/', contacts, name='contacts'),

    path('search', search, name='search'),

    path('administrat/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^tinymce/', include('tinymce.urls')),
]

# handle /media/, /static/ static files (only if DEBUG is True)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Административная панель ЯЛ ӖҪЧЕНӖ'
handler404 = 'django.views.defaults.page_not_found'
