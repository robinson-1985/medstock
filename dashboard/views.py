from django.http import HttpResponse


def home(request):
    return HttpResponse('Bem-vindo à página inicial do estoque.')


def pagina_dashboard(request):
    return HttpResponse('Página inicial do estoque.')


def produtos(request):
    return HttpResponse('Lista de produtos.')


def fornecedores(request):
    return HttpResponse("Fornecedores")
