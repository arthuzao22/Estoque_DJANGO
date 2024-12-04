from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Empresa
from django.contrib.auth.mixins import LoginRequiredMixin


# Lista de empresas
class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'empresa_list.html'
    context_object_name = 'empresas'

# Detalhes de uma empresa
class EmpresaDetailView(LoginRequiredMixin, DetailView):
    model = Empresa
    template_name = 'empresa_detail.html'

# Criar uma nova empresa
class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    template_name = 'empresa_form.html'
    fields = ['nome', 'endereco']
    success_url = reverse_lazy('empresa-list')

# Atualizar uma empresa existente
class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    template_name = 'empresa_form.html'
    fields = ['nome', 'endereco']
    success_url = reverse_lazy('empresa-list')

# Deletar uma empresa
class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'empresa_confirm_delete.html'
    success_url = reverse_lazy('empresa-list')
