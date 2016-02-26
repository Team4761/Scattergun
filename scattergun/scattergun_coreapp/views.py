from django.shortcuts import render
from .models import Team

def team_view(request, team_number):
    team = Team.objects.get(number=team_number)
    return render(request, "team.html", dictionary={"team": team})