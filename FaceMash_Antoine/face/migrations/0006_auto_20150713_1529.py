# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0005_remove_question_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='choice',
            new_name='photo',
        ),
    ]
