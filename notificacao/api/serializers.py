from rest_framework import  serializers
from notificacao.models import Notificacao


class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = ['id', 'descricao','status', 'data', 'id_agrupamento']

