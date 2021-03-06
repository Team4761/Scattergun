from django.db import models

functionality_choices = (
    (0, "Inapplicable/Unknown/Does not work"),
    (1, "Terrible"),
    (2, "Bad"),
    (3, "OK, I guess..."),
    (4, "Good"),
    (5, "Fantastic"),
)

defenses = (
    ("Portcullis", "Portcullis"),
    ("Cheval de Frise", "Cheval de Frise"),
    ("Ramparts", "Ramparts"),
    ("Moats", "Moats"),
    ("Drawbridge", "Drawbridge"),
    ("Sally Port", "Sally Port"),
    ("Rock Wall", "Rock Wall"),
    ("Rough Terrain", "Rough Terrain")
)


class Team(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(primary_key=True)
    things_driveteam_can_do_well = models.TextField(blank=True, null=True)
    drive_team_personality_compatibility = models.IntegerField(choices=functionality_choices, blank=True, null=True)
    robot_height_in_inches = models.IntegerField(blank=True, null=True)

    def get_average_score(self):
        team_reports = RoundReport.objects.filter(team=self)
        friendly_scores = [report.friendly_alliance_score for report in team_reports]
        if len(friendly_scores) == 0:
            return 0
        return sum(friendly_scores) / float(len(friendly_scores))

    def get_max_boulders_scored_low(self):
        team_reports = RoundReport.objects.filter(team=self)
        low_goals = [report.boulders_scored_in_low for report in team_reports]
        if len(low_goals) == 0:
            return 0
        return max(low_goals)

    def lowbar_compatibility(self):
        if self.robot_height_in_inches is not None:
            return self.robot_height_in_inches < 16

    def __str__(self):
        return "#{} - {}".format(self.number, self.name)


class Competition(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} ({})".format(self.name, self.date)


class RoundReport(models.Model):
    team = models.ForeignKey(Team)
    match_number = models.IntegerField()
    competition = models.ForeignKey(Competition)

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
    tower_scaling_time = models.IntegerField(blank=True, null=True)  # in seconds

    # Defense
    low_boulders_blocked = models.IntegerField(default=0)
    high_boulders_blocked = models.IntegerField(default=0)
    notes_about_defense = models.TextField(blank=True, null=True)

    # Penalties received
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

    # Defenses
    a_defense = models.CharField(max_length=15, choices=defenses, blank=True, null=True)
    b_defense = models.CharField(max_length=15, choices=defenses, blank=True, null=True)
    c_defense = models.CharField(max_length=15, choices=defenses, blank=True, null=True)
    d_defense = models.CharField(max_length=15, choices=defenses, blank=True, null=True)

    # Defense ability
    a_defense_ability = models.IntegerField(choices=functionality_choices, blank=True, null=True)
    b_defense_ability = models.IntegerField(choices=functionality_choices, blank=True, null=True)
    c_defense_ability = models.IntegerField(choices=functionality_choices, blank=True, null=True)
    d_defense_ability = models.IntegerField(choices=functionality_choices, blank=True, null=True)

    def __str__(self):
        return "Match #{} in {} for {} (F:{}/E:{})".format(self.match_number, self.competition, self.team.name,
                                                           self.friendly_alliance_score, self.enemy_alliance_score)
