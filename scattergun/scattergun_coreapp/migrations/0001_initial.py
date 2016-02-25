# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoundReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendly_alliance_score', models.IntegerField(default=0)),
                ('enemy_alliance_score', models.IntegerField(default=0)),
                ('friendly_alliance_rank_points', models.IntegerField(default=0)),
                ('enemy_alliance_rank_points', models.IntegerField(default=0)),
                ('boulders_scored_in_low', models.IntegerField(default=0)),
                ('boulders_scored_in_high', models.IntegerField(default=0)),
                ('can_scale_tower', models.BooleanField(default=False)),
                ('tower_scaling_ability', models.IntegerField(blank=True, choices=[(0, 'Inapplicable/Unknown/Does not work'), (1, 'Terrible'), (2, 'Bad'), (3, 'OK, I guess...'), (4, 'Good'), (5, 'Fantastic')], null=True)),
                ('tower_scaling_time', models.IntegerField(blank=True, null=True)),
                ('low_boulders_blocked', models.IntegerField(default=0)),
                ('high_boulders_blocked', models.IntegerField(default=0)),
                ('notes_about_defense', models.TextField(blank=True, null=True)),
                ('foul_count', models.IntegerField(default=0)),
                ('technical_foul_count', models.IntegerField(default=0)),
                ('yellow_card_count', models.IntegerField(default=0)),
                ('red_card_count', models.IntegerField(default=0)),
                ('got_stuck', models.BooleanField(default=False)),
                ('lost_connection', models.BooleanField(default=False)),
                ('lost_control', models.BooleanField(default=False)),
                ('tech_issues_comment', models.TextField(blank=True, null=True)),
                ('speed', models.IntegerField(blank=True, choices=[(0, 'Inapplicable/Unknown/Does not work'), (1, 'Terrible'), (2, 'Bad'), (3, 'OK, I guess...'), (4, 'Good'), (5, 'Fantastic')], null=True)),
                ('maneuverability', models.IntegerField(blank=True, choices=[(0, 'Inapplicable/Unknown/Does not work'), (1, 'Terrible'), (2, 'Bad'), (3, 'OK, I guess...'), (4, 'Good'), (5, 'Fantastic')], null=True)),
                ('pushing_power', models.IntegerField(blank=True, choices=[(0, 'Inapplicable/Unknown/Does not work'), (1, 'Terrible'), (2, 'Bad'), (3, 'OK, I guess...'), (4, 'Good'), (5, 'Fantastic')], null=True)),
                ('driveteam_maneuvering_skill', models.IntegerField(blank=True, choices=[(0, 'Inapplicable/Unknown/Does not work'), (1, 'Terrible'), (2, 'Bad'), (3, 'OK, I guess...'), (4, 'Good'), (5, 'Fantastic')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('things_driveteam_can_do_well', models.TextField(blank=True, null=True)),
                ('drive_team_personality_compatibility', models.IntegerField(blank=True, choices=[(0, 'Inapplicable/Unknown/Does not work'), (1, 'Terrible'), (2, 'Bad'), (3, 'OK, I guess...'), (4, 'Good'), (5, 'Fantastic')], null=True)),
                ('robot_height_in_inches', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='roundreport',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scattergun_coreapp.Team'),
        ),
    ]