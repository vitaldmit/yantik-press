from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import News, Banners


def index(request):
    # Главная страница
    all_news = News.objects.filter(type='news').order_by('-created')[:10]
    all_publications = News.objects.filter(type='publications').order_by('-created')[:8]
    all_banners = Banners.objects.all()
    return render(request, 'index.html',
                  {'all_news': all_news,
                   'all_publications': all_publications,
                   'all_banners': all_banners})

def news(request):
    # Тип новости 'Новости'
    all_news = News.objects.filter(type='news').order_by('-created')
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
    # Тип новости 'Публикация'
    all_publications = News.objects.filter(type='publications').order_by('-created')[:8]
    all_banners = Banners.objects.all()
    return render(request, 'news.html',
                  {'page': page,
                   'all_news': all_news,
                   'all_publications': all_publications,
                   'all_banners': all_banners})

def publications(request):
    # Тип новости 'Публикации'
    all_publications = News.objects.filter(type='publications').order_by('-created')
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
    # Тип новости 'Публикация'
    all_news = News.objects.filter(type='news').order_by('-created')[:8]
    all_banners = Banners.objects.all()
    return render(request, 'publications.html',
                  {'page': page,
                   'all_publications': all_publications,
                   'all_news': all_news,
                   'all_banners': all_banners})


def news_article(request, year, month, day, post):
    news_article = get_object_or_404(News, slug=post, visible=True,
                                     publish__year=year, publish__month=month,
                                     publish__day=day)
    return render(request, 'news_article.html', {'news_article': news_article})
