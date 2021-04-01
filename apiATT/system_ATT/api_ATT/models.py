from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.utils import timezone
import os


class PreCliente(models.Model):
    id_pre_cliente = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=50, null=False, blank=False)
    numero_rg = models.CharField(max_length=15, null=False, blank=False)
    numero_cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=25, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    logradouro = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    numero_residencia = models.CharField(max_length=10, null=False,
                                         blank=False)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    nacionalidade = models.CharField(max_length=50, null=False, blank=False)
    naturalidade = models.CharField(max_length=50, null=False, blank=False)
    emprego_fixo = models.BooleanField()
    possui_antecedentes = models.BooleanField()
    ciente_das_validacoes = models.BooleanField()
    activate = models.BooleanField(default=False)
    insert_date = models.DateTimeField(default=timezone.now,
                                       null=True, blank=True)

    class Meta:
        ordering = ['id_pre_cliente']

    def __str__(self):
        return self.nome_completo


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=50, null=False, blank=False)
    numero_rg = models.CharField(max_length=15, null=False, blank=False)
    numero_cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=25, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    logradouro = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    numero_residencia = models.CharField(max_length=10, null=False,
                                         blank=False)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    nacionalidade = models.CharField(max_length=50, null=False, blank=False)
    naturalidade = models.CharField(max_length=50, null=False, blank=False)
    activate = models.BooleanField(default=False)
    insert_date = models.DateTimeField(default=timezone.now,
                                       null=True, blank=True)

    class Meta:
        ordering = ['id_cliente']

    def __str__(self):
        return f'{self.id_cliente}, {self.nome_completo}'


class InformacoesExtraCliente (models.Model):
    id_informacao_extra = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente',
                                   related_name='informacoes_extras',
                                   on_delete=models.CASCADE,
                                   db_constraint=False)
    nome_pai = models.CharField(max_length=50, null=True, blank=True)
    nome_mae = models.CharField(max_length=50, null=True, blank=True)
    profissao = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.id_cliente


class TipoPagamento (models.Model):
    id_tipo_pagamento = models.AutoField(primary_key=True)
    tipo_pagamento = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return {
            'id_tipo_pagamento': self.id_tipo_pagamento,
            'tipo_pagamento': self.tipo_pagamento
        }


class Dossie(models.Model):
    id_dossie = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', related_name='dossies',
                                   on_delete=models.CASCADE,
                                   db_constraint=False)
    flag_cadastro_completo = models.BooleanField(null=True, blank=True)
    flag_copia_rg_cnh = models.BooleanField(null=True, blank=True)
    flag_comprovante_endereco = models.BooleanField(null=True, blank=True)
    flag_comprovante_ocupacao = models.BooleanField(null=True, blank=True)
    flag_certidao_federal = models.BooleanField(null=True, blank=True)
    flag_certidao_estadual = models.BooleanField(null=True, blank=True)
    flag_certidao_militar = models.BooleanField(null=True, blank=True)
    flag_certidao_eleitoral = models.BooleanField(null=True, blank=True)
    flag_requerimento_comandante = models.BooleanField(null=True, blank=True)
    flag_declaracao_antecedentes = models.BooleanField(null=True, blank=True)
    flag_declaracao_seguranca_acervo = models.BooleanField(null=True,
                                                           blank=True)
    flag_declaracao_endereco_acervo = models.BooleanField(null=True,
                                                          blank=True)
    flag_termo_ciencia_compromisso = models.BooleanField(null=True, blank=True)
    flag_laudo_psicologico = models.BooleanField(null=True, blank=True)
    flag_laudo_tecnico = models.BooleanField(null=True, blank=True)
    flag_filiacao = models.BooleanField(null=True, blank=True)
    flag_comprovante_pagamento_gru = models.BooleanField(null=True, blank=True)
    insert_date = models.DateTimeField(default=timezone.now, null=True,
                                       blank=True)

    def __str__(self):
        return str(self.id_dossie)


class Protocolo(models.Model):
    id_protocolo = models.AutoField(primary_key=True)
    id_dossie = models.ForeignKey('Dossie', related_name='protocolos',
                                  on_delete=models.CASCADE,
                                  db_constraint=False,
                                  null=True)
    num_protocolo = models.IntegerField()
    dt_protocolo = CharField(max_length=50,
                             null=True,
                             blank=True)
    insert_date = DateTimeField(default=timezone.now, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    subsecao = models.CharField(max_length=50, null=True, blank=True)
    servico = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.num_protocolo)


class ProtocoloDetails(models.Model):
    protocolo = models.ForeignKey(Protocolo, related_name='detalhes',
                                  null=True,
                                  on_delete=models.CASCADE)
    dt_aviso = models.DateTimeField(null=True, blank=True)
    mensagens = models.CharField(max_length=50, null=True, blank=True)
    ciencia_registrada = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.id_protocolo)


class Recibo(models.Model):
    id_recibo = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    id_tipo_pagamento = models.ForeignKey('TipoPagamento',
                                          on_delete=models.CASCADE)
    num_recibo = models.IntegerField()
    dt_emissao_recibo = models.DateField(default=timezone.now)
    vl_recibo = models.IntegerField()

    def __str__(self):
        return {
            'id_recibo': self.id_recibo,
            'id_cliente': self.id_cliente,
            'id_tipo_pagamento': self.id_tipo_pagamento,
            'num_recibo': self.num_recibo,
            'dt_emissao_recibo': self.dt_emissao_recibo,
            'vl_recibo': self.vl_recibo,
        }


class Etapa(models.Model):
    id_etapa = models.AutoField(primary_key=True)
    descricao_etapa = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return {
            'descricao_etapa': self.descricao_etapa
        }


class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    descricao_documento = models.CharField(max_length=30,
                                           null=False, blank=False)

    def __str__(self):
        return {
            'descricao_documento': self.descricao_documento
        }


class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    id_tipo_documento = models.ForeignKey('TipoDocumento',
                                          on_delete=models.CASCADE,
                                          related_name='tipo_documento',
                                          db_constraint=False)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE,
                                   related_name='documentos',
                                   db_constraint=False)
    numero_documento = models.CharField(max_length=50, null=False, blank=False)
    extra_field1 = models.CharField(max_length=50, null=True, blank=True)
    extra_field2 = models.CharField(max_length=50, null=True, blank=True)
    extra_field3 = models.CharField(max_length=50, null=True, blank=True)
    extra_field4 = models.CharField(max_length=50, null=True, blank=True)
    path = models.FileField(blank=True, null=True)
    file_ok = models.BooleanField(default=None)

    def __str__(self):
        return self.id_cliente


class DocumentoSalvos(models.Model):
    id_file_salve = models.AutoField(primary_key=True)
    id_documento = models.ForeignKey('Documento',
                                     on_delete=models.CASCADE,
                                     related_name='documento_id')
    id_cliente = models.ForeignKey('Cliente',
                                   on_delete=models.CASCADE)
    filename = models.CharField(max_length=100, null=False, blank=False)


class File(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
