# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provincia',
            name='zona',
            field=models.CharField(max_length=50, default=1),
            preserve_default=False,
        ),
    ]
