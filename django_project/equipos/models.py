from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Equipo(models.Model):
	nombre = models.CharField(max_length=255)
	imagen_equipo = models.ImageField(blank=True)
	fuente = models.CharField(max_length=255, blank=True)
	historia = models.TextField()
	slug = models.CharField(max_length=255, default='equipo', editable=True)



	class Meta:
		ordering = ('nombre',)

	def __unicode__(self):
		return self.nombre


