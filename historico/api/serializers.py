from rest_framework import  serializers
from historico.models import Historico
from historico_tipo.models import Historico_Tipo
from animais.models import Animal


class HistoricoSerializer(serializers.ModelSerializer):
    cod_tipo = serializers.SlugRelatedField( queryset=Historico_Tipo.objects.all(),slug_field='descricao' )
    # id_animal = serializers.SlugRelatedField( queryset=Animal.objects.all(),slug_field='id' )

    class Meta:
        model = Historico
        fields = ['id', 'id_animal','descricao','cod_tipo','data','notificacao']
