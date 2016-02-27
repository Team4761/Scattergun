from django.shortcuts import render, get_object_or_404
from .models import Team


def team_list_view(request):
    teams = Team.objects.all()
    return render(request, "team_list.html", context={"teams": teams})


def team_view(request, team_number):
    team = get_object_or_404(Team, number=team_number)
    return render(request, "team.html", context={"team": team})