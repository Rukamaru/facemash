# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0002_auto_20150713_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='choice',
            field=models.ManyToManyField(to='face.Choice'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.OneToOneField(to='face.Choice'),
        ),
    ]
