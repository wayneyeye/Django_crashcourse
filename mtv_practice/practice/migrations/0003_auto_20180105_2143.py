# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[(b'S', b'Small'), (b'L', b'Large'), (b'XL', b'Extra Large')], max_length=2),
        ),
    ]
