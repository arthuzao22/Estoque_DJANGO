from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Empresa

# Lista de empresas
class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa_list.html'
    context_object_name = 'empresas'

# Detalhes de uma empresa
class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'empresa_detail.html'

# Criar uma nova empresa
class EmpresaCreateView(CreateView):
    model = Empresa
    template_name = 'empresa_form.html'
    fields = ['nome', 'endereco']
    success_url = reverse_lazy('empresa-list')

# Atualizar uma empresa existente
class EmpresaUpdateView(UpdateView):
    model = Empresa
    template_name = 'empresa_form.html'
    fields = ['nome', 'endereco']
    success_url = reverse_lazy('empresa-list')

# Deletar uma empresa
class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = 'empresa_confirm_delete.html'
    success_url = reverse_lazy('empresa-list')
