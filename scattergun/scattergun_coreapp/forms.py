from django.forms import ModelForm, Form, ModelChoiceField
from .models import Team, RoundReport, Competition
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import FormActions, TabHolder, Tab


class CompetitionForm(ModelForm):
    class Meta:
        model = Competition
        exclude = ()


class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ()


class CompetitionSelectForm(Form):
    competition = ModelChoiceField(queryset=Competition.objects.all(), to_field_name="name")

    def __init__(self, *args, **kwargs):
        super(CompetitionSelectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            "competition",
            Submit('select', 'Select'),
        )


class RoundReportForm(ModelForm):
    # match = ModelChoiceField(queryset=Competition.objects.all(), to_field_name="number")

    def __init__(self, *args, **kwargs):
        super(RoundReportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    "Pre-Round Information",
                    "team",
                    "match_number",
                    "competition",
                    "a_defense",
                    "b_defense",
                    "c_defense",
                    "d_defense",
                ),
                Tab(
                    "During-Round Information",

                    "a_defense_ability",
                    "b_defense_ability",
                    "c_defense_ability",
                    "d_defense_ability",

                    "boulders_scored_in_low",
                    "boulders_scored_in_high",
                    "can_scale_tower",
                    "tower_scaling_ability",
                    "tower_scaling_time",

                    "low_boulders_blocked",
                    "high_boulders_blocked",
                    "notes_about_defense",
                ),
                Tab(
                    "Post-Round Data",

                    "friendly_alliance_score",
                    "enemy_alliance_score",
                    "friendly_alliance_rank_points",
                    "enemy_alliance_rank_points",

                    "foul_count",
                    "technical_foul_count",
                    "yellow_card_count",
                    "red_card_count",

                    "got_stuck",
                    "lost_connection",
                    "lost_control",
                    "tech_issues_comment",

                    "speed",
                    "maneuverability",
                    "pushing_power",

                    "driveteam_maneuvering_skill",
                )
            ),
            FormActions(
                Submit('save', 'Save'),
            )
        )

    class Meta:
        model = RoundReport
        exclude = ()
