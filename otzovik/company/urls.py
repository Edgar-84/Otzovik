from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page.as_view(), name='home'),
    path('cats/', categories, name='cats'),
    path('addcompany/', add_company.as_view(), name='add_company'),
    path('info/', info_about_site, name='info'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post.as_view(), name='post'),
    path('category/<slug:cat_slug>/', show_category.as_view(), name='category'),
]