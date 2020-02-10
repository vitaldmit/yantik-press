from django.urls import path

from . import views


app_name = 'news'
urlpatterns = [
    path('', views.news, name='news'),
    path('publications/', views.publications, name='publications'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.news_article, name='news_article'),
]
