from django.contrib import admin
from .models import *

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')

@admin.register(Visitas)
class VisitasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dia', 'horario', 'status')

admin.site.register(DiasVisita)
admin.site.register(Cidade)
admin.site.register(Imagem)
admin.site.register(Horario)