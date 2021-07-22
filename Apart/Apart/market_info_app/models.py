from django.db import models


class MarketInfoModel(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField()
    source = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    source_url = models.URLField()
