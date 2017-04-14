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
from .models import Circuito

class CircuitoLista(ListView):
	model = Circuito

class CircuitoDetalle(DetailView):
	model = Circuito

class CircuitoNuevo(LoginRequiredMixin, CreateView):
	model = Circuito
	success_url = reverse_lazy('circuitos:lista')
	fields = ['nombre','descripcion','fecha_evento','slug']

class CircuitoActualizado(LoginRequiredMixin, UpdateView):
	model = Circuito
	success_url = reverse_lazy('circuitos:lista')
	fields = ['nombre','descripcion','fecha_evento','slug']

class CircuitoEliminar(LoginRequiredMixin, DeleteView):
	model = Circuito
	success_url = reverse_lazy('circuitos:lista')
