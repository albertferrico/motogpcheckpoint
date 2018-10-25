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
from .models import News

class NewsList(ListView):
        model = News
        paginate_by = 20
        #queryset = Noticia.objects.all()  # Default: Model.objects.all()

        def get_queryset(self):
                queryset = News.objects.all()
                if self.request.GET.get("language"):
                        selection = self.request.GET.get("language")
                        queryset = News.objects.filter(language = selection)
                return queryset

class NewsNew(LoginRequiredMixin, CreateView):
        model = News
        success_url = reverse_lazy('news:list')
        fields = ['title','news_url']

class NewsUpdated(LoginRequiredMixin, UpdateView):
        model = News
        success_url = reverse_lazy('news:list')
        fields = ['title','news_url']

class NewsDelete(LoginRequiredMixin, DeleteView):
        model = News
        success_url = reverse_lazy('news:list')
