from django.shortcuts import render


def home(request):
    return render(request, 'fornecedores/home.html')
  
def fornecedores(request):
    return render(request, 'fornecedores/fornecedores.html')
