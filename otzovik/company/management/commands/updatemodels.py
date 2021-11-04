from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand
import pandas as pd
from company.models import Company
from urllib.parse import urlparse
import urllib.request


class Command(BaseCommand):
    help = 'import booms'

    def image_converter(self, url):
        """ This function can converter url on photo in photo to database """

        company = Company()
        if url == 'No logo':
            return
        else:
            name = urlparse(url).path.split('/')[-1]
            tmpfile, _ = urllib.request.urlretrieve(url)
            company.photo = SimpleUploadedFile(name, open(tmpfile, 'rb').read())
            return company.photo



    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        """ This function converts data from json to database """

        df = pd.read_json('avtomobilnyj_biznes.json')
        for title, url, photo, content in zip(df.title, df.url_for_site, df.photo, df.content):
            models = Company(title=title, url_for_site=url, photo=self.image_converter(photo), content=content)
            models.save()