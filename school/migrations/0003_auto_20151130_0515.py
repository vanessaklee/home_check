# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20151130_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='display_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
