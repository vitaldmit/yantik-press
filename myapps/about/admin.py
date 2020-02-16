from django.contrib import admin

from .models import Employees, Vacancies, Documents, Subscribe, Advertising, Announcing, Contacts


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'phone', 'email', 'visible')


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('post', 'visible')


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible')


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'visible')


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'visible')


@admin.register(Announcing)
class AnnouncingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'visible')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'visible')
