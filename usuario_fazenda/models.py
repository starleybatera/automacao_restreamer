from django.db import models
from fazenda.models import Fazenda
from django.contrib.auth.models import User

class Usuario_Fazenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE)

    class Meta:
            unique_together = (("usuario", "fazenda"),)