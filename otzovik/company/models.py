from django.db import models

class Company(models.Model):
    """This table will store all the information about the companies"""

    title = models.CharField(max_length=100)
    url_for_site = models.URLField(max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
