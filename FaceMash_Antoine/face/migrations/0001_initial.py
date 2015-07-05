# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('note', models.IntegerField()),
                ('synopsis', models.TextField(null=True)),
                ('date_sortie', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
            ],
        ),
    ]
