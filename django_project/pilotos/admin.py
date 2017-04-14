from django.contrib import admin
from .models import Piloto
# Register your models here.

@admin.register(Piloto)
class AdminPiloto(admin.ModelAdmin):
	list_display = ('numero_dorsal','nombre',)