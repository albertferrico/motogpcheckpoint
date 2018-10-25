from django.contrib import admin
from .models import News

@admin.register(News)
class AdminNews(admin.ModelAdmin):
        list_display = ('language','timestamp','title','news_url',)
