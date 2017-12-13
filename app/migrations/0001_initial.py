# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Process_ID', models.IntegerField()),
                ('start_time', models.CharField(max_length=30)),
                ('end_time', models.CharField(max_length=30)),
            ],
        ),
    ]
