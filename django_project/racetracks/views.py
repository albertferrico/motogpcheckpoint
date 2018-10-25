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
from .models import Racetrack

class RacetrackList(ListView):
        model = Racetrack

class RacetrackDetail(DetailView):
        model = Racetrack

class RacetrackNew(LoginRequiredMixin, CreateView):
        model = Racetrack
        success_url = reverse_lazy('racetracks:list')
        fields = ['name','description','event_date','slug']

class RacetrackUpdated(LoginRequiredMixin, UpdateView):
        model = Racetrack
        success_url = reverse_lazy('racetracks:list')
	fields = ['name','description','event_date','slug']

class RacetrackDelete(LoginRequiredMixin, DeleteView):
        model = Racetrack
        success_url = reverse_lazy('racetracks:list')
