from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView  # Importando ListView aqui
from .models import Movimentacoes
from django.shortcuts import get_object_or_404
from produto.models import Estoque
from django.http import HttpResponse

# Listar movimentações
class MovimentacoesListView(LoginRequiredMixin, ListView):
    model = Movimentacoes
    template_name = 'movimentacoes_list.html'
    context_object_name = 'movimentacoes'

# Criar movimentação
class MovimentacoesCreateView(LoginRequiredMixin, CreateView):
    model = Movimentacoes
    template_name = 'movimentacoes_form.html'
    fields = ['qtde', 'tipo_movimentacao', 'id_empresa', 'id_produto']
    success_url = reverse_lazy('movimentacoes-list')

    def form_valid(self, form):
        # Atribui o id_usuario como o usuário atualmente logado
        form.instance.id_usuario = self.request.user

        # Obter o estoque relacionado ao id_produto
        estoque = get_object_or_404(Estoque, id_produto=form.cleaned_data['id_produto'])

        # Atualizar a qtde no estoque com base no tipo de movimentação
        if form.cleaned_data['tipo_movimentacao'] == 'Entrada':
            estoque.qtde += form.cleaned_data['qtde']
        elif form.cleaned_data['tipo_movimentacao'] == 'Saída':
            if estoque.qtde >= form.cleaned_data['qtde']:
                estoque.qtde -= form.cleaned_data['qtde']
            else:
                return HttpResponse("qtde insuficiente no estoque.")

        # Salvar o estoque atualizado
        estoque.save()

        # Chama o método original para salvar o formulário
        return super().form_valid(form)

# Deletar movimentação
class MovimentacoesDeleteView(LoginRequiredMixin, DeleteView):
    model = Movimentacoes
    template_name = 'movimentacoes_confirm_delete.html'
    success_url = reverse_lazy('movimentacoes-list')
