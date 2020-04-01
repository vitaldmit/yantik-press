from django.urls import path

from . import views


app_name = 'news'
urlpatterns = [
    path('photogallery/', views.photogallery, name='photogallery'),
    path('photogallery/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.photogallery_article, name='photogallery_article'),
    path('news/', views.news, name='news'),
    path('actuals/', views.actuals, name='actuals'),
    path('publications/', views.publications, name='publications'),
    path('<str:type>/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.news_actuals_publications_article, name='news_article'),
]
