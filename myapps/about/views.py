from django.shortcuts import render

from .models import Employees, Vacancies, Documents


def employees(request):
    """Страница структуры"""
    all_employees = Employees.objects.all()
    return render(request, 'structure.html', {'all_employees': all_employees})


def vacancies(request):
    """Страница с вакансими"""
    all_vacancies = Vacancies.objects.all()
    return render(request, 'vacancies.html', {'all_vacancies': all_vacancies})

def documents(request):
    """Страница с докумнетами"""
    all_documents = Documents.objects.all()
    return render(request, 'documents.html', {'all_documents': all_documents})
