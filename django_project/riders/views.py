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
from .models import Rider


class RiderList(ListView):
        model = Rider

class RiderDetail(DetailView):
        model = Rider

class RiderNew(LoginRequiredMixin, CreateView):
        model = Rider
        success_url = reverse_lazy('riders:list')
        fields = ['name','team','rider_number','biography','rider_profile','source']

class RiderUpdated(LoginRequiredMixin, UpdateView):
        model = Rider
        success_url = reverse_lazy('riders:list')
        fields = ['name','team','rider_number','biography','rider_profile','source']

class RiderDelete(LoginRequiredMixin, DeleteView):
        model = Rider
        success_url = reverse_lazy('riders:list')
