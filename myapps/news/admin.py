from django.contrib import admin

from .models import News, NewsImages, Banners, PhotoGallery


class NewsImagesInline(admin.TabularInline):
    model = NewsImages


class PhotoGalleryInline(admin.StackedInline):
    model = PhotoGallery
    max_num = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'created', 'visible')
    list_filter = ('visible', 'created', 'publish', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('-created', '-publish')
    inlines = [PhotoGalleryInline, ]


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'visible')
    list_filter = ('visible', 'created',)
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('news',)
    date_hierarchy = 'created'
    ordering = ('-created', )
    inlines = [NewsImagesInline, ]


# @admin.register(NewsImages)
# class NewsImagesAdmin(admin.ModelAdmin):
#     list_display = ('news', 'created', 'updated', 'visible')
#     list_filter = ('visible', 'created', 'updated')
#     search_fields = ('news', )
#     ordering = ('-created', )


@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', 'visible',)
    list_filter = ('visible', 'created', 'updated')
    search_fields = ('title', )
    ordering = ('-created', '-publish')
