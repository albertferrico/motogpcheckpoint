from django.db import models


class Noticia(models.Model):
	titulo = models.CharField(max_length=255)
	url_noticia = models.CharField(max_length=255)
	fecha_noticia = models.DateField(auto_now=True, auto_now_add=False)

	class Meta:
		ordering = ['-fecha_noticia']

	def __unicode__(self):
		return self.titulo
