from django.urls import path
from .views import ProdutoListView, ProdutoCreateView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produtos'),
    path('novo/', ProdutoCreateView.as_view(), name='produto_novo'), 
]
