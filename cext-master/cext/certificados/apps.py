# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class CertificadosConfig(AppConfig):
    name = 'certificados'

    def ready(self):
        import certificados.signals
