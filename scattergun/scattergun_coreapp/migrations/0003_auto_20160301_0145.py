# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scattergun_coreapp', '0002_auto_20160225_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('blue_team', models.ManyToManyField(related_name='red', to='scattergun_coreapp.Team')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scattergun_coreapp.Competition')),
                ('red_team', models.ManyToManyField(related_name='blue', to='scattergun_coreapp.Team')),
            ],
        ),
        migrations.AlterField(
            model_name='roundreport',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scattergun_coreapp.Team'),
        ),
        migrations.AddField(
            model_name='roundreport',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scattergun_coreapp.Match'),
        ),
    ]
