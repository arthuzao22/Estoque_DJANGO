from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Formato

# Lista de formatos
class FormatoListView(ListView):
    model = Formato
    template_name = 'formato_list.html'
    context_object_name = 'formatos'

# Detalhes de um formato
class FormatoDetailView(DetailView):
    model = Formato
    template_name = 'formato_detail.html'

# Criar um novo formato
class FormatoCreateView(CreateView):
    model = Formato
    template_name = 'formato_form.html'
    fields = ['formato']
    success_url = reverse_lazy('formato-list')

# Atualizar um formato existente
class FormatoUpdateView(UpdateView):
    model = Formato
    template_name = 'formato_form.html'
    fields = ['formato']
    success_url = reverse_lazy('formato-list')

# Deletar um formato
class FormatoDeleteView(DeleteView):
    model = Formato
    template_name = 'formato_confirm_delete.html'
    success_url = reverse_lazy('formato-list')
