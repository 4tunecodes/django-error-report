# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='type')),
                ('info', models.TextField()),
                ('data', models.TextField(blank=True, null=True)),
                ('path', models.URLField(blank=True, null=True)),
                ('when', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('html', models.TextField(blank=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Error',
                'verbose_name_plural': 'Errors',
            },
        ),
    ]
