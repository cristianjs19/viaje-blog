# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'No title', max_length=50)),
                ('photo', models.ImageField(upload_to=b'photos/')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('favorite', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=200, blank=True)),
                ('category', models.ForeignKey(blank=True, to='album.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
