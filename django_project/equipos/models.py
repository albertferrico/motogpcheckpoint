from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
#from pilotos.models import Piloto

class Equipo(models.Model):
	nombre = models.CharField(max_length=255)
	pilotos_del_equipo = models.ManyToManyField('pilotos.Piloto',related_name='pilotos_del_equipo',blank=True)
	imagen_equipo = models.ImageField(blank=True)
	fuente = models.CharField(max_length=255, blank=True)
	historia = models.TextField()
	estado = models.CharField(max_length=255, blank=True)
	slug = models.CharField(max_length=255, default='equipo', editable=True)



	class Meta:
		ordering = ('nombre',)

	def __unicode__(self):
		return self.nombre


