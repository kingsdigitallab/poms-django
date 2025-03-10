# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-18 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pomsapp', '0003_fix_source_inheritance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assocfactoidperson',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assoc_factoid_person', to='pomsapp.Person'),
        ),
        migrations.AlterField(
            model_name='assocfactoidposs_office',
            name='factoid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assocfactoidpossoffice', to='pomsapp.Factoid'),
        ),
        migrations.AlterField(
            model_name='assochelperperson',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='helperperson', to='pomsapp.Person'),
        ),
        migrations.AlterField(
            model_name='factoid',
            name='sourcekey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factoids', to='pomsapp.Source', verbose_name='Document'),
        ),
    ]
