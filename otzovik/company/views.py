from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def main_page(request):
    """This main page handler"""
    return HttpResponse('Главная страница приложения')

def pageNotFound(request, exception):
    """This error handler 404 """
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def categories(request):
    """This categories of company handler"""
    return HttpResponse(f'<h1>Просмотр всех категорий вакансий</h1>')

