from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import Client, TestCase
from .models import Team, RoundReport, Competition
import datetime
import re
import os

TEST_PY_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Test Team 1", number=1)
        competition = Competition.objects.create(name="Who cares?", date=datetime.datetime.now())
        self.test_team_1 = Team.objects.get(number=1)
        self.competition = competition

    def test_team_created_correctly(self):
        self.test_team_1 = Team.objects.get(number=1)
        self.assertEqual(self.test_team_1.name, "Test Team 1")
        self.assertEqual(self.test_team_1.number, 1)

    def test_get_average_score(self):
        scores = (3, 4, 5, 7)
        for score in scores:
            r = RoundReport(competition=self.competition,
                            match_number=1,
                            team=self.test_team_1,
                            friendly_alliance_score=score)
            r.save()
        self.assertEqual(self.test_team_1.get_average_score(), 4.75)


class RoundReportTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Test Team 1", number=1)
        Competition.objects.create(name="Who cares?", date=datetime.datetime.now())

    def test_report_created_with_only_team_and_match_and_competition(self):
        # You should be able to create a round report with ONLY a team and a match ... and a competition
        test_team_1 = Team.objects.get(number=1)
        test_competition = Competition.objects.get(name="Who cares?")
        r = RoundReport(team=test_team_1, match_number=1, competition=test_competition)
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
