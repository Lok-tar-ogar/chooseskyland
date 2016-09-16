# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160912_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length='100', verbose_name='合作伙伴名字')),
                ('link', models.CharField(blank=True, max_length='1000', verbose_name='合作伙伴链接', null=True)),
                ('Image', models.FileField(upload_to='core/static/img/', verbose_name='上传合作伙伴Logo')),
                ('dimDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '合作伙伴',
                'ordering': ['-dimDate'],
                'verbose_name': '合作伙伴',
            },
        ),
    ]
