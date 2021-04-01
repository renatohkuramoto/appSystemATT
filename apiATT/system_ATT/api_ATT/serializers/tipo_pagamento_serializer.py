from rest_framework import serializers
from ..models import TipoPagamento


class TipoPagamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoPagamento
        fields = [
                    'tipo_pagamento'
                ]
