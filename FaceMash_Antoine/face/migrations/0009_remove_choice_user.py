# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0008_auto_20150713_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='user',
        ),
    ]
