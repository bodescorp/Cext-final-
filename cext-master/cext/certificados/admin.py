# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Participante, Certificado,Curso

from django.utils.html import format_html
from django.core.urlresolvers import reverse

#########################


#############################


class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf','email' )
    search_fields = ['nome','cpf' ]

admin.site.register(Participante, ParticipanteAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ['nome']
admin.site.register(Curso, CursoAdmin)


@admin.register (Certificado)
class CertificadoAdmin(admin.ModelAdmin):
	list_display = ('participante','curso',"acconts_actions")
	search_fields = ['participante__nome','curso__nome',]

	def acconts_actions(self, obj):	
		return format_html(

			'<a class = "button" href = "{}">Gerar PDF </a> ' ,
		
			reverse('button_create', args=[obj.pk])
			
		)
#admin.site.register(Certificado, CertificadoAdmin)

	


