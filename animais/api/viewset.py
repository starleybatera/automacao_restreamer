from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from animais.models import Animal
from raca.models import Raca
from agrupamentos.models import Agrupamento
from .serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['identificacao', 'descricao','cod_agrupamento__identificacao']
    ordering = ['-id']


class Lista_Animais(generics.ListAPIView):
    serializer_class =  AnimalSerializer

    def get_queryset(self):
        
        cod_animal = self.kwargs['identificacao']
        
        return Animal.objects.filter(identificacao=cod_animal)

class Lista_Animal(generics.ListAPIView):
    serializer_class = AnimalSerializer

    def get_queryset(self):
        cod_animal = self.kwargs['identificacao']
        id = self.kwargs['id']
        return Animal.objects.filter(identificacao= cod_animal, id=id)