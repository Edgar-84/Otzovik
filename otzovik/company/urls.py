from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('cats/', categories, name='cats'),
    path('addcompany/', add_company, name='add_company'),
    path('info/', info_about_site, name='info'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]