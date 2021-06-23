from django.contrib import admin
from .models import Usuario_Fazenda


@admin.register(Usuario_Fazenda)
class Usuario_FazendaAdmin(admin.ModelAdmin):
    
    list_display = ('usuario', 'fazenda')
    search_fields = ('usuario', 'fazenda')
