from rest_framework import serializers
from ..models import Etapa


class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = [
                    'id_etapa',
                    'descricao_etapa'
                ]
