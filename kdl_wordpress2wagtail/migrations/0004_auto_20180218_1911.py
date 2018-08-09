# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-18 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kdl_wordpress2wagtail', '0003_kdlwordpressreference_imported'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kdlwordpressreference',
            name='imported',
        ),
        migrations.AddField(
            model_name='kdlwordpressreference',
            name='protected',
            field=models.BooleanField(default=False),
        ),
    ]