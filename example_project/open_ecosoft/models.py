from django.db import models
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy_djangoitem import DjangoItem
# from scrapy_django_dashboard.models import Scraper, SchedulerRuntime
from six import python_2_unicode_compatible
import json
# Create your models here.

from django.utils import timezone


class ScrapyItemModel(models.Model):
    sn = models.CharField(max_length=100, null=True)
    trade_code = models.CharField(max_length=100, null=True)
    cat = models.CharField(max_length=100, null=True)
    ltp = models.CharField(max_length=100, null=True)
    change = models.CharField(max_length=100, null=True)
    change_persent = models.CharField(max_length=100, null=True)
    value = models.CharField(max_length=100, null=True)
    volume = models.CharField(max_length=100, null=True)
    trade = models.CharField(max_length=100, null=True)
    high = models.CharField(max_length=100, null=True)
    low = models.CharField(max_length=100, null=True)
    open = models.CharField(max_length=100, null=True)
    ycp = models.CharField(max_length=100, null=True)
    # pe = models.CharField(max_length=100, null=True)
    # spot = models.CharField(max_length=100, null=True)
    # sector = models.CharField(max_length=100, null=True)
    # record_date = models.DateTimeField()
    # dividend = models.CharField(max_length=100, null=True)
    # analysis = models.CharField(max_length=100, null=True)

    # @property
    # def to_dict(self):
    #     data = {
    #         'data': json.loads(self.data),
    #         'date': self.date
    #     }
    #     return data
    #
    # def __str__(self):
    #     return self.unique_id