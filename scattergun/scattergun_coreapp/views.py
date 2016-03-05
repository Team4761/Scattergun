from django.shortcuts import render, get_object_or_404, redirect
from .forms import TeamForm, RoundReportForm, CompetitionForm
from .models import Team, RoundReport, Competition


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
    return render(request, "generic_form.html", context={"form": form, "thing": "competition"})


def competition_list_view(request):
    comps = Competition.objects.all()
    return render(request, "competition_list.html", context={"comps": comps})


def roundreport_add_view(request):
    if request.method == "POST":
        form = RoundReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scattergun-roundreport-list')
    else:
        form = RoundReportForm()
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
    return render(request, "generic_form.html", context={"form": form, "thing": "team"})


def team_view(request, team_number):
    team = get_object_or_404(Team, number=team_number)
    reports = RoundReport.objects.filter(team=team)
    
    pointsdataset = {}
    pointsdataset["name"] = team.number
    pointsdataset["xy"] = []
    comments = []
    
    for report in reports:
        pointsdataset["xy"].append({'x':report.match_number, 'y':report.friendly_alliance_score})
        if not report.tech_issues_comment == "":
            comments.append(report.tech_issues_comment)
    
    pointsdataset["xy"] = sorted(pointsdataset["xy"], key=lambda score: score["x"])
    
    context = {"team": team,
    "reports": reports,
    "pointsdataset": [pointsdataset],
    "comments": comments}
    
    return render(request, "team.html", context=context)
