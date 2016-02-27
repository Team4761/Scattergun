from django.contrib import admin
from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')


class RoundReportAdmin(admin.ModelAdmin):
    list_display = ('team', 'friendly_alliance_score', 'enemy_alliance_score')

# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(RoundReport, RoundReportAdmin)
