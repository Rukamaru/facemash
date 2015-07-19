# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0013_auto_20150714_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='choice',
            new_name='choices',
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
    ]
