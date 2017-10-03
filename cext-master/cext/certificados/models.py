# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin



class Curso (models.Model):
    nome = models.CharField(
        'nome',
        max_length = 100
        )

    inicio = models.DateField(
        'inicio do curso',
        auto_now=False, 
        auto_now_add=False
        )

    fim = models.DateField(
        'fim do curso',
        auto_now=False, 
        auto_now_add=False
        )

    carga_horaria = models.IntegerField(
        'carga horaria',
    )

    coordenador = models.CharField(
        'coordenador',
        max_length = 80
        )

    ministrante = models.CharField(
        'ministrante',
        max_length = 80
        )

    cidade = models.CharField(
        'cidade',
        max_length = 30)

    modelo = models.FileField(
    'modelo de certificados',
    upload_to=None,
    max_length=100 ,
    blank = True,
    null = True
    )

    def __str__(self):
        return self.nome


class Participante (models.Model):

    nome = models.CharField(
        'nome',
        max_length = 80)

    cpf = models.CharField(
        'cpf',
        max_length = 14)
    telefone = models.CharField(
        'telefone',
        max_length = 11)
    email = models.EmailField(
        'email',
        max_length = 254)
    matricula = models.CharField(
        'matricula',
        max_length = 11,
        blank = True,
        null = True
    )

    def __str__(self):
        return self.nome



class Certificado (models.Model):
    participante = models.ForeignKey(
        Participante,
        verbose_name = 'Participante',
        related_name = 'certificado',
    )

    curso = models.ForeignKey(
        Curso,
        verbose_name = 'Curso',
        related_name = 'certificado',
    )
    unique_together = (("participante", "curso"),)

    def __str__(self):
        return '%s - %s' % (self.participante.nome, self.curso.nome)

    