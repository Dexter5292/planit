# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 09:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plan', '0007_school_subject_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='cls_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=30)),
                ('grade', models.CharField(max_length=5)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.school_info')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.subject_info')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='topics',
            fields=[
                ('topic_number', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.subject_info')),
            ],
        ),
    ]