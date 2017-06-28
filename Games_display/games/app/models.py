from __future__ import unicode_literals

from django.db import models

# Create your models here.

class gamelist(models.Model):
	title = models.CharField(max_length = 56)
	platform = models.CharField(max_length = 16)
	score = models.DecimalField(max_digits=2,decimal_places = 1)
	genre = models.CharField(max_length = 17)
	editors_choice = models.CharField(max_length=1)
