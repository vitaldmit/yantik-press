from datetime import datetime

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from myapps.news.models import Banners


def structure(request):
    """ Страница 'Структура' """
    data = {
        'all_employees': Employees.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    }
    return render(request, 'structure.html', data)


def vacancies(request):
    """ Страница 'Вакансии' """
    data = {
        'all_vacancies': Vacancies.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish'),
        'all_banners': Banners.objects.all().filter(visible=True)
    }
    return render(request, 'vacancies.html', data)


def documents(request):
    """ Страница 'Документы' """
    data = {
        'all_documents': Documents.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish'),
        'all_banners': Banners.objects.all().filter(visible=True)
    }
    return render(request, 'documents.html', data)


def projects(request):
    """ Страница 'Документы' """
    data = {
        'all_projects': Projects.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish'),
        # 'docs':Projects.objects.filter(projects_files__visible=True),
        'all_banners': Banners.objects.all().filter(visible=True)
    }
    return render(request, 'projects.html', data)


def history(request):
    """ Страница 'История' """
    data = {
        'all_history': History.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    }
    return render(request, 'history.html', data)


def subscribe(request):
    """ Страница 'Подписка' """
    data = {
        'all_subscribe': Subscribe.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    }
    return render(request, 'subscribe.html', data)


def advertising(request):
    """ Страница 'Реклама' """
    data = {
        'all_advertising': Advertising.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    }
    return render(request, 'advertising.html', data)


def announcing(request):
    """ Страница 'Объявления' """
    all_announcing = Announcing.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    paginator = Paginator(all_announcing, 10)
    page = request.GET.get('page')
    try:
        all_announcing = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом,возвращаем первую страницу.
        all_announcing = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц,
        # возвращаем последнюю.
        all_announcing = paginator.page(paginator.num_pages)
    return render(request, 'announcing.html',
                  {'page': page,
                   'all_announcing': all_announcing})


def contacts(request):
    """ Страница 'Контакты' """
    data = {
        'all_contacts': Contacts.objects.filter(visible=True).filter(publish__lte=datetime.now()).order_by('-publish')
    }
    return render(request, 'contacts.html', data)
