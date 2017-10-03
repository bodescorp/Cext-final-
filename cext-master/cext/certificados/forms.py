# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from certificados.models import Participante, Curso,Certificado

class ParticipanteForm(forms.ModelForm):

    class Meta:
        model = Participante
        fields = ('__all__')

class CursoForm(forms.ModelForm):
	
	class Meta:
		model = Curso
		fields = ('__all__')

class CertificadoForm(forms.ModelForm):
	class Meta:
		model = Certificado
		fields = ('__all__')
