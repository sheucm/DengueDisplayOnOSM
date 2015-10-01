# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dengue_all',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=10)),
                ('zone', models.CharField(max_length=10)),
                ('road', models.CharField(max_length=30)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
