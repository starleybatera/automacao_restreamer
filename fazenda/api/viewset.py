from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, generics
from fazenda.models import Fazenda
from agrupamentos.models import Agrupamento
from camera.models import Camera
from .serializers import FazendaSerializer

class FazendaViewSet(viewsets.ModelViewSet):
    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['id', 'identificacao']

class FazendaIndividual(generics.ListAPIView):
    serializer_class = FazendaSerializer
    def get_queryset(self):
        
        id_fazenda = self.kwargs['id']
        return Fazenda.objects.filter(id=id_fazenda)