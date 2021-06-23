from django.contrib import admin
from .models import Imagens

@admin.register(Imagens)
class Imagens_Admin(admin.ModelAdmin):
    
    list_display = ('cod_animal','imagem')
    search_fields = ('id','cod_animal')