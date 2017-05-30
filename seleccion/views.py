# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView
)

from .models import Futbolista
# Create your views here.
class FutbolistaList(ListView):
	model = Futbolista

class FutbolistaDetail(DetailView):
	model = Futbolista

class FutbolistaCreation(CreateView):
	model = Futbolista
	success_url = reverse_lazy('seleccion:list')
	fields = ['author', 'title', 'text', 'picture', 'created_date']

class FutbolistaUpdate(UpdateView):
	model = Futbolista
	success_url = reverse_lazy('seleccion:list')
	fields = ['author', 'title', 'text', 'picture', 'created_date']

class FutbolistaDelete(DeleteView):
	model = Futbolista
	success_url = reverse_lazy('seleccion:list')