from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^teams/(?P<team_number>\d+)$', views.team_view),
    url(r'^teams/', views.team_list_view),
]
