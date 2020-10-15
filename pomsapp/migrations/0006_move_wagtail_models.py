# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-10 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('pomsapp', '0005_wagtail_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='richtextpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
        migrations.DeleteModel(
            name='IndexPage',
        ),
        migrations.DeleteModel(
            name='RichTextPage',
        ),
    ]