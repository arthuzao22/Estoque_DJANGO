from django.contrib import admin
from django.urls import path
from empresa.views import EmpresaListView, EmpresaCreateView, EmpresaUpdateView, EmpresaDeleteView, EmpresaDetailView
from categoria.views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, CategoriaDetailView
from formato.views import FormatoListView, FormatoCreateView, FormatoUpdateView, FormatoDeleteView, FormatoDetailView
from produto.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, ProdutoDetailView
from movimentacoes.views import movimentacoes_view
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
        <h1>Bem-vindo ao Sistema de Estoque</h1>
        <ul>
            <li><a href="/empresa/">Empresa</a></li>
            <li><a href="/categoria/">Categoria</a></li>
            <li><a href="/formato/">Formato</a></li>
            <li><a href="/produto/">Produto</a></li>
            <li><a href="/estoque/">Estoque</a></li>
            <li><a href="/movimentacoes/">Movimentações</a></li>
        </ul>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('movimentacoes/', movimentacoes_view, name='movimentacoes'),
    
    # Rotas para Empresa
    path('empresa/', EmpresaListView.as_view(), name='empresa-list'),
    path('empresa/novo/', EmpresaCreateView.as_view(), name='empresa-create'),
    path('empresa/<int:pk>/editar/', EmpresaUpdateView.as_view(), name='empresa-update'),
    path('empresa/<int:pk>/deletar/', EmpresaDeleteView.as_view(), name='empresa-delete'),
    path('empresa/<int:pk>/', EmpresaDetailView.as_view(), name='empresa-detail'),

    # Rotas para Formato
    path('formato/', FormatoListView.as_view(), name='formato-list'),
    path('formato/novo/', FormatoCreateView.as_view(), name='formato-create'),
    path('formato/<int:pk>/editar/', FormatoUpdateView.as_view(), name='formato-update'),
    path('formato/<int:pk>/deletar/', FormatoDeleteView.as_view(), name='formato-delete'),
    path('formato/<int:pk>/', FormatoDetailView.as_view(), name='formato-detail'),
    
    # Rotas para categoria
    path('categoria/', CategoriaListView.as_view(), name='categoria-list'),
    path('categoria/novo/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('categoria/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categoria/<int:pk>/deletar/', CategoriaDeleteView.as_view(), name='categoria-delete'),
    path('categoria/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
    
    # Rotas para o produto
    path('produto/', ProdutoListView.as_view(), name='produto-list'),
    path('produto/novo/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produto/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto-update'),
    path('produto/<int:pk>/deletar/', ProdutoDeleteView.as_view(), name='produto-delete'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto-detail'),
]
