# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20151130_0523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('cover', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='assignment',
            name='instructions',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='goal',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='resource',
            field=models.ForeignKey(default='None', blank=True, to='school.Resource'),
            preserve_default=False,
        ),
    ]
