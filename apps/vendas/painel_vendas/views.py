from django.shortcuts import render


def painel_vendas(request):
    return render(request, 'painel_vendas/painel_vendas.html')
