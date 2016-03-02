from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from .models import Team, RoundReport, Match, Competition
import datetime


class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Test Team 1", number=1)

    def test_team_created_correctly(self):
        test_team_1 = Team.objects.get(number=1)
        self.assertEqual(test_team_1.name, "Test Team 1")
        self.assertEqual(test_team_1.number, 1)


class TeamViewTestCase(TestCase):
    def setUp(self):
        self.views = ('scattergun-team-add', 'scattergun-team-list')
        self.client = Client()

    def test_team_views(self):
        for view in self.views:
            response = self.client.get(reverse(view))
            self.assertEqual(response.status_code, 200)


class RoundReportTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Test Team 1", number=1)
        competition = Competition.objects.create(name="Who cares?",date=datetime.datetime.now())
        Match.objects.create(number=1, competition = competition)

    def test_report_created_with_only_team(self):
        # You should be able to create a round report with ONLY a team
        test_team_1 = Team.objects.get(number=1)
        match = Match.objects.get(number=1) # The competition is irrelevant.
        r = RoundReport(team=test_team_1,match=match)
        r.save()


class RoundReportViewTestCase(TestCase):
    def setUp(self):
        self.views = ('scattergun-roundreport-add', 'scattergun-roundreport-list')
        self.client = Client()

    def test_roundreport_views(self):
        for view in self.views:
            response = self.client.get(reverse(view))
            self.assertEqual(response.status_code, 200)
