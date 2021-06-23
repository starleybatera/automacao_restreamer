from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, generics
from agrupamentos.models import Agrupamento
from .serializers import AgrupamentoSerializer
from rest_framework.response import Response


class AgrupamentoViewSet(viewsets.ModelViewSet):
    queryset = Agrupamento.objects.all()
    serializer_class = AgrupamentoSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['id', 'descricao','fazenda']

class Lista_Agrupamentos(generics.ListAPIView):
    serializer_class =  AgrupamentoSerializer

    def get_queryset(self):
        
        user = self.request.user
  
        return Agrupamento.objects.filter(fazenda__usuario_fazenda__usuario=user.id).order_by('id')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        
        if user.is_superuser:
            agrupamento = serializer.save()
            return Response({"Results":AgrupamentoSerializer(agrupamento, context=self.get_serializer_context()).data,})
        else:
            raise serializers.ValidationError({'Error': 'Usuário sem autorização para cadastrar!'})
