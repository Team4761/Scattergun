from django.test import TestCase
from .models import Team


class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Test Team 1", number=1)

    def test_team_created_correctly(self):
        test_team_1 = Team.objects.get(number=1)
        self.assertEqual(test_team_1.name, "Test Team 1")
        self.assertEqual(test_team_1.number, 1)