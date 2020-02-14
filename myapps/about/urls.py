from django.urls import path

from . import views


app_name = 'about'
urlpatterns = [
    # path('structure/', views.employees, name='structure'),
    path('structure/', views.structure, name='structure'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('documents/', views.documents, name='documents'),
]
