from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Formato
from django.contrib.auth.mixins import LoginRequiredMixin


# Lista de formatos
class FormatoListView(LoginRequiredMixin, ListView):
    model = Formato
    template_name = 'formato_list.html'
    context_object_name = 'formatos'

# Detalhes de um formato
class FormatoDetailView(LoginRequiredMixin, DetailView):
    model = Formato
    template_name = 'formato_detail.html'

# Criar um novo formato
class FormatoCreateView(LoginRequiredMixin, CreateView):
    model = Formato
    template_name = 'formato_form.html'
    fields = ['formato']
    success_url = reverse_lazy('formato-list')

# Atualizar um formato existente
class FormatoUpdateView(LoginRequiredMixin, UpdateView):
    model = Formato
    template_name = 'formato_form.html'
    fields = ['formato']
    success_url = reverse_lazy('formato-list')

# Deletar um formato
class FormatoDeleteView(LoginRequiredMixin, DeleteView):
    model = Formato
    template_name = 'formato_confirm_delete.html'
    success_url = reverse_lazy('formato-list')
