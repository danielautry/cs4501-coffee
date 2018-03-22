# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-14 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='coffeeProduct',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='coffeeApp.CoffeeProduct'),
            preserve_default=False,
        ),
    ]
