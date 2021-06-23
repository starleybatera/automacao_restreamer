from rest_framework import  serializers
from historico_tipo.models import Historico_Tipo


class Historico_TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico_Tipo
        fields = ['id', 'descricao']
