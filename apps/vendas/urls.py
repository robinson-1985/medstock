from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendas, name='vendas'),
]
