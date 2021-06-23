from rest_framework import  serializers
from django.contrib.auth.models import User 
from fazenda.models import Fazenda
from agrupamentos.models import Agrupamento
from agrupamentos.api.serializers import AgrupamentoSerializer
from camera.api.serializers import CameraSerializer



class FazendaSerializer(serializers.ModelSerializer):
    # agrupamento = serializers.StringRelatedField(many=True)
    agrupamento = AgrupamentoSerializer(many=True, read_only=True)
    class Meta:
        model = Fazenda
        fields = ['id', 'identificacao','agrupamento']