from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView
)
from django.core.urlresolvers import reverse_lazy
from .models import Noticia

class NoticiaLista(ListView):
	model = Noticia
	paginate_by = 20
	queryset = Noticia.objects.all()  # Default: Model.objects.all()
	

class NoticiaNueva(LoginRequiredMixin, CreateView):
	model = Noticia
	success_url = reverse_lazy('noticias:lista')
	fields = ['titulo','url_noticia']

class NoticiaActualizada(LoginRequiredMixin, UpdateView):
	model = Noticia
	success_url = reverse_lazy('noticias:lista')
	fields = ['titulo','url_noticia']

class NoticiaEliminar(LoginRequiredMixin, DeleteView):
	model = Noticia
	success_url = reverse_lazy('noticias:lista')
