from rest_framework import  serializers
from django.contrib.auth.models import User 
from fazenda.models import Fazenda
from usuario_fazenda.models import Usuario_Fazenda

class Fazenda_Usuario(serializers.SlugRelatedField):
    def get_queryset(self):
        queryset = Fazenda.objects.all()
        request = self.context.get('request', None)
        if request.user.is_superuser:
            
            queryset = queryset.filter(usuario_fazenda__usuario=request.user.id)
            
        return queryset

class Usuario_FazendaSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField( queryset=User.objects.all(),slug_field='username' )
    fazenda = Fazenda_Usuario(slug_field='identificacao')

    class Meta:
        model = Usuario_Fazenda
        fields = ['id', 'usuario','fazenda']
