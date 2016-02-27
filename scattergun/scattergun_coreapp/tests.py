from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from .models import Team


class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Test Team 1", number=1)

    def test_team_created_correctly(self):
        test_team_1 = Team.objects.get(number=1)
        self.assertEqual(test_team_1.name, "Test Team 1")
        self.assertEqual(test_team_1.number, 1)


class TeamViewTestCase(TestCase):
    def test_team_views(self):
        views = ('scattergun-team-add', 'scattergun-team-list')
        client = Client()
        for view in views:
            response = self.client.get(reverse(view))
            self.assertEqual(response.status_code, 200)