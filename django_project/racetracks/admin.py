from django.contrib import admin
from .models import Racetrack

@admin.register(Racetrack)
class AdminRacetrack(admin.ModelAdmin):
        list_display = ('event_date','name')
