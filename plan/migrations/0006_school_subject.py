# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 07:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plan', '0005_auto_20171022_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='school_subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periods', models.IntegerField(default=4)),
                ('grade', models.CharField(max_length=50)),
                ('prac', models.BooleanField(default=False)),
                ('ratio', models.CharField(max_length=20)),
                ('syllabus', models.CharField(max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.school_info')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
