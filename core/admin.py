from django.contrib import admin

from core.models import Autor, Compra, Categoria, Editora, ItensCompra, Livro

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
#admin.site.register(Compra)
admin.site.register(ItensCompra)

class ItensInline(admin.StackedInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensInline]