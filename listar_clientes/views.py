from django.http import HttpResponse

def listar_clientes(request):
    return HttpResponse("Clientes funcionando")
