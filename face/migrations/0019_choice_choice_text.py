# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0018_auto_20150718_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(null=True, verbose_name='Choice', max_length=200),
        ),
    ]
