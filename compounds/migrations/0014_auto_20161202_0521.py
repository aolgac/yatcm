# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0013_auto_20161202_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chineseidentity',
            name='compound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.Compound'),
        ),
        migrations.AlterField(
            model_name='englishidentity',
            name='compound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.Compound'),
        ),
    ]