from django.contrib import admin
from .models import Agrupamento
from fazenda.models import Fazenda


@admin.register(Agrupamento)
class Agrupamento_Admin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        user = request.user
        if db_field.name == "fazenda":
            kwargs["queryset"] = Fazenda.objects.filter(usuario_fazenda__usuario=user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('id','descricao','fazenda')
    search_fields = ('id','descricao','fazenda')
