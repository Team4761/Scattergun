from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"competitions/$", views.competition_list_view, name="scattergun-competition-list"),
    url(r"competitions/add/", views.competition_add_view, name="scattergun-competition-add"),

    url(r"leaderboard/", views.avg_score_leaderboard_view, name="scattergun-avg-score-leaderboard"),

    url(r"roundreports/add", views.roundreport_add_view, name="scattergun-roundreport-add"),
    url(r"roundreports", views.roundreport_list_view, name="scattergun-roundreport-list"),

    url(r"teams/$", views.team_list_view, name="scattergun-team-list"),
    url(r"teams/add/", views.team_add_view, name="scattergun-team-add"),
    url(r"teams/(?P<team_number>\d+)$", views.team_view, name="scattergun-team-show"),

    url(r"$", views.index_view, name="scattergun-index"),
]
