from django.shortcuts import render


def gerar_relatorio(request):
    return render(request, 'home/relatorio.html')
