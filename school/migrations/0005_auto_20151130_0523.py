# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20151130_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='goal',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='time_spent',
            field=models.TimeField(blank=True),
        ),
    ]
