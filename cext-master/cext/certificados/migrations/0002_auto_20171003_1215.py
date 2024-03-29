# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-03 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificado', to='certificados.Curso', unique=True, verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificado', to='certificados.Participante', unique=True, verbose_name='Participante'),
        ),
    ]
