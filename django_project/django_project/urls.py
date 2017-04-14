from django.conf.urls import include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from portada import views
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('portada/')),
    url(r'portada/', include('portada.urls', namespace='portada')),
    #url(r'^$', lambda r: HttpResponseRedirect('noticias/')),
    url(r'^noticias/', include('noticias.urls', namespace='noticias')),
    url(r'^equipos/', include('equipos.urls', namespace='equipos')),
    url(r'^circuitos/', include('circuitos.urls', namespace='circuitos')),
    url(r'^pilotos/', include('pilotos.urls', namespace='pilotos')),
    url(r'^admin/', include(admin.site.urls)),
]
