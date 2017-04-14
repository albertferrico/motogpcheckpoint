from django.conf.urls import url

from .views import Portada

urlpatterns = [
	url(r'^$', Portada, name='portada'),
]
