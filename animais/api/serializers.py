from rest_framework import  serializers
from animais.models import Animal
from raca.models import Raca
from agrupamentos.models import Agrupamento
from historico.api.serializers import HistoricoSerializer




class AnimalSerializer(serializers.ModelSerializer):

    cod_raca = serializers.SlugRelatedField( queryset=Raca.objects.all(),slug_field='descricao' )
    cod_agrupamento = serializers.SlugRelatedField( queryset=Agrupamento.objects.all(),slug_field='identificacao')
    historicos = HistoricoSerializer(many=True)
    class Meta:
        model = Animal
        fields = ['id', 'identificacao', 'descricao', 'cod_raca', 'cod_agrupamento',"historicos"]
       

    
   