from django.shortcuts import render, get_object_or_404, redirect
from .forms import TeamForm, RoundReportForm
from .models import Team, RoundReport


def index_view(request):
    return render(request, "index.html")


def roundreport_add_view(request):
    if request.method == "POST":
        form = RoundReportForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect('scattergun-index')
    else:
        form = RoundReportForm()
    return render(request, "team_add.html", context={"form": form})


def roundreport_list_view(request):
    reports = RoundReport.objects.all()
    return render(request, "roundreport_list.html", context={"reports": reports})


def team_list_view(request):
    teams = Team.objects.all()
    return render(request, "team_list.html", context={"teams": teams})


def team_add_view(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect('scattergun-team-show', team_number=team.number)
    else:
        form = TeamForm()
    return render(request, "team_add.html", context={"form": form})


def team_view(request, team_number):
    team = get_object_or_404(Team, number=team_number)
    return render(request, "team.html", context={"team": team})