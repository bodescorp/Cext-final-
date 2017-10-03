# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,get_object_or_404

from .models import Participante, Curso, Certificado

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from certificados import forms
from django.http.response import HttpResponse
from docxtpl import DocxTemplate
from certificados import models
import os
import mimetypes
from datetime import date


class ParticipantesDetailsView(generic.DetailView):

    model = models.Participante
    template_name = 'certificados/participante.html'
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(models.Participante, pk = pk)

    def today(self):
    	return date.today()

	# def get_context_data(self, **kwargs):
	# 	context = super(ParticipantesDetailsView, self).get_context_data(**kwargs)
	# 	context['number'] = 1
	# 	return context




class Dadoscurso (generic.DetailView):
	
	model = models.Curso
	template_name = 'certificados/dadoscurso.html'

	def get_object(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(models.Curso, pk= pk)

	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
		context = super(Dadoscurso, self).get_context_data(**kwargs)
		
		if date.today() > self.get_object().inicio  :
			context['Certificado'] = Certificado.objects.filter(curso=self.get_object())
		else:
			context['Participante'] = Participante.objects.all()
		context['form'] = forms.CertificadoForm()
		
		return context

	




	


class CadastroParticipante(generic.CreateView,generic.ListView):
    model = Participante
    template_name = 'certificados/user.html'
    form_class = forms.ParticipanteForm
    success_url = reverse_lazy('sucesso')

    


class CadastroCurso(generic.CreateView):
	model = Curso
	template_name = 'certificados/cadastro_curso.html'
	form_class = forms.CursoForm
	success_url = reverse_lazy('sucesso')

class InscricaoAluno(generic.CreateView):
	model = Certificado
	# template_name = 
	success_url = reverse_lazy('sucesso')


class CadastroCurso_Aluno(generic.TemplateView):
	template_name = 'certificados/redirect.html'
	#forms_class = forms.CertificadoForm
	#success_url = reverse_lazy('sucesso')

	def get_context_data(self,**kwargs):
		context = super(CadastroCurso_Aluno,self).get_context_data(**kwargs)

		pkAluno = self.kwargs.get('pkAluno')
		pkCurso = self.kwargs.get('pkCurso')

		context['Aluno'] = Participante.objects.filter(pk = pkAluno)[0]
		context['Curso'] = Curso.objects.filter(pk = pkCurso)[0]

		Certificado(participante=context['Aluno'],curso=context['Curso']).save()

		context['url'] = '/dados_curso/'+pkCurso

		return context




















def lista_cursos (request):
	cursos = Curso.objects.all()
	return render (request, 'certificados/listacursos.html',{'cursos' : cursos })





def lista_participantes (request):
	participantes = Participante.objects.all()
	return render (request, 'certificados/listaparticipante.html',{'participantes' : participantes})






















def tela (request):
	return render (request, 'certificados/template.html', {})




def sucesso(request):
	return render (request, 'certificados/sucesso.html', {})





def base (request):
	return render(request, 'certificados/base.html')











def gerar_certificado (request, pk):
	return button_create(request,pk)




def button_create (request, pk):#args, obj, request,pk, self

		certificados = Certificado.objects.get(pk=pk)

		doc = DocxTemplate(certificados.curso.modelo)
		context = { 
	    	"nome" : certificados.participante.nome,
	    	"cpf" : certificados.participante.cpf,
	    	"email" : certificados.participante.email,
	    	"matricula" : certificados.participante.matricula,
	    	"telefone" : certificados.participante.telefone,

	    	"nome_curso": certificados.curso.nome,
	    	"carga_horaria" : certificados.curso.carga_horaria,
	    	"coordenador" : certificados.curso.coordenador,
	    	"ministrante" : certificados.curso.ministrante,
	    	"cidade" : certificados.curso.cidade,
	        "data_inicio": certificados.curso.inicio,
	        "data_fim": certificados.curso.fim

	    	}
		print context
		filename = "%s%s.docx" % (certificados.curso.pk, certificados.participante.pk)
		doc.render(context)
		doc.save(filename)
		os.system('unoconv %s' % filename)
		print filename
		filename = filename[:-4]+"pdf"
		mimetypes.init()
		try:
			#file_path = settings.UPLOAD_LOCATION + '/' + filename
			file_path = filename
			fsock = open(file_path,"r")
			#file = fsock.read()
			#fsock = open(file_path,"r").read()
			#file_name = os.path.basename(file_path)
			#file_size = os.path.getsize(file_path)
			#print "file size is: " + str(file_size)
			response = HttpResponse(fsock, content_type = "application/pdf")
			response['Content-Disposition'] = 'attachment; filename=' + filename            
		except Exception as ex:
			print ex
			response = HttpResponseNotFound()
		return response
		#return redirect( filename )
		# return render (request, 'certificados/buttonsave.html',{'certificados': certificados})
	    




