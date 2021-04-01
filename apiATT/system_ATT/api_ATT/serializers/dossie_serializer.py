from rest_framework import serializers
from ..models import Dossie
from .protocolo_serializer import ProtocoloSerializer


class DossieSerializer(serializers.ModelSerializer):

    protocolos = ProtocoloSerializer(many=True, read_only=True)

    class Meta:
        model = Dossie
        fields = [
            'id_dossie',
            'id_cliente',
            'flag_cadastro_completo',
            'flag_copia_rg_cnh',
            'flag_comprovante_endereco',
            'flag_comprovante_ocupacao',
            'flag_certidao_federal',
            'flag_certidao_estadual',
            'flag_certidao_militar',
            'flag_certidao_eleitoral',
            'flag_requerimento_comandante',
            'flag_declaracao_antecedentes',
            'flag_declaracao_seguranca_acervo',
            'flag_declaracao_endereco_acervo',
            'flag_termo_ciencia_compromisso',
            'flag_laudo_psicologico',
            'flag_laudo_tecnico',
            'flag_filiacao',
            'flag_comprovante_pagamento_gru',
            'protocolos'
        ]
