from django.contrib import admin
from .models import Circuito

@admin.register(Circuito)
class AdminCircuito(admin.ModelAdmin):
	list_display = ('fecha_evento','nombre')
