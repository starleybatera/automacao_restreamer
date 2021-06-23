from django.contrib import admin
from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    
    list_display = ('identificacao', 'descricao', 'cod_raca', 'cod_agrupamento')
    search_fields = ('identificacao', 'descricao')
