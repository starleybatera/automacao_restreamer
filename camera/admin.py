from django.contrib import admin
from .models import Camera
from agrupamentos.models import Agrupamento


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        user = request.user
        if db_field.name == "agrupamento":
            kwargs["queryset"] = Agrupamento.objects.filter(fazenda__usuario_fazenda__usuario=user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('descricao', 'url', 'agrupamento')
    search_fields = ('descricao', 'url','agrupamento')
