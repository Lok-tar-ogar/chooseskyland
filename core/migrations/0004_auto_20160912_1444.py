# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-12 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160912_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsimg',
            name='apktype',
        ),
        migrations.AlterField(
            model_name='newsimg',
            name='Linkto',
            field=models.CharField(blank=True, max_length=100, verbose_name='链接地址'),
        ),
    ]
