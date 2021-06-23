from django.contrib import admin
from .models import Historico_Tipo


@admin.register(Historico_Tipo)
class Historico_Tipo_Admin(admin.ModelAdmin):
    
    list_display = ('id','descricao')
    search_fields = ('id','descricao')
