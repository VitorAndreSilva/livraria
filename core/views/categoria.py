from core.models import Categoria
from rest_framework.permissions import IsAuthenticated
from core.serializers import CategoriaSerializer
from rest_framework.viewsets import ModelViewSet

class CategoriaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

"""
class CategoriaView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                qs = Categoria.objects.get(id=id)
                data = {}
                data['id'] = qs.id
                data['descricao'] = qs.descricao
            except Categoria.DoesNotExist:
                return JsonResponse({'erro': 'Categoria não encontrada'}, status=404)
        else:
            data = list(Categoria.objects.values())
            formatado = json.dumps(data, ensure_ascii=False)
            return JsonResponse(data, safe=False)
            #return HttpResponse(formatado, content_type="application_json")
    
    def post(self, request):
        json_data = request.data #json.loads(request.body)
        novaCategoria = Categoria.objects.create(**json_data)
        data = {"id": novaCategoria.id, "descricao": novaCategoria.descricao}
        return JsonResponse(data)
    
    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id=id)
        qs.descricao = json_data['descricao'] if 'descricao' in json_data else qs.descricao
        qs.save()
        data = {}l
        data['id'] = qs.id
        data['descricao'] = qs.descricao
        return JsonResponse(data)
    
    def delete(self, request, id):
        qs = Categoria.objects.get(id=id)
        qs.delete()
        data = {'Item excluído com sucesso'}
        return JsonResponse(data)
"""