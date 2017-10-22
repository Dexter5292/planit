# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_auto_20171022_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school_info',
            name='sch_period_num',
        ),
        migrations.AddField(
            model_name='school_info',
            name='sch_table_span',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='school_info',
            name='sch_period_length',
            field=models.IntegerField(default=30),
        ),
    ]