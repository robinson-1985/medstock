from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel_vendas, name='painel_vendas'),
]
