from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Team(models.Model):
        name = models.CharField(max_length=255)
        team_riders = models.ManyToManyField('riders.Rider',related_name='team_riders',blank=True)
        team_image = models.ImageField(blank=True)
        source = models.CharField(max_length=255, blank=True)
        history = models.TextField()
        slug = models.CharField(max_length=255, default='team', editable=True)



        class Meta:
                ordering = ('name',)

        def __unicode__(self):
                return self.name
