from django.urls import path

from . import views


app_name = 'news'
urlpatterns = [
    path('', views.news, name='news'),
    path('actual/', views.actuals, name='actuals'),
    path('publications/', views.publications, name='publications'),
    path('photogallery/', views.photogallery, name='photogallery'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.news_article, name='news_article'),
    path('photo/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.photogallery_article, name='photogallery_article'),
]
