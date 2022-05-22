from django.db import models


class Book(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False, unique=True)
    title = models.CharField(verbose_name='題名', max_length=30)
    author = models.CharField(verbose_name='著者', max_length=30)
    price = models.IntegerField(verbose_name='価格')

