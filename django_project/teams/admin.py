from django.contrib import admin
from .models import Team

@admin.register(Team)
class AdminTeam(admin.ModelAdmin):
        list_display = ('name',)
