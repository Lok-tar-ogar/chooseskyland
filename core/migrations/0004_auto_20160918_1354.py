# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='合作伙伴链接'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, verbose_name='合作伙伴名字'),
        ),
    ]