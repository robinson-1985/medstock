from django.urls import path
from . import views

app_name = 'listar_clientes'

urlpatterns = [
    path('', views.listar_clientes, name='clientes'),
]
