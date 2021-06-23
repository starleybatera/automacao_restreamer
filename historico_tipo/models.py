from django.db import models

class Historico_Tipo(models.Model):
    descricao = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.descricao