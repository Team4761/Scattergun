from django.contrib import admin
from .models import Team, RoundReport, Competition

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')


class RoundReportAdmin(admin.ModelAdmin):
    list_display = ('team', 'friendly_alliance_score', 'enemy_alliance_score')


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('date', 'name')
    
# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(RoundReport, RoundReportAdmin)
admin.site.register(Competition, CompetitionAdmin)
