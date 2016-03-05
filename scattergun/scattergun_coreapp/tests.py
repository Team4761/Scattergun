from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import Client, TestCase
from .models import Team, RoundReport, Match, Competition
import datetime
import re
import os

TEST_PY_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Test Team 1", number=1)
        self.test_team_1 = Team.objects.get(number=1)

    def test_team_created_correctly(self):
        self.test_team_1 = Team.objects.get(number=1)
        self.assertEqual(self.test_team_1.name, "Test Team 1")
        self.assertEqual(self.test_team_1.number, 1)

    def test_get_average_score(self):
        scores = (3, 4, 5, 7)
        for score in scores:
            competition = Competition(name="Who cares?", date=datetime.datetime.now())
            competition.save()
            match = Match(competition=competition, number=1)
            match.save()
            r = RoundReport(team=self.test_team_1, friendly_alliance_score=score, match=match)
            r.save()
        self.assertEqual(self.test_team_1.get_average_score(), 4.75)


class RoundReportTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Test Team 1", number=1)
        competition = Competition.objects.create(name="Who cares?", date=datetime.datetime.now())
        Match.objects.create(number=1, competition=competition)

    def test_report_created_with_only_team(self):
        # You should be able to create a round report with ONLY a team
        test_team_1 = Team.objects.get(number=1)
        match = Match.objects.get(number=1)  # The competition is irrelevant.
        r = RoundReport(team=test_team_1, match=match)
        r.save()


class TestViews(TestCase):
    def setUp(self):
        self.views = []
        with open(os.path.join(TEST_PY_BASE_DIR, "scattergun_coreapp", "urls.py")) as f:
            for line in f.readlines():
                if "'" in line:
                    raise Exception("' character found in urls.py")
                match = re.search(r'name="([A-Za-z-]+)"', line)
                if match is not None:
                    self.views.append(match.group(1))
        self.client = Client()

    def test_views(self):
        for view in self.views:
            try:
                response = self.client.get(reverse(view))
                self.assertEqual(response.status_code, 200)
            except NoReverseMatch:
                pass
