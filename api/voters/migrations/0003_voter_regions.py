# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0002_regions'),
        ('voters', '0002_election_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='regions',
            field=models.ManyToManyField(blank=True, to='elections.Region'),
        ),
    ]
