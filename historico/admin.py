from django.contrib import admin
from .models import Historico

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    
    list_display = ('id_animal','descricao','cod_tipo','data')
    search_fields = ('id_animal','descricao', 'data','cod_tipo')