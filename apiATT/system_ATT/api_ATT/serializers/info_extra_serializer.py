from rest_framework import serializers
from ..models import InformacoesExtraCliente


class InfoExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacoesExtraCliente
        fields = [
            'id_cliente',
            'nome_pai',
            'nome_mae',
            'profissao'
        ]
