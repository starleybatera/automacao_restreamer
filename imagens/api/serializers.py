from rest_framework import  serializers
from imagens.models import Imagens
from animais.models import Animal
# from django.urls import reverse

class ImagensSerializer(serializers.ModelSerializer):

    identificacao = serializers.ReadOnlyField()

    class Meta:
        model = Imagens
        fields = ['id','identificacao','imagem']
