from django.conf.urls import url
from .views import(
	CircuitoLista,
	CircuitoDetalle,
	CircuitoNuevo,
	CircuitoActualizado,
	CircuitoEliminar,
)
urlpatterns = [
	url(r'^$', CircuitoLista.as_view(), name='lista'),
	url(r'^(?P<slug>[\w-]+)/$', CircuitoDetalle.as_view(), name='detalle'),
	url(r'^nuevo$', CircuitoNuevo.as_view(), name='nuevo'),
	url(r'^editar/(?P<pk>\d+)$', CircuitoActualizado.as_view(), name='editar'),
	url(r'^eliminar/(?P<pk>\d+)$', CircuitoEliminar.as_view(), name='eliminar'),
]
