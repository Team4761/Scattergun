from django.shortcuts import render, get_object_or_404, redirect
from .forms import TeamForm, RoundReportForm, CompetitionSelectForm, MatchForm, CompetitionForm
from .models import Team, RoundReport, Competition, Match


def index_view(request):
    return render(request, "index.html")


def avg_score_leaderboard_view(request):
    teams = Team.objects.all()
    sort = sorted(teams, key=lambda team: -team.get_average_score())
    return render(request, "leaderboard.html", context={"teams": sort})


def competition_add_view(request):
    if request.method == "POST":
        form = CompetitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scattergun-index')
    else:
        form = CompetitionForm()
    return render(request, "match_list.html", context={"form": form, "thing": "competition"})


def competition_list_view(request):
    comps = Competition.objects.all()
    return render(request, "competition_list.html", context={"comps": comps})


def competition_select_view(request):
    if request.method == "POST":
        form = CompetitionSelectForm(request.POST)
        if form.is_valid():
            request.session["competition"] = form.cleaned_data["competition"]
            return redirect('scattergun-roundreport-add')
    else:
        form = CompetitionSelectForm()
    return render(request, "competition_select.html", context={"form": form})


def match_add_view(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scattergun-index')
    else:
        form = MatchForm()
    return render(request, "match_list.html", context={"form": form, "thing": "match"})


def match_list_view(request):
    matches = Match.objects.all()
    return render(request, "match_list.html", context={"matches": matches})


def roundreport_add_view(request):
    if request.method == "POST":
        form = RoundReportForm(None, request.POST)
        if form.is_valid():
            form.save()
            return redirect('scattergun-roundreport-list')
    else:
        form = RoundReportForm(request.session.get("competition"))
    return render(request, "roundreport_add.html", context={"form": form})


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
    return render(request, "match_list.html", context={"form": form, "thing": "team"})


def team_view(request, team_number):
    team = get_object_or_404(Team, number=team_number)
    reports = RoundReport.objects.filter(team=team)
    return render(request, "team.html", context={"team": team, "reports": reports})
