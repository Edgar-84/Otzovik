# Generated by Django 3.2.7 on 2021-10-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='url_for_site',
            field=models.URLField(max_length=255, null=True, verbose_name='Ссылка на сайт компании'),
        ),
    ]
