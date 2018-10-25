from django.contrib import admin
from .models import Rider
# Register your models here.

@admin.register(Rider)
class AdminRider(admin.ModelAdmin):
        list_display = ('rider_number','name',)
