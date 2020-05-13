from django.urls import path

from . import views


app_name = 'news'
urlpatterns = [
    path('photogallery/', views.photogallery, name='photogallery'),
    path('photogallery/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.photogallery_article, name='photogallery_article'),

    path('videonews/', views.videonews, name='videonews'),
    path('videonews/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.videonews_article, name='videonews_article'),

    path('news/', views.news, name='news'),
    path('actuals/', views.actuals, name='actuals'),
    path('publications/', views.publications, name='publications'),
    path('<str:type>/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.news_article, name='news_article'),
]
