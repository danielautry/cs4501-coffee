# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-14 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeApp', '0002_sale_coffeeproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cardNumber',
            field=models.CharField(max_length=100),
        ),
    ]