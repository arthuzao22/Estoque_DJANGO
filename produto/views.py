from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin


#PRODUTOS

# Listar produtos
class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'

# Detalhar produto
class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'produto_detail.html'

# Criar produto
class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'id_categoria', 'id_formato', 'unidades']
    success_url = reverse_lazy('produto-list')

# Atualizar produto
class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'id_categoria', 'id_formato', 'unidades']
    success_url = reverse_lazy('produto-list')

# Deletar produto
class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto-list')
    
# ESTOQUE    
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Estoque

# Listar itens do estoque
class EstoqueListView(LoginRequiredMixin, ListView):
    model = Estoque
    template_name = 'estoque/estoque_list.html'
    context_object_name = 'estoques'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estoques = context['estoques']

        # Adicionar o cálculo diretamente ao queryset
        for estoque in estoques:
            estoque.calculo = estoque.qtde * estoque.id_produto.unidades

        return context

# Detalhar item do estoque
class EstoqueDetailView(LoginRequiredMixin, DetailView):
    model = Estoque
    template_name = 'estoque/estoque_detail.html'

# Adicionar item ao estoque
class EstoqueCreateView(LoginRequiredMixin, CreateView):
    model = Estoque
    template_name = 'estoque/estoque_form.html'
    fields = ['id_produto', 'qtde']
    success_url = reverse_lazy('estoque-list')

# Atualizar item no estoque
class EstoqueUpdateView(LoginRequiredMixin, UpdateView):
    model = Estoque
    template_name = 'estoque/estoque_form.html'
    fields = ['id_produto', 'qtde']
    success_url = reverse_lazy('estoque-list')

# Remover item do estoque
class EstoqueDeleteView(LoginRequiredMixin, DeleteView):
    model = Estoque
    template_name = 'estoque/estoque_confirm_delete.html'
    success_url = reverse_lazy('estoque-list')

