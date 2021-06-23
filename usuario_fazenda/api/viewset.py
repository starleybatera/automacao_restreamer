from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, generics
from usuario_fazenda.models import Usuario_Fazenda
from .serializers import Usuario_FazendaSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class Usuario_FazendaViewSet(viewsets.ModelViewSet):
    queryset = Usuario_Fazenda.objects.all()
    serializer_class = Usuario_FazendaSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['id', 'usuario','fazenda']

class Lista_Fazenda_Usuario(generics.ListAPIView):
    serializer_class =  Usuario_FazendaSerializer

    def get_queryset(self):
        
        user = self.request.user
        user_faz = Usuario_Fazenda.objects.get(usuario=user.id)
        return Usuario_Fazenda.objects.filter(fazenda__identificacao=user_faz.fazenda).order_by('id')

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        
        user = self.request.user
        if user.is_superuser:
            usuario_fazenda = serializer.save()
            return Response({"Results":Usuario_FazendaSerializer(usuario_fazenda, context=self.get_serializer_context()).data,})
        else:
            raise serializers.ValidationError({'Error': 'Usuário sem autorização para cadastrar!'}) 