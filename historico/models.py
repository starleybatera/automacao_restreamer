from django.db import models
from historico_tipo.models import Historico_Tipo
from animais.models import Animal
from django.utils.timezone import now


class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

class Historico(models.Model):
    descricao = models.TextField(max_length=255)
    notificacao = models.BooleanField(verbose_name=("lida"), default=False)
    data = CustomDateTimeField(default=now)
    cod_tipo = models.ForeignKey(Historico_Tipo, on_delete=models.CASCADE)
    id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='historicos')

    

    def __str__(self):
        return self.descricao

