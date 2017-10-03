from django.conf.urls import include, url
from . import views

urlpatterns = [
    
    
    
    url(r'lista_curso',views.lista_cursos, name='lista_cursos'),

    url(r'^$',views.lista_participantes, name='lista_participantes'),
    
    url(r'^dados_curso/(?P<pk>[0-9]+)/$', views.Dadoscurso.as_view(), name = 'dados_curso' ),

    url(r'^button_create/(?P<pk>[0-9]+)/', views.button_create, name = 'button_create'),

    url(r'^certificado_gerar/(?P<pk>[0-9]+)/$',views.gerar_certificado, name ='certificado_gerar'),

    url(r'^inscrever/(?P<pkAluno>[0-9]+)/(?P<pkCurso>[0-9]+)',views.CadastroCurso_Aluno.as_view(), name ='inscrever'),

    url(r'^inscricao',views.InscricaoAluno.as_view(), name ='inscricao'),

    url(r'cadastro_curso', views.CadastroCurso.as_view(), name='cadastro-curso'),

    url(r'^cadastro_participante', views.CadastroParticipante.as_view(), name='cadastro-participantes'),
    
    url(r'^participantes/(?P<pk>[0-9]+)/$', views.ParticipantesDetailsView.as_view(), name='participantes'),
    
    url(r'base',views.base, name = 'base'),

    url(r'sucesso',views.sucesso, name = 'sucesso'),

    url(r'bodes',views.tela, name='bodes'),
]
