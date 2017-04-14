from django.db import models
from equipos.models import Equipo
class Piloto(models.Model):
	nombre = models.CharField(max_length=255)
	equipo = models.ForeignKey('equipos.Equipo',related_name='equipo_del_piloto', on_delete=models.CASCADE, null=True)
	biografia = models.TextField()
	perfil_piloto = models.ImageField(blank=True)
	fuente = models.CharField(max_length=255, blank=True)
	numero_dorsal = models.IntegerField(default=0)
	slug = models.CharField(max_length=255, default='piloto', editable=True)

	class Meta:
		ordering = ('numero_dorsal',)

	def __unicode__(self):
		return self.nombre
