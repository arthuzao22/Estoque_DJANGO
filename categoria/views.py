from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria

# Listar categorias
class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'

# Detalhar categoria
class CategoriaDetailView(LoginRequiredMixin, DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'

# Criar categoria
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'categoria_form.html'
    fields = ['categoria']
    success_url = reverse_lazy('categoria-list')

# Atualizar categoria
class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'categoria_form.html'
    fields = ['categoria']
    success_url = reverse_lazy('categoria-list')

# Deletar categoria
class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria-list')
