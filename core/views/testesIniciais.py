from django.http import HttpResponse, JsonResponse

def teste (request):
    return HttpResponse("Olá mundo!")

def teste2 (request):
    #return HttpResponse("Nova página de Django")
    data = {
        "data": {
            "1": "Carrinho",
            "2": "Realizado",
            "3": "Finalizado"
        }
    }
    return JsonResponse