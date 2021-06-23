from django.db import models

class Fazenda(models.Model):
    identificacao = models.CharField(max_length=255, unique=True, null=False)


    def __str__(self):
        return self.identificacao
