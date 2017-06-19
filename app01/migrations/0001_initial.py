# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='host',
            fields=[
                ('nid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=64)),
                ('ip', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.business')),
            ],
        ),
    ]
