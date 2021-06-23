from django.contrib import admin
from .models import Notificacao


@admin.register(Notificacao)
class Notificacao_Admin(admin.ModelAdmin):
    
    list_display = ('id','descricao','data','id_agrupamento')
    search_fields = ('id','descricao','data','id_agrupamento')
