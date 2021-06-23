from rest_framework import  serializers
from agrupamentos.models import Agrupamento
from camera.models import Camera

class User_Agrupamentos(serializers.SlugRelatedField):
    def get_queryset(self):
        queryset = Agrupamento.objects.all()
        request = self.context.get('request', None)
        if request.user.is_superuser:
            queryset = queryset.filter(fazenda__usuario_fazenda__usuario=request.user.id)
        return queryset

class CameraSerializer(serializers.ModelSerializer):
    # agrupamento = User_Agrupamentos(slug_field='descricao')
    
    class Meta:
        model = Camera
        fields = ['id','descricao','url']

