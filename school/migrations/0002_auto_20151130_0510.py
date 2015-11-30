# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='display_date',
            field=models.DateTimeField(default=b'2015-11-30T05:10:07.789911'),
        ),
    ]
