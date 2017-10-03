# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Participante
from .models import Curso
from .models import Certificado

# Register your models here.
admin.site.register(Participante)

admin.site.register(Curso)

admin.site.register(Certificado)
