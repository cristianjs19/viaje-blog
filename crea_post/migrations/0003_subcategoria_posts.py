# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-10 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crea_post', '0002_auto_20170709_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoria',
            name='posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crea_post.Post'),
        ),
    ]
