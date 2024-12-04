from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Produto

# Listar produtos
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'

# Detalhar produto
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'

# Criar produto
class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'id_categoria', 'id_formato', 'unidades']
    success_url = reverse_lazy('produto-list')

# Atualizar produto
class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'id_categoria', 'id_formato', 'unidades']
    success_url = reverse_lazy('produto-list')

# Deletar produto
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto-list')
