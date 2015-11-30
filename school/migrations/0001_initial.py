# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('goal', models.CharField(max_length=255)),
                ('display_date', models.DateTimeField(verbose_name=b'display date')),
                ('complete', models.BooleanField(default=False, verbose_name=b'Are you finished with this assignment?')),
                ('time_spent', models.IntegerField(default=0)),
            ],
        ),
    ]
