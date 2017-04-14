from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView, 
	UpdateView,
	DeleteView
)
from django.core.urlresolvers import reverse_lazy
from .models import Piloto


class PilotoLista(ListView):
	model = Piloto

class PilotoDetalle(DetailView):
	model = Piloto

class PilotoNuevo(LoginRequiredMixin, CreateView):
	model = Piloto
	success_url = reverse_lazy('pilotos:lista')
	fields = ['nombre','equipo','numero_dorsal','biografia','perfil_piloto','fuente']

class PilotoActualizado(LoginRequiredMixin, UpdateView):
	model = Piloto
	success_url = reverse_lazy('pilotos:lista')
	fields = ['nombre','equipo','numero_dorsal','biografia','perfil_piloto','fuente']

class PilotoEliminar(LoginRequiredMixin, DeleteView):
	model = Piloto
	success_url = reverse_lazy('pilotos:lista')
