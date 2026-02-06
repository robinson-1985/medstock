from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos),
    path('fornecedores/', views.fornecedores),
]
