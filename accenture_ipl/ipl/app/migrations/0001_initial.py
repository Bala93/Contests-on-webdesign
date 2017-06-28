# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-17 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matchinfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('season', models.TextField()),
                ('city', models.TextField()),
                ('date', models.TextField()),
                ('team1', models.TextField()),
                ('team2', models.TextField()),
                ('toss_winner', models.TextField()),
                ('toss_decision', models.TextField()),
                ('result', models.TextField()),
                ('dl_applied', models.TextField()),
                ('winner', models.TextField()),
                ('win_by_runs', models.TextField()),
                ('win_by_wickets', models.TextField()),
                ('player_of_match', models.TextField()),
                ('venue', models.TextField()),
                ('umpire1', models.TextField()),
                ('umpire2', models.TextField()),
                ('umpire3', models.TextField()),
            ],
        ),
    ]