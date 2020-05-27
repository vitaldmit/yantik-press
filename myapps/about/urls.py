from django.urls import path

from . import views


app_name = 'about'
urlpatterns = [
    # path('structure/', views.employees, name='structure'),
    path('structure/', views.structure, name='structure'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('documents/', views.documents, name='documents'),
    path('projects/', views.projects, name='projects'),
    path('history/', views.history, name='history'),
    # path('documents/<int:year>-<int:month>-<int:day>/<slug:slug>.docx',
    #      views.documents, name='documents'),

    # path('subscribe/', views.subscribe, name='subscribe'),
    # path('advertising/', views.advertising, name='advertising'),
    # path('announcing/', views.announcing, name='announcing'),
    # path('contacts/', views.contacts, name='contacts'),
]
