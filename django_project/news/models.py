from __future__ import unicode_literals

from django.db import models


class News(models.Model):
        language = models.CharField(max_length=10)
        title = models.CharField(max_length=255)
        news_url = models.CharField(max_length=255)
        timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
        class Meta:
                ordering = ['-timestamp']

        def __unicode__(self):
                return self.title
