# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0014_auto_20150715_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='choices',
            new_name='choice',
        ),
    ]
