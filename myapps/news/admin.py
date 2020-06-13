from django.contrib import admin

from .models import *


class PhotoGalleryImagesInline(admin.TabularInline):
    model = PhotoGalleryImages


class PhotoGalleryInline(admin.StackedInline):
    model = PhotoGallery
    max_num = 1


def turn_into_actuals(modeladmin, request, queryset):
    queryset.update(type='actuals')


def turn_into_news(modeladmin, request, queryset):
    queryset.update(type='news')


def turn_into_publications(modeladmin, request, queryset):
    queryset.update(type='publications')


turn_into_actuals.short_description = "Перевести в 'Актуально'"
turn_into_news.short_description = "Перевести в 'Новости'"
turn_into_publications.short_description = "Перевести в 'Публикации'"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'publish', 'created', 'visible')
    list_filter = ('type', 'visible', 'created', 'publish', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('-publish', '-created')
    # inlines = [PhotoGalleryInline, ]
    actions = [turn_into_actuals, turn_into_news, turn_into_publications]


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created', 'visible')
    list_filter = ('visible', 'created', 'publish')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('news',)
    date_hierarchy = 'publish'
    ordering = ('-publish', '-created')
    inlines = [PhotoGalleryImagesInline, ]


@admin.register(VideoNews)
class VideoNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created', 'visible')
    list_filter = ('visible', 'created', 'publish')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('news',)
    date_hierarchy = 'publish'
    ordering = ('-publish', '-created')
    # inlines = [VideoNewsImagesInline, ]


@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created', 'visible')
    list_filter = ('visible', 'created', 'publish')
    search_fields = ('title', )
    date_hierarchy = 'publish'
    ordering = ('-publish', '-created')
