from django.db import models
from datetime import date

class Circuito(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField()
	imagen_trazado = models.ImageField(blank=True)
	fecha_evento = models.DateField(auto_now_add=False)
	slug = models.CharField(max_length=255, default='circuito', editable=True)

	class Meta:
		ordering = ('fecha_evento',)
	
	def carrera_por_disputar(self):
		return self.fecha_evento > date.today()	

	def __unicode__(self):
		return self.nombre
