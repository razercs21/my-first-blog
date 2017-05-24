# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('picture', models.ImageField(upload_to='media/courses/pictures')),
            ],
        ),
    ]
