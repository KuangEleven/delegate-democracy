# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delegate_democracy', '0002_auto_20170123_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delegate_democracy.Body'),
        ),
        migrations.AlterField(
            model_name='issuecategory',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delegate_democracy.Body'),
        ),
        migrations.AlterField(
            model_name='issuetype',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delegate_democracy.Body'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delegate_democracy.Body'),
        ),
    ]