from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Matchinfo(models.Model):
	id = models.IntegerField(primary_key=True)
	season = models.TextField()
	city= models.TextField()
	date= models.TextField()
	team1= models.TextField()
	team2= models.TextField()
	toss_winner= models.TextField()
	toss_decision= models.TextField()
	result= models.TextField()
	dl_applied= models.TextField()
	winner= models.TextField()
	win_by_runs= models.TextField()
	win_by_wickets= models.TextField()
	player_of_match= models.TextField()
	venue= models.TextField()
	umpire1= models.TextField()
	umpire2= models.TextField()
	umpire3= models.TextField()
