from django.db import models
from fazenda.models import Fazenda

class Agrupamento(models.Model):
    descricao = models.CharField(max_length=255, unique=True, null=False)
    fazenda = models.ForeignKey(Fazenda, on_delete=models.SET_NULL, blank=True, null=True, related_name='agrupamento')

    def __str__(self):
        return self.descricao

