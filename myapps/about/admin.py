from django.contrib import admin

from .models import *


class DocumentsFilesInline(admin.TabularInline):
    model = DocumentsFiles


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'phone', 'email', 'visible')
    ordering = ('-publish', '-created')


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('post', 'visible')
    ordering = ('-publish', '-created')


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'created', 'publish')
    ordering = ('-publish', '-created')
    inlines = [DocumentsFilesInline, ]


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created')
    list_filter = ('visible', 'created', 'publish')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish'
    ordering = ('-publish', '-created')


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'visible')
    ordering = ('-publish', '-created')


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'visible')
    ordering = ('-publish', '-created')


@admin.register(Announcing)
class AnnouncingAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created', 'ontop', 'visible')
    list_filter = ('visible', 'created', 'publish')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish'
    ordering = ('-publish', '-created')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    ordering = ('-publish', '-created')
