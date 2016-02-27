from django.shortcuts import render, get_object_or_404
from .models import Team


def team_view(request, team_number):
    team = get_object_or_404(Team, number=team_number)
    return render(request, "team.html", dictionary={"team": team})