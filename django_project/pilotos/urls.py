from django.conf.urls import url

from .views import(
	PilotoLista,
	PilotoDetalle,
	PilotoNuevo,
	PilotoActualizado,
	PilotoEliminar
)

urlpatterns = [
	url(r'^$', PilotoLista.as_view(), name='lista'),
	url(r'^(?P<slug>[\w-]+)/$', PilotoDetalle.as_view(), name='detalle'),
	url(r'^nuevo$', PilotoNuevo.as_view(), name='nuevo'),
	url(r'^editar/(?P<pk>\d+)$', PilotoActualizado.as_view(), name='editar'),
	url(r'^eliminar/(?P<pk>\d+)$', PilotoEliminar.as_view(), name='eliminar'),

]
