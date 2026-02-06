from django.urls import path
from . import views

app_name = 'painel_vendas'

urlpatterns = [
    path('', views.home, name='vendas'),
]
