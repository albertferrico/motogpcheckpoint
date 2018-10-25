from __future__ import unicode_literals

from django.db import models
from datetime import date

class Racetrack(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField()
        track_image = models.ImageField(blank=True)
        event_date = models.DateField(auto_now_add=False)
        slug = models.CharField(max_length=255, default='racetrack', editable=True)

        class Meta:
                ordering = ('event_date',)

        def coming_race(self):
                return self.event_date > date.today()
        def race_ongoing(self):
                return self.event_date == date.today()

        def __unicode__(self):
                return self.name
