# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0004_auto_20150713_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
    ]
