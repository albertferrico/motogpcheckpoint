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
from .models import Team

class TeamList(ListView):
        model = Team

class TeamDetail(DetailView):
        model = Team

class TeamNew(LoginRequiredMixin, CreateView):
        model = Team
        success_url = reverse_lazy('teams:list')
        fields = ['name','team_riders','history','team_image','source']

class TeamUpdated(LoginRequiredMixin, UpdateView):
        model = Team
        success_url= reverse_lazy('teams:list')
        fields = ['name','team_riders','history','team_image','source']

class TeamDelete(LoginRequiredMixin, DeleteView):
        model = Team
        success_url = reverse_lazy('teams:list')
