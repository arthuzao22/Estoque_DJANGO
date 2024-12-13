from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction

#PRODUTOS

# Listar produtos
class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'

# Criar produto
class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'id_categoria', 'formato', 'id_formato', 'unidades']
    success_url = reverse_lazy('produto-list')

    def form_valid(self, form):
        # Salva o produto e cria o estoque com qtde 0
        with transaction.atomic():
            response = super().form_valid(form)
            # Acessando o produto recém-criado via self.object
            # Isso já acessa a instância do produto criada
            Estoque.objects.create(id_produto=self.object, qtde=0)  # Não precisa definir 'data_cadastro'
        return response

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
from django.views.generic import ListView
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
