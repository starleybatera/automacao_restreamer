from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from imagens.models import Imagens
from imagens.models import Animal
from .serializers import ImagensSerializer
from rest_framework.permissions import IsAuthenticated



class ImagensViewSet(viewsets.ModelViewSet):
    queryset = Imagens.objects.all()
    serializer_class = ImagensSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['cod_animal__identificacao','cod_animal__descricao']

# class Imagens(generics.ListAPIView):
#     queryset = Imagens.objects.all()
#     serializer_class = ImagensSerializer

#     filter_backends = (SearchFilter, OrderingFilter)
#     search_fields = ['cod_animal__identificacao','cod_animal__descricao']

class Lista_Imagens(generics.ListAPIView):
    serializer_class = ImagensSerializer

    def get_queryset(self):
        
        cod_animal = self.kwargs['cod_animal']
        return Imagens.objects.filter(cod_animal=cod_animal)

class Lista_Imagem(generics.ListAPIView):
    serializer_class = ImagensSerializer

    def get_queryset(self):
        cod_animal = self.kwargs['cod_animal']
        id = self.kwargs['id']
        return Imagens.objects.filter(cod_animal= cod_animal, id=id)