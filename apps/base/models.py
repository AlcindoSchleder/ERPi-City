# -*- coding: utf-8 -*-

from django.db import models
from configs.configs import APP_DBMODES_CHOICES

from apps.cadastro.models.empresa import  Empresa


class Tenants(models.Model):
    pk_tenants = models.AutoField(primary_key=True)
    fk_empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    db_name = models.CharField(max_length=32, null=True, blank=True)
    db_mode = models.CharField(
        max_length=10, choices=APP_DBMODES_CHOICES, null=True, blank=True
    )

    class Meta:
        verbose_name = "Assinantes"

    def __unicode__(self):
        return u'%s: %s - DB: %s' % (self.fk_empresas.nome_razao_social, self.db_mode, self.db_mode)

    def __str__(self):
        return u'%s: %s - DB: %s' % (self.fk_empresas.nome_razao_social, self.db_mode, self.db_mode)
