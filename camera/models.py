from django.db import models
from agrupamentos.models import Agrupamento

class Camera(models.Model):
    descricao = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=200, unique = True)
    agrupamento = models.ForeignKey(Agrupamento, on_delete=models.CASCADE, related_name='camera')

    

    def __str__(self):
        return self.descricao