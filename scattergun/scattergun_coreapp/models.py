from django.db import models

functionality_choices = (
	(0, "Inapplicable/Unknown/Does not work"),
	(1, "Terrible"),
	(2, "Bad"),
	(3, "OK, I guess..."),
	(4, "Good"),
	(5, "Fantastic"),
)

class Team(models.Model):
	name = models.CharField(max_length=100)
	number = models.IntegerField()
	things_driveteam_can_do_well = models.TextField(blank=True, null=True)
	drive_team_personality_compatibility = models.IntegerField(choices=functionality_choices, blank=True, null=True)
	robot_height_in_inches = models.IntegerField(blank=True, null=True)

class RoundReport(models.Model):
	team = models.ForeignKey(Team)
	
	# Round information
	friendly_alliance_score = models.IntegerField(default=0)
	enemy_alliance_score = models.IntegerField(default=0)
	friendly_alliance_rank_points = models.IntegerField(default=0)
	enemy_alliance_rank_points = models.IntegerField(default=0)
	
	# Point scoring activities
	boulders_scored_in_low = models.IntegerField(default=0)
	boulders_scored_in_high = models.IntegerField(default=0)
	can_scale_tower = models.BooleanField(default=False)
	tower_scaling_ability = models.IntegerField(choices=functionality_choices, blank=True, null=True)
	tower_scaling_time = models.IntegerField(blank=True, null=True) # in seconds
	
	# Defense
	low_boulders_blocked = models.IntegerField(default=0)
	high_boulders_blocked = models.IntegerField(default=0)
	notes_about_defense = models.TextField(blank=True, null=True)
	
	# Penalties recieved
	foul_count = models.IntegerField(default=0)
	technical_foul_count = models.IntegerField(default=0)
	yellow_card_count = models.IntegerField(default=0)
	red_card_count = models.IntegerField(default=0)
	
	# Breakdown/Technical Issues
	got_stuck = models.BooleanField(default=False)
	lost_connection = models.BooleanField(default=False)
	lost_control = models.BooleanField(default=False)
	tech_issues_comment = models.TextField(blank=True, null=True)

	# General
	speed = models.IntegerField(choices=functionality_choices, blank=True, null=True)
	maneuverability = models.IntegerField(choices=functionality_choices, blank=True, null=True)
	pushing_power = models.IntegerField(choices=functionality_choices, blank=True, null=True)
	
	# Drive team ratings
	driveteam_maneuvering_skill = models.IntegerField(choices=functionality_choices, blank=True, null=True)
