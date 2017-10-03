#from django.db.models.signals import post_save
#from django.dispatch import receiver
#
#from.models import Certificado
#from docxtpl import DocxTemplate
#from certificados import models
#import os
#
#@receiver(post_save, sender = models.Certificado)
#def my_handler(sender, instance, **kwargs):
#    
#    
    #doc = DocxTemplate(instance.curso.modelo)
    #context = { 
    	#"nome" : instance.participante.nome,
    	#"cpf" : instance.participante.cpf,
    	#"email" : instance.participante.email,
    	#"matricula" : instance.participante.matricula,
    	#"telefone" : instance.participante.telefone,
#
    	#"nome_curso": instance.curso.nome,
    	#"carga_horaria" : instance.curso.carga_horaria,
    	#"coordenador" : instance.curso.coordenador,
    	#"ministrante" : instance.curso.ministrante,
    	#"cidade" : instance.curso.cidade,
        #"data_inicio": instance.curso.inicio,
        #"data_fim": instance.curso.fim
#
    	#}
    #print context
    #filename = "%s%s.docx" % (instance.curso.pk, instance.participante.pk)
    #doc.render(context)
    #doc.save(filename)
    #os.system('unoconv %s' % filename)
