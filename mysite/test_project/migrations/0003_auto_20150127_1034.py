# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0002_provincia_zona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('code', models.CharField(primary_key=True, serialize=False, max_length=50)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('code', models.CharField(primary_key=True, serialize=False, max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('zone', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='provincia',
        ),
        migrations.DeleteModel(
            name='Municipio',
        ),
        migrations.DeleteModel(
            name='Provincia',
        ),
        migrations.AddField(
            model_name='municipality',
            name='province',
            field=models.ForeignKey(to='test_project.Province'),
            preserve_default=True,
        ),
    ]
