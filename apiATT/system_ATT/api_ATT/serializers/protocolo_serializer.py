from rest_framework import serializers
from ..models import Protocolo
from .protocolo_details_serializer import ProtocoloDetailsSerializer

class ProtocoloSerializer(serializers.ModelSerializer):
    detalhes = ProtocoloDetailsSerializer(many=True, read_only=True)
    class Meta:
        model = Protocolo
        ordering = ['id_protocolo']
        fields = [
                    'id_protocolo',
                    'id_dossie',
                    'num_protocolo',
                    'dt_protocolo',
                    'insert_date',
                    'status',
                    'subsecao',
                    'servico',
                    'detalhes',
                ]
