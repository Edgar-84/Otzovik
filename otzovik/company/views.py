from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class main_page(DataMixin, ListView):
    """This class shows the main page"""
    model = Company
    template_name = 'company/index.html'
    context_object_name = 'companies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        """This method shows only the published ones"""

        return Company.objects.filter(is_published=True).select_related('cat')


class categories(DataMixin, ListView):
    """This class displays a page with categories"""

    model = Company
    template_name = 'company/categories.html'
    context_object_name = 'companies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категории компаний', cat_selected=0)
        return dict(list(context.items()) + list(c_def.items()))
# def categories(request):
#     """This categories of company handler"""
#
#     context = {
#         'menu': menu,
#         'title': "Категории компаний",
#         'cat_selected': 0,
#     }
#     return render(request, 'company/categories.html', context=context)


class add_company(LoginRequiredMixin, DataMixin, CreateView):
    """This class allows you to register new companies"""

    form_class = add_company_form
    template_name = 'company/addcompany.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


def info_about_site(request):
    return HttpResponse('Информация о сайте')


class show_post(DataMixin, DetailView):
    """This class shows the publication"""

    model = Company
    template_name = 'company/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'].title)
        return dict(list(context.items()) + list(c_def.items()))

class show_category(DataMixin, ListView):
    """This class filters and shows companies by category"""

    model = Company
    template_name = 'company/index.html'
    context_object_name = 'companies'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        """This method filters companies by categories and publications"""

        return Company.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

class Register_user(DataMixin, CreateView):
    """This class performs user register his account"""

    form_class = register_user_form
    template_name = 'company/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        """This method will redirect the user to the main page upon successful registration"""
        user = form.save()
        login(self.request, user)
        return redirect('home')

class login_user(DataMixin, LoginView):
    """This class performs user login to the account"""

    form_class = login_user_form
    template_name = 'company/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        """This method will redirect the user to the main page"""

        return reverse_lazy('home')

def logout_user(request):
    """This method will redirect the user to the login form when he logs out of his account"""

    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    """This error handler 404 """

    return HttpResponseNotFound('<h1>Страница не найдена</h1>')