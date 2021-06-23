from django.contrib import admin
from .models import Raca

@admin.register(Raca)
class Raca_Admin(admin.ModelAdmin):
    
    list_display = ('id','descricao')
    search_fields = ('id','descricao')