from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.postgres.search import (SearchVector, SearchQuery,
                                            SearchRank)

from .models import *


def index(request):
    # Главная страница
    all_news = News.objects.filter(Q(type='news') | Q(type='actuals')).filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')[:10]
    all_publications = News.objects.filter(type='publications').filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')[:10]
    all_photogallery = PhotoGallery.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')[:1]
    all_videonews = VideoNews.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')[:1]
    all_banners = Banners.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('publish')
    return render(request, 'index.html',
                  {'all_news': all_news,
                   'all_publications': all_publications,
                   'all_banners': all_banners,
                   'all_photogallery': all_photogallery,
                   'all_videonews': all_videonews})


def news(request):
    # Тип новости 'Новости'
    all_news = News.objects.filter(type='news').filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    paginator = Paginator(all_news, 10)
    page = request.GET.get('page')
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом,возвращаем первую страницу.
        all_news = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц,
        # возвращаем последнюю.
        all_news = paginator.page(paginator.num_pages)
    num_pages = paginator.num_pages
    # Баннеры
    all_banners = Banners.objects.filter(visible=True)
    return render(request, 'news.html',
                  {'page': page,
                   'all_news': all_news,
                   'all_banners': all_banners,
                   'num_pages': num_pages})


def publications(request):
    # Тип новости 'Публикации'
    all_publications = News.objects.filter(type='publications').filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    paginator = Paginator(all_publications, 10)
    page = request.GET.get('page')
    try:
        all_publications = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом,возвращаем первую страницу.
        all_publications = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц,
        # возвращаем последнюю.
        all_publications = paginator.page(paginator.num_pages)
    num_pages = paginator.num_pages
    # Баннеры
    all_banners = Banners.objects.filter(visible=True)
    return render(request, 'publications.html',
                  {'page': page,
                   'all_publications': all_publications,
                   'all_banners': all_banners,
                   'num_pages': num_pages})


def actuals(request):
    # Тип новости 'Публикации'
    all_actuals = News.objects.filter(type='actuals').filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    paginator = Paginator(all_actuals, 10)
    page = request.GET.get('page')
    try:
        all_actuals = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом,возвращаем первую страницу.
        all_actuals = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц,
        # возвращаем последнюю.
        all_actuals = paginator.page(paginator.num_pages)
    num_pages = paginator.num_pages
    # Баннеры
    all_banners = Banners.objects.filter(visible=True)
    return render(request, 'actuals.html',
                  {'page': page,
                   'all_actuals': all_actuals,
                   'all_banners': all_banners,
                   'num_pages': num_pages})


def news_article(request, type, year, month, day, slug):
    news_article = get_object_or_404(News, slug=slug,
                                     visible=True,
                                     publish__year=year,
                                     publish__month=month,
                                     publish__day=day,
                                     type=type)
    all_banners = Banners.objects.filter(visible=True)
    return render(request, 'news_article.html',
                  {'news_article':
                   news_article,
                   'all_banners': all_banners})


def photogallery(request):
    # видеоновости
    all_photogallery = PhotoGallery.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    paginator = Paginator(all_photogallery, 10)
    page = request.GET.get('page')
    try:
        all_photogallery = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом,возвращаем первую страницу.
        all_photogallery = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц,
        # возвращаем последнюю.
        all_photogallery = paginator.page(paginator.num_pages)
    num_pages = paginator.num_pages
    # Баннеры
    all_banners = Banners.objects.filter(visible=True)
    return render(request, 'photogallery.html',
                  {'page': page,
                   'all_photogallery': all_photogallery,
                   'all_banners': all_banners,
                   'num_pages': num_pages})


def photogallery_article(request, year, month, day, slug):
    photogallery_article = get_object_or_404(PhotoGallery, slug=slug,
                                             visible=True,
                                             publish__year=year,
                                             publish__month=month,
                                             publish__day=day)
    all_banners = Banners.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('publish')
    return render(request, 'photogallery_article.html',
                  {'photogallery_article': photogallery_article,
                   'all_banners': all_banners})


def videonews(request):
    # Видеоновости
    all_videonews = VideoNews.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    paginator = Paginator(all_videonews, 10)
    page = request.GET.get('page')
    try:
        all_videonews = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом,возвращаем первую страницу.
        all_videonews = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц,
        # возвращаем последнюю.
        all_videonews = paginator.page(paginator.num_pages)
    num_pages = paginator.num_pages
    # Баннеры
    all_banners = Banners.objects.filter(visible=True)
    return render(request, 'videonews.html',
                  {'page': page,
                   'all_videonews': all_videonews,
                   'all_banners': all_banners,
                   'num_pages': num_pages})


def videonews_article(request, year, month, day, slug):
    videonews_article = get_object_or_404(VideoNews, slug=slug,
                                          visible=True,
                                          publish__year=year,
                                          publish__month=month,
                                          publish__day=day)
    all_banners = Banners.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('publish')
    return render(request, 'videonews_article.html',
                  {'videonews_article': videonews_article,
                   'all_banners': all_banners})


def search(request):
    query = request.GET.get('q')
    if query:
        # all_results = News.objects.filter(content__contains=query)
        # all_results = News.objects.filter(content__search=query)
        # all_results = News.objects.annotate(search=SearchVector('content', 'title')).filter(search=query)
        search_vector = SearchVector('title', 'content')
        search_query = SearchQuery(query)
        all_results = News.objects.annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query)
        ).filter(search=search_query).order_by('-rank')
        paginator = Paginator(all_results, 10)
        page = request.GET.get('page')
        try:
            all_results = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом,возвращаем первую страницу.
            all_results = paginator.page(1)
        except EmptyPage:
            # Если номер страницы больше, чем общее количество страниц,
            # возвращаем последнюю.
            all_results = paginator.page(paginator.num_pages)
        num_pages = paginator.num_pages
        all_banners = Banners.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('publish')
        return render(request, 'search.html', {'query': query,
                                               'all_results': all_results,
                                               'page': page,
                                               'num_pages': num_pages,
                                               'all_banners': all_banners})
