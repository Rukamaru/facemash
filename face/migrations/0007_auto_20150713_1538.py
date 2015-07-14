# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0006_auto_20150713_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.ForeignKey(to='face.User', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ForeignKey(to='face.Photo'),
        ),
    ]
