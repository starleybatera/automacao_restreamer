from django.contrib import admin
from .models import Fazenda


@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    
    list_display = ('identificacao', )
    search_fields = ('identificacao', )
