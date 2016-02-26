from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^teams/(?P<team_number>\d+)$', views.team_view)
]
