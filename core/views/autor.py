from core.models import Autor
from core.serializers import AutorSerializer
from rest_framework.viewsets import ModelViewSet

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer