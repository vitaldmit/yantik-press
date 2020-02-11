from django.contrib import admin

from .models import News, NewsImages, Banners


class NewsImagesInline(admin.TabularInline):
    model = NewsImages


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'created', 'visible')
    list_filter = ('visible', 'created', 'publish', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('-created', '-publish')
    inlines = [NewsImagesInline, ]


@admin.register(NewsImages)
class NewsImagesAdmin(admin.ModelAdmin):
    list_display = ('news', 'created', 'updated', 'visible')
    list_filter = ('visible', 'created', 'updated')
    search_fields = ('news', )
    ordering = ('-created', )


@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', 'visible',)
    list_filter = ('visible', 'created', 'updated')
    search_fields = ('title', )
    ordering = ('-created', '-publish')
