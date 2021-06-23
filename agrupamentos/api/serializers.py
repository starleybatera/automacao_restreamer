from rest_framework import  serializers
from fazenda.models import Fazenda
from agrupamentos.models import Agrupamento
from camera.api.serializers import CameraSerializer

class User_Fazenda(serializers.SlugRelatedField):
    def get_queryset(self):
        queryset = Fazenda.objects.all()
        request = self.context.get('request', None)
        if request.user.is_superuser:
            queryset = queryset.filter(usuario_fazenda__usuario=request.user.id)
        return queryset

class AgrupamentoSerializer(serializers.ModelSerializer):
    # fazenda = User_Fazenda(slug_field='identificacao' )
    camera = CameraSerializer(many=True, read_only=True)
    class Meta:
        model = Agrupamento
        fields = ['id','descricao','camera']

