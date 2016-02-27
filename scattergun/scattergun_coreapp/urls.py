from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'teams/add', views.team_add_view, name='scattergun-team-add'),
    url(r'^teams/(?P<team_number>\d+)$', views.team_view, name='scattergun-team-show'),
    url(r'^teams/', views.team_list_view, name='scattergun-team-list'),
]
