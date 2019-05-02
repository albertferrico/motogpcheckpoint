from django.conf.urls import include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from portada import views
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', lambda r: HttpResponseRedirect('portada/')),
    #url(r'portada/', include('portada.urls', namespace='portada')),
    url(r'^$', lambda r: HttpResponseRedirect('noticias/')),
    url(r'^noticias/', include('noticias.urls', namespace='noticias')),
    url(r'^news/', include('news.urls', namespace='news')), 
    url(r'^equipos/', include('equipos.urls', namespace='equipos')),
    url(r'^teams/', include('teams.urls', namespace='teams')),
    url(r'^circuitos/', include('circuitos.urls', namespace='circuitos')),
    url(r'^racetracks/', include('racetracks.urls', namespace='racetracks')),
    url(r'^pilotos/', include('pilotos.urls', namespace='pilotos')),
    url(r'^riders/', include('riders.urls', namespace='riders')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sobre_nosotros/', 
    TemplateView.as_view(template_name="pag_estaticas/sobre_nosotros.html"),
    name='sobre_nostros'),
    url(r'^terminos_condiciones/',
    TemplateView.as_view(template_name="pag_estaticas/term_and_cond.html"),
    name='terminos_condiciones'),
]
