from django.contrib import admin
from .models import Empresa, Rodada, Decisao

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

@admin.register(Rodada)
class RodadaAdmin(admin.ModelAdmin):
    list_display = ['id']  # 100% seguro

@admin.register(Decisao)
class DecisaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'empresa', 'rodada']
    list_filter = ['rodada', 'empresa']