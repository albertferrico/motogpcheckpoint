from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import pre_save
from django.utils.text import slugify
from teams.models import Team
class Rider(models.Model):
        name = models.CharField(max_length=255)
        team = models.ForeignKey('teams.Team',related_name='rider_team', on_delete=models.CASCADE, blank=True)
        biography = models.TextField()
        rider_profile = models.ImageField(blank=True)
        source = models.CharField(max_length=255, blank=True)
        rider_number = models.IntegerField(default=0)
        slug = models.CharField(max_length=255, default='rider', editable=True)

        class Meta:
                ordering = ('rider_number',)

        def __unicode__(self):
                return self.name
