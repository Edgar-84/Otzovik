from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', main_page.as_view(), name='home'),
    path('cats/', categories.as_view(), name='cats'),
    path('addcompany/', add_company.as_view(), name='add_company'),
    path('info/', info_about_site, name='info'),
    path('login/', login_user.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', Register_user.as_view(), name='register'),
    path('post/<slug:post_slug>/', show_post.as_view(), name='post'),
    path('category/<slug:cat_slug>/', show_category.as_view(), name='category'),
    path('contact/', contant_form.as_view(), name='contact'),
]