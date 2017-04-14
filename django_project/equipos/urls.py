from django.conf.urls import url

from .views import(
	EquipoLista,
	EquipoDetalle,
	EquipoNuevo,
	EquipoActualizado,
	EquipoEliminar
)

urlpatterns = [
	url(r'^$', EquipoLista.as_view(), name='lista'),
	url(r'^(?P<slug>[\w-]+)/$', EquipoDetalle.as_view(), name='detalle'),
	url(r'^nuevo$', EquipoNuevo.as_view(), name='nuevo'),
	url(r'^editar/(?P<pk>\d+)$', EquipoActualizado.as_view(), name='editar'),
	url(r'^eliminar/(?P<pk>\d+)$', EquipoEliminar.as_view(), name='eliminar'),
]
