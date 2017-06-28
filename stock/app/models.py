from __future__ import unicode_literals

from django.db import models

# Create your models here.
class companynames(models.Model):
    symbol = models.CharField(max_length = 25)
    name   = models.CharField(max_length = 200)
    marketcap = models.CharField(max_length = 200)
    sector = models.CharField(max_length = 100)
    industry = models.CharField(max_length = 200)
    
class compinfo(models.Model):

    symbol = models.CharField(max_length = 25)
    tradetime = models.CharField(max_length = 200)
    tradeprice= models.CharField(max_length = 200)
