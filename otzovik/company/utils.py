from .models import *
from django.core.cache import cache

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Категории компаний", 'url_name': 'cats'},
        {'title': "Добавить компанию", 'url_name': 'add_company'},
        {'title': "Информация о сайте", 'url_name': 'info'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        """This method makes an access to the database, adds new information
         to the cache if it is not there"""

        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.all()
            cache.set('cats', cats, 60)

        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context