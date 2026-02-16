from django.views.generic import ListView, CreateView
from .models import Produto
from apps.core.mixins import OrganizationQuerysetMixin, OrganizationCreateMixin


class ProdutoListView(OrganizationQuerysetMixin, ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'
    context_object_name = 'produtos'
    
    
class ProdutoCreateView(OrganizationCreateMixin, CreateView):
    model = Produto
    fields = ['nome', 'preco']
    template_name = 'produtos/produto_form.html'
    success_url = '/produtos/'
