from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView  # Importando ListView aqui
from .models import Movimentacoes

# Listar movimentações
class MovimentacoesListView(LoginRequiredMixin, ListView):
    model = Movimentacoes
    template_name = 'movimentacoes_list.html'
    context_object_name = 'movimentacoes'

# Detalhar movimentação
class MovimentacoesDetailView(LoginRequiredMixin, DetailView):
    model = Movimentacoes
    template_name = 'movimentacoes_detail.html'

# Criar movimentação
class MovimentacoesCreateView(LoginRequiredMixin, CreateView):
    model = Movimentacoes
    template_name = 'movimentacoes_form.html'
    fields = ['qtde', 'tipo_movimentacao', 'id_empresa', 'id_produto']
    success_url = reverse_lazy('movimentacoes-list')

    def form_valid(self, form):
        # Atribui o id_usuario como o usuário atualmente logado
        form.instance.id_usuario = self.request.user
        # Chama o método original para salvar o formulário
        return super().form_valid(form)

# Atualizar movimentação
class MovimentacoesUpdateView(LoginRequiredMixin, UpdateView):
    model = Movimentacoes
    template_name = 'movimentacoes_form.html'
    fields = ['qtde', 'tipo_movimentacao', 'id_empresa', 'id_produto']  # Removido 'id_usuario'
    success_url = reverse_lazy('movimentacoes-list')

    def form_valid(self, form):
        # Atribui o id_usuario como o usuário atualmente logado
        form.instance.id_usuario = self.request.user
        return super().form_valid(form)


# Deletar movimentação
class MovimentacoesDeleteView(LoginRequiredMixin, DeleteView):
    model = Movimentacoes
    template_name = 'movimentacoes_confirm_delete.html'
    success_url = reverse_lazy('movimentacoes-list')
