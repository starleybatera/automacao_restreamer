from django.shortcuts import render
from django.views.generic.edit import UpdateView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import viewsets, generics
from historico.models import Historico
from .serializers import HistoricoSerializer
from rest_framework.pagination import PageNumberPagination

class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    pagination_class = PageNumberPagination

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['id_animal']
    ordering = ['-id']


class Lista_Historicos(generics.ListAPIView):
    serializer_class =  HistoricoSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        
        id_animal = self.kwargs['id_animal']
        return Historico.objects.filter(id_animal=id_animal)

class Lista_Historico(generics.ListAPIView):
    serializer_class = HistoricoSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        id_animal = self.kwargs['id_animal']
        id = self.kwargs['id']
        notificacao = Historico.objects.filter(id_animal= id_animal, id=id)[0]
        notificacao.notificacao = "True"
        notificacao.save()
        return Historico.objects.filter(id_animal= id_animal, id=id)

class Lista_Historico_Notificacoes(generics.ListAPIView):
    serializer_class = HistoricoSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        
        if self.kwargs['status'] == "nao_lidos":
            return Historico.objects.filter(status="False")
        else:
            if self.kwargs['status'] == "lidos":
                 return Historico.objects.filter(status="True")
        
