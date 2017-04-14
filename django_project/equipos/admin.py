from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class AdminEquipo(admin.ModelAdmin):
	list_display = ('nombre',)