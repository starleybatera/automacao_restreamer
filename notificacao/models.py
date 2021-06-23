from django.db import models
from agrupamentos.models import Agrupamento
from django.utils.timezone import now


class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

class Notificacao(models.Model):
    descricao = models.TextField(max_length=255)
    status = models.BooleanField(verbose_name=("lida"), default=False)
    data = CustomDateTimeField(default=now)
    id_agrupamento = models.ForeignKey(Agrupamento, on_delete=models.CASCADE,related_name='agrupamento')

    

    def __str__(self):
        return self.descricao

