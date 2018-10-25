from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)
from django.core.urlresolvers import reverse_lazy
from .models import Equipo

class EquipoLista(ListView):
	model = Equipo

class EquipoDetalle(DetailView):
	model = Equipo

class EquipoNuevo(LoginRequiredMixin, CreateView):
	model = Equipo
	success_url = reverse_lazy('equiposlista')
	fields = ['nombre','pilotos','historia','imagen_equipo','fuente','pilotos_del_equipo']

class EquipoActualizado(LoginRequiredMixin, UpdateView):
	model = Equipo
	success_url= reverse_lazy('equipos:lista')
	fields = ['nombre','pilotos','historia','imagen_equipo','fuente','pilotos_del_equipo']

class EquipoEliminar(LoginRequiredMixin, DeleteView):
	model = Equipo
	success_url = reverse_lazy('equipos:lista')

