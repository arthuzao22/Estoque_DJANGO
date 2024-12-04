from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Categoria

# Listar categorias
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'

# Detalhar categoria
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'

# Criar categoria
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categoria_form.html'
    fields = ['categoria']
    success_url = reverse_lazy('categoria-list')

# Atualizar categoria
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'categoria_form.html'
    fields = ['categoria']
    success_url = reverse_lazy('categoria-list')

# Deletar categoria
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria-list')
