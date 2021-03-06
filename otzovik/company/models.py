from django.db import models
from django.urls import reverse


class Company(models.Model):
    """This table will store all the information about the companies"""

    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    url_for_site = models.URLField(max_length=255, null=True, verbose_name='Ссылка на сайт компании')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    content = models.TextField(verbose_name="Описание")
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Компании'
        verbose_name_plural = 'Компании'
        ordering = ['-time_create', 'title']

class Category(models.Model):
    """This table with category of company"""

    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']