from django.conf.urls import url

from .views import(
	NoticiaLista,
	NoticiaNueva,
	NoticiaActualizada,
	NoticiaEliminar
)

urlpatterns = [
	url(r'^$', NoticiaLista.as_view(), name='lista'),
	url(r'^nueva$', NoticiaNueva.as_view(), name='nueva'),
	url(r'^editar/(?P<pk>\d+)$', NoticiaActualizada.as_view(), name='editar'),
	url(r'^eliminar/(?P<pk>\d+)$', NoticiaEliminar.as_view(), name='eliminar'),

]
