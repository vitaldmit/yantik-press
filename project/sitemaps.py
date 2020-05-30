from datetime import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from myapps.news.models import News, PhotoGallery, VideoNews


class IndexSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['index', ]

    def location(self, item):
        return reverse(item)


class NewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return News.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')

    def lastmod(self, obj):
        return obj.updated


class PhotoGallerySitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return PhotoGallery.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')

    def lastmod(self, obj):
        return obj.updated


class VideoNewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return VideoNews.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')

    def lastmod(self, obj):
        return obj.updated


class VideoNewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return VideoNews.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')

    def lastmod(self, obj):
        return obj.updated


class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['about:structure', 'about:vacancies', 'about:documents',
                'about:projects', 'about:history', 'subscribe', 'advertising',
                'announcing', 'contacts']

    # def lastmod(self, item):
    #     return item.updated

    def location(self, item):
        return reverse(item)
