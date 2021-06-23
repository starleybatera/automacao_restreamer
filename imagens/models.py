from django.db import models
from animais.models import Animal

# def upload_imagem(instance, filename):
#     return f"{instance.id}.{filename}"

class Imagens(models.Model):
    # imagem = models.ImageField(upload_to=upload_imagem, blank=True, null=True)
    imagem = models.TextField(null=True)
    cod_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.imagem

    def identificacao(self):
        return self.cod_animal.identificacao
