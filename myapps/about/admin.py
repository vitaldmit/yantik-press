from django.contrib import admin

from .models import Employees, Vacancies, Documents


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'visible')


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('post', 'visible')


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible')
