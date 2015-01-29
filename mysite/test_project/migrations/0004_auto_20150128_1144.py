# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0003_auto_20150127_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('code', models.CharField(serialize=False, max_length=1, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='province',
            name='zone',
            field=models.ForeignKey(to='test_project.Zone'),
            preserve_default=True,
        ),
    ]
