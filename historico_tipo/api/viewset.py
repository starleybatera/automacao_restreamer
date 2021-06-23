from django.shortcuts import render
from rest_framework import viewsets
from historico_tipo.models import Historico_Tipo
from .serializers import Historico_TipoSerializer


class Historico_TipoViewSet(viewsets.ModelViewSet):
    queryset = Historico_Tipo.objects.all()
    serializer_class = Historico_TipoSerializer