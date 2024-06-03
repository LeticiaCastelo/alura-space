from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada",)
    list_display_links = ("id", "nome")
    search_fields = ("nome",) # campo de busca 
    list_filter = ("categoria",) # filtro por categoria
    list_editable = ("publicada",)
    list_per_page = 10 # itens por página
  

admin.site.register(Fotografia, ListandoFotografias)
