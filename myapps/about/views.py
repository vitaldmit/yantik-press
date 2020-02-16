from django.shortcuts import render

from .models import Employees, Vacancies, Documents, Subscribe, Advertising, Announcing, Contacts


def structure(request):
    """ Страница 'Структура' """
    all_employees = Employees.objects.all()
    return render(request, 'structure.html', {'all_employees': all_employees})


def vacancies(request):
    """ Страница 'Вакансии' """
    all_vacancies = Vacancies.objects.all().order_by('-created')
    return render(request, 'vacancies.html', {'all_vacancies': all_vacancies})


def documents(request):
    """ Страница 'Документы' """
    all_documents = Documents.objects.all().order_by('-created')
    return render(request, 'documents.html', {'all_documents': all_documents})


def subscribe(request):
    """ Страница 'Подписка' """
    all_subscribe = Subscribe.objects.all().order_by('-created')
    return render(request, 'subscribe.html', {'all_subscribe': all_subscribe})


def advertising(request):
    """ Страница 'Реклама' """
    all_advertising = Advertising.objects.all().order_by('-created')
    return render(request, 'advertising.html', {'all_advertising': all_advertising})


def announcing(request):
    """ Страница 'Объявления' """
    all_announcing = Announcing.objects.all().order_by('-created')
    return render(request, 'announcing.html', {'all_announcing': all_announcing})


def contacts(request):
    """ Страница 'Контакты' """
    all_contacts = Contacts.objects.all()
    return render(request, 'contacts.html', {'all_contacts': all_contacts})
