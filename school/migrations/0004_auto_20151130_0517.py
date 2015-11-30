# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20151130_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='time_spent',
            field=models.TimeField(default=0),
        ),
    ]
