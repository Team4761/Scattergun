from django.forms import ModelForm
from .models import Team, RoundReport


class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ()


class RoundReportForm(ModelForm):
    class Meta:
        model = RoundReport
        exclude = ()
