from django.contrib import admin

from .models import *


class DocumentsFilesInline(admin.TabularInline):
    model = DocumentsFiles


class ProjectsFilesInline(admin.TabularInline):
    model = ProjectsFiles


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'publish', 'created', 'visible')
    ordering = ('-publish', '-created')


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('post', 'visible')
    ordering = ('-publish', '-created')


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'publish', 'created')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-publish', '-created')
    inlines = [DocumentsFilesInline, ]


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'publish', 'created')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-publish', '-created')
    inlines = [ProjectsFilesInline, ]


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created')
    list_filter = ('visible', 'created', 'publish')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish'
    ordering = ('-publish', '-created')


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created', 'visible')
    ordering = ('-publish', '-created')


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created', 'visible')
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
    list_display = ('title', 'publish', 'created', 'updated')
    ordering = ('-publish', '-created')
