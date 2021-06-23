from django.db import models
from raca.models import Raca
from agrupamentos.models import Agrupamento


class Animal(models.Model):
    identificacao =  models.CharField(max_length=255, unique=True, null=False)
    descricao = models.TextField(max_length=255, null=True)
    cod_raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    cod_agrupamento = models.ForeignKey(Agrupamento, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.identificacao

    

