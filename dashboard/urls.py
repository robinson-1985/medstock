from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos),
    path('fornecedores/', views.fornecedores),
]
