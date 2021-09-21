from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Категории компаний", 'url_name': 'cats'},
        {'title': "Добавить компанию", 'url_name': 'add_company'},
        {'title': "Информация о сайте", 'url_name': 'info'},
        {'title': "Регистрация", 'url_name': 'login'}]

class main_page(ListView):

    model = Company
    template_name = 'company/index.html'
    context_object_name = 'companies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Company.objects.filter(is_published=True)

def categories(request):
    """This categories of company handler"""

    context = {
        'menu': menu,
        'title': "Категории компаний",
        'cat_selected': 0,
    }
    return render(request, 'company/categories.html', context=context)


class add_company(CreateView):
    form_class = add_company_form
    template_name = 'company/addcompany.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context


def info_about_site(request):

    return HttpResponse('Информация о сайте')

def login(request):

    return HttpResponse('Регистрация пользователя')

class show_post(DetailView):
    model = Company
    template_name = 'company/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['menu'] = menu
        return context

class show_category(ListView):
    model = Company
    template_name = 'company/index.html'
    context_object_name = 'companies'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['companies'][0].cat)
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Company.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


def pageNotFound(request, exception):
    """This error handler 404 """

    return HttpResponseNotFound('<h1>Страница не найдена</h1>')