from rest_framework import serializers
from ..models import Documento
from ..serializers import tipo_documento_serializer


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = [
            'id_documento',
            'id_tipo_documento',
            'id_cliente',
            'numero_documento',
            'extra_field1',
            'extra_field2',
            'extra_field3',
            'extra_field4',
            'path',
            'file_ok'
        ]
