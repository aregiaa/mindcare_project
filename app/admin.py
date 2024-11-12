from django.contrib import admin

from .models import *

admin.site.register(Agendamentos)
admin.site.register(Cidade)
admin.site.register(Instituicao)
admin.site.register(Ocupacao)
admin.site.register(Paciente)
admin.site.register(Profissional)
admin.site.register(Horario)