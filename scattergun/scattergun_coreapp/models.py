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

    def lowbar_compatibility(self):
        if self.robot_height_in_inches is not None:
            return self.robot_height_in_inches < 16

    def __str__(self):
        return "#{} - {}".format(self.number, self.name)


class Competition(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)


class Match(models.Model):
    number = models.IntegerField()
    competition = models.ForeignKey(Competition)
    blue_team = models.ManyToManyField(Team, related_name="red")
    red_team = models.ManyToManyField(Team, related_name="blue")

    def get_red_score(self):
        total_score = 0
        total_reports = 0
        for team in self.red_team.all():
            report = RoundReport.objects.all().filter(match=self, team=team)[1]
            total_score += report.friendly_alliance_score
            total_reports += 1
        return total_score/total_reports

    def get_blue_score(self):
        total_score = 0
        total_reports = 0
        for team in self.blue_team.all():
            report = RoundReport.objects.all().filter(match=self, team=team)[1]
            total_score += report.friendly_alliance_score
            total_reports += 1
        return total_score/total_reports

    def get_red_rank(self):
        total_score = 0
        total_reports = 0
        for team in self.red_team.all():
            report = RoundReport.objects.all().filter(match=self, team=team)[1]
            total_score += report.friendly_alliance_rank_points
            total_reports += 1
        return total_score/total_reports

    def get_blue_rank(self):
        total_score = 0
        total_reports = 0
        for team in self.blue_team.all():
            report = RoundReport.objects.all().filter(match=self, team=team)[1]
            total_score += report.friendly_alliance_rank_points
            total_reports += 1
        return total_score/total_reports


class RoundReport(models.Model):
    team = models.ForeignKey(Team)
    match = models.ForeignKey(Match)

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
