# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20151130_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='goal',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='resource',
            field=models.ForeignKey(blank=True, to='school.Resource', null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='time_spent',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='cover',
            field=models.ImageField(null=True, upload_to=None, blank=True),
        ),
    ]
