from rest_framework.viewsets import ModelViewSet
from core.models import Compra
from core.serializers import CompraSerializer, NovaCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    #serializer_class = CompraSerializer
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return CompraSerializer
        else:
            return NovaCompraSerializer
        
    def get_queryset(self):
        usuario = self.request.user
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)