from rest_framework import serializers
from ..models import Recibo


class ReciboSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recibo
        fields = [
                    'id_recibo',
                    'id_tipo_pagamento',
                    'num_recibo',
                    'dt_emissao_recibo',
                    'vl_recibo'
                ]
