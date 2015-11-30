# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('instructions', models.TextField(max_length=1000, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('goal', models.TextField(max_length=1000, null=True, blank=True)),
                ('display_date', models.DateField(default=datetime.date.today)),
                ('due_date', models.DateField(default=datetime.date.today)),
                ('complete', models.BooleanField(default=False, verbose_name=b'Are you finished with this assignment?')),
                ('time_spent', models.TimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Name of the resource?')),
                ('cover', models.ImageField(null=True, upload_to=None, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='resource',
            field=models.ForeignKey(blank=True, to='school.Resource', null=True),
        ),
    ]
