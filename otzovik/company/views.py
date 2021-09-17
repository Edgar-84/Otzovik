from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView

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
    context_object_name = 'post'

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

def add_company(request):
    """This handler for add company"""

    if request.method == 'POST':
        form = add_company_form(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = add_company_form()
    return render(request, 'company/addcompany.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def info_about_site(request):

    return HttpResponse('Информация о сайте')

def login(request):
    """This handler for login users"""

    return HttpResponse('Регистрация пользователя')

def show_post(request, post_slug):
    """This handler for show post"""
    post = get_object_or_404(Company, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'company/post.html', context=context)

def show_category(request, cat_slug):
    """This handler for displaying category"""

    # if len(post) == 0:
    #      raise Http404()
    #name_category = Category.name(pk=cat_id)
    context = {
        'menu': menu,
        'title': 'Выбранная категория',
        'cat_selected': cat_slug,
    }
    return render(request, 'company/index.html', context=context)



def pageNotFound(request, exception):
    """This error handler 404 """

    return HttpResponseNotFound('<h1>Страница не найдена</h1>')