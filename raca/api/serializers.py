from rest_framework import  serializers
from raca.models import Raca

class RacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raca
        fields = ['id', 'descricao']
