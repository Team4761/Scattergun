from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"competitions/$", views.competition_list_view, name="scattergun-competition-list"),
    url(r"competitions/add/", views.competition_add_view, name="scattergun-competition-add"),
    url(r"competitions/(?P<comp_number>\d+)", views.competition_show_view, name="scattergun-competition-show"),

    url(r"export/roundreports.(?P<target>\w+)$", views.export_roundreport_view, name="scattergun-export-roundreports"),
    url(r"export/teams.(?P<target>\w+)$", views.export_team_view, name="scattergun-export-teams"),
    url(r"export/competitions.(?P<target>\w+)$", views.export_competition_view, name="scattergun-export-competitions"),
    url(r"export/", views.export_index_view, name="scattergun-export-index"),

    url(r"leaderboards/avg_alliance_score", views.leaderboard_avg_score_view, name="scattergun-avg-score-leaderboard"),
    url(r"leaderboards/max_low_boulders", views.leaderboard_max_low_boulders,
        name="scattergun-max-low-boulders-leaderboard"),

    url(r"roundreports/add", views.roundreport_add_view, name="scattergun-roundreport-add"),
    url(r"roundreports/$", views.roundreport_list_view, name="scattergun-roundreport-list"),
    url(r"roundreports/(?P<report>\d+)", views.roundreport_show_view, name="scattergun-roundreport-show"),

    url(r"teams/$", views.team_list_view, name="scattergun-team-list"),
    url(r"teams/add/", views.team_add_view, name="scattergun-team-add"),
    url(r"teams/(?P<team_number>\d+)$", views.team_view, name="scattergun-team-show"),

    url(r"$", views.index_view, name="scattergun-index"),
]
