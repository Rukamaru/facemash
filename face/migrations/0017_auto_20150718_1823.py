# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0016_auto_20150718_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
