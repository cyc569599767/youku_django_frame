# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-07-27 13:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='uid',
        ),
        migrations.AlterField(
            model_name='history',
            name='down_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 27, 21, 39, 6, 488379), verbose_name='下载日期'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='up_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 27, 21, 39, 6, 491882), verbose_name='上传日期'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 27, 21, 39, 6, 490881), verbose_name='发布日期'),
        ),
    ]
