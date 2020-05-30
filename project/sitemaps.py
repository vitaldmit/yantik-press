from datetime import datetime

from django.contrib.sitemaps import Sitemap

from myapps.news.models import News, PhotoGallery, VideoNews


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
