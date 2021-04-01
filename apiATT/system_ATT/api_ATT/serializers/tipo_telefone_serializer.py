from rest_framework import serializers
from ..models import TipoTelefone


class TipoTelefoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoTelefone
        fields = [
                    'tipo_telefone'
                ]
