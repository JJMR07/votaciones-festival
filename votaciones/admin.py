from django.contrib import admin

from .models import Categoria, Edicion, Opcion, Votacion


@admin.register(Edicion)
class EdicionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edicion")
    list_filter = ("edicion",)


@admin.register(Votacion)
class VotacionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria")
    list_filter = ("categoria",)


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "votacion")
    list_filter = ("votacion",)
