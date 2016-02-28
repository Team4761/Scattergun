from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from .models import Team, RoundReport


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

    def test_report_created_with_only_team(self):
        # You should be able to create a round report with ONLY a team
        test_team_1 = Team.objects.get(number=1)
        r = RoundReport(team=test_team_1)
        r.save()


class RoundReportViewTestCase(TestCase):
    def setUp(self):
        self.views = ('scattergun-roundreport-add', 'scattergun-roundreport-list')
        self.client = Client()

    def test_roundreport_views(self):
        for view in self.views:
            response = self.client.get(reverse(view))
            self.assertEqual(response.status_code, 200)