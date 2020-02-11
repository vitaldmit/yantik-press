from django.shortcuts import render

from .models import Employees, Vacancies


def employees(request):
    """Страница структуры"""
    all_employees = Employees.objects.all()
    return render(request, 'structure.html', {'all_employees': all_employees})


def vacancies(request):
    """Страница структуры"""
    all_vacancies = Vacancies.objects.all()
    return render(request, 'vacancies.html', {'all_vacancies': all_vacancies})
