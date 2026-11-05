from django.contrib import admin

# receitas/admin.py

from django.contrib import admin
from .models import Categoria, Receita


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Configuração administrativa para o modelo Categoria."""

    list_display = ["nome"]
    search_fields = ["nome"]
    ordering = ["nome"]


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    """Configuração administrativa para o modelo Receita."""

    list_display = [
        "titulo",
        "autor",
        "tempo_preparo",
        "publicada",
        "data_publicacao",
    ]
    
    list_filter = ["publicada", "categorias", "data_publicacao"]
    
    search_fields = ["titulo", "ingredientes", "modo_preparo"]
    
    filter_horizontal = ["categorias"]
    
    readonly_fields = ["data_publicacao"]
    
    ordering = ["-data_publicacao"]
    
    list_editable = ["publicada"]
