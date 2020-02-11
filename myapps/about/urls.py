from django.urls import path

from . import views


app_name = 'about'
urlpatterns = [
    # path('structure/', views.employees, name='structure'),
    path('employees/', views.employees, name='employees'),
    path('employeesvacancies/', views.vacancies, name='vacancies'),
]
