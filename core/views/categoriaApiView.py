from core.models import Categoria
from rest_framework.views import APIView
from core.serializers import CategoriaSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class CategoriasList(APIView):
    def get(self, request, id="none"):
        qs = Categoria.objects.get(id=id)
        serializer = CategoriaSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(Self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetail(APIView):
    def get(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    def put(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        categoria.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
