from django.shortcuts import render
from rest_framework import viewsets
from raca.models import Raca 
from .serializers import RacaSerializer


class RacaViewSet(viewsets.ModelViewSet):
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer
