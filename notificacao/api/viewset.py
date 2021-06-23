from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from notificacao.models import Notificacao
from .serializers import NotificacaoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, generics



class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer
    pagination_class = PageNumberPagination

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['id', 'descricao','data','id_agrupamento']

class Lista_Notificacoes(generics.ListAPIView):
    serializer_class =  NotificacaoSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        
        id_agrupamento = self.kwargs['id_agrupamento']
        return Notificacao.objects.filter(id_agrupamento=id_agrupamento)

class Lista_Notificacao(generics.ListAPIView):
    serializer_class = NotificacaoSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        id_agrupamento = self.kwargs['id_agrupamento']
        id = self.kwargs['id']
        notificacao = Notificacao.objects.filter(id_agrupamento= id_agrupamento, id=id)[0]
        notificacao.status = "True"
        notificacao.save()
        return Notificacao.objects.filter(id_agrupamento= id_agrupamento, id=id)

class Lista_Agrupamentos_Notificacoes(generics.ListAPIView):
    serializer_class = NotificacaoSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        
        if self.kwargs['status'] == "nao_lidos":
            return Notificacao.objects.filter(status="False")
        else:
            if self.kwargs['status'] == "lidos":
                 return Notificacao.objects.filter(status="True")