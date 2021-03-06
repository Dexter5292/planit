# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0011_auto_20171025_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='initial_done',
            name='username',
        ),
        migrations.AddField(
            model_name='cls_info',
            name='profile',
            field=models.ImageField(default=1, upload_to='static plan/photos/', verbose_name='profile_pic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='school_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.school_info'),
        ),
        migrations.DeleteModel(
            name='initial_done',
        ),
    ]
