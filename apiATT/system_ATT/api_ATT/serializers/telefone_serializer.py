from rest_framework import serializers
from ..models import Telefone


class TelefoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Telefone
        fields = [
                    'id_telefone',
                    'id_tipo_telefone',
                    'num_telefone'
                ]
