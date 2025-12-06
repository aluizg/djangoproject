from django.contrib import admin
from .models import Empreendimento, Colaborador

class EmpreendimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'status')
    list_filter = ('status',)
    search_fields = ('nome', 'endereco')

class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    list_filter = ('nome',)
    search_fields = ('nome', 'email')


# Register your models here.
# ALG Registrando os modelos para aparecerem no admin
admin.site.register(Empreendimento, EmpreendimentoAdmin)
admin.site.register(Colaborador, ColaboradorAdmin)