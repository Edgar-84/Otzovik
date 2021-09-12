from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *
menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Категории компаний", 'url_name': 'cats'},
        {'title': "Добавить компанию", 'url_name': 'add_company'},
        {'title': "Информация о сайте", 'url_name': 'info'},
        {'title': "Регистрация", 'url_name': 'login'}]

def main_page(request):
    """This main page handler"""
    post = Company.objects.all()
    context = {
        'posts': post,
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'company/index.html', context=context)

def categories(request):
    """This categories of company handler"""
    cats = Category.objects.all()
    context = {
        'cats': cats,
        'menu': menu,
        'title': "Категории компаний",
        'cat_selected': 0,
    }
    return render(request, 'company/categories.html', context=context)

def add_company(request):
    return HttpResponse('Добавление компании')

def info_about_site(request):
    return HttpResponse('Информация о сайте')

def login(request):
    return HttpResponse('Регистрация пользователя')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def show_category(request, cat_id):

    post = Company.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(post) == 0:
        raise Http404()

    context = {
        'posts': post,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по категории',
        'cat_selected': cat_id,
    }

    return render(request, 'company/index.html', context=context)



def pageNotFound(request, exception):
    """This error handler 404 """
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')