from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import numpy
from .admin import RoundReportResource, TeamResource, CompetitionResource
from .forms import TeamForm, RoundReportForm, CompetitionForm
from .models import Team, RoundReport, Competition


def index_view(request):
    return render(request, "index.html")


def leaderboard_avg_score_view(request):
    teams = Team.objects.all()
    sort = sorted(teams, key=lambda team: -team.get_average_score())
    return render(request, "leaderboards/avg_alliance_score.html", context={"teams": sort,
                                                                            "thing": "Average alliance score"})


def leaderboard_max_low_boulders(request):
    teams = Team.objects.all()
    sort = sorted(teams, key=lambda team: -team.get_max_boulders_scored_low())
    return render(request, "leaderboards/max_low_boulders.html", context={"teams": sort,
                                                                          "thing": "Max boulders scored in low goal"})


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


def competition_show_view(request, comp_number):
    comp = get_object_or_404(Competition, pk=comp_number)
    reports = RoundReport.objects.all().filter(competition=comp)
    teams = [report.team for report in reports]
    sort = set(sorted(teams, key=lambda team: -team.get_average_score()))
    return render(request, "competition.html", context={"reports": reports, "teams": sort})


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


def roundreport_show_view(request, report):
    report = get_object_or_404(RoundReport, pk=report)
    return render(request, "roundreport.html", context={"report": report})


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

    print([report["a_defense_ability"] for report in RoundReport.objects.filter(team=team, a_defense="Portcullis").values()])
    abilities = {
        "portcullis": numpy.mean([report["a_defense_ability"] for report in RoundReport.objects.filter(team=team, a_defense="Portcullis").values()]),
        "cheval_de_frise": numpy.mean([report["a_defense_ability"] for report in RoundReport.objects.filter(team=team, a_defense="Cheval de Frise").values()]),
        "ramparts": numpy.mean([report["b_defense_ability"] for report in RoundReport.objects.filter(team=team, b_defense="Ramparts").values()]),
        "moats": numpy.mean([report["b_defense_ability"] for report in RoundReport.objects.filter(team=team, b_defense="Moats").values()]),
        "drawbridge": numpy.mean([report["c_defense_ability"] for report in RoundReport.objects.filter(team=team, c_defense="Drawbridge").values()]),
        "sally_port": numpy.mean([report["c_defense_ability"] for report in RoundReport.objects.filter(team=team, c_defense="Sally Port").values()]),
        "rock_wall": numpy.mean([report["d_defense_ability"] for report in RoundReport.objects.filter(team=team, d_defense="Rock Wall").values()]),
        "rough_terrain": numpy.mean([report["d_defense_ability"] for report in RoundReport.objects.filter(team=team, d_defense="Rough Terrain").values()]),
    }
    pointsdataset = {
        "name": team.number,
        "xy": [],
    }
    comments = []

    for report in reports:
        pointsdataset["xy"].append({'x': report.match_number, 'y': report.friendly_alliance_score})
        if not report.tech_issues_comment == "":
            comments.append(report.tech_issues_comment)

    pointsdataset["xy"] = sorted(pointsdataset["xy"], key=lambda score: score["x"])

    context = {
        "team": team,
        "reports": reports,
        "pointsdataset": [pointsdataset],
        "comments": comments,
        "abilities": abilities,
    }

    return render(request, "team.html", context=context)


def export_roundreport_view(request, target):
    all = RoundReportResource().export()
    content_type = None
    data = None
    print(target)
    if target == "csv":
        data = all.csv
        content_type = "text/plain"
    elif target == "xlsx":
        data = all.xlsx
        content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    else:
        return HttpResponse("Unrecognized format", status=500)
    return HttpResponse(data, content_type=content_type)


def export_team_view(request, target):
    all = TeamResource().export()
    content_type = None
    data = None
    print(target)
    if target == "csv":
        data = all.csv
        content_type = "text/plain"
    elif target == "xlsx":
        data = all.xlsx
        content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    else:
        return HttpResponse("Unrecognized format", status=500)
    return HttpResponse(data, content_type=content_type)


def export_competition_view(request, target):
    all = CompetitionResource().export()
    content_type = None
    data = None
    print(target)
    if target == "csv":
        data = all.csv
        content_type = "text/plain"
    elif target == "xlsx":
        data = all.xlsx
        content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    else:
        return HttpResponse("Unrecognized format", status=500)
    return HttpResponse(data, content_type=content_type)


def export_index_view(request):
    return render(request, "export.html")
