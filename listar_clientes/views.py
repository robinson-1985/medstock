from django.shortcuts import render


def home(request):
    return render(request, 'clientes/home.html')

def clientes(request):
    return render(request, 'clientes/clientes.html')
