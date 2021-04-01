from rest_framework import serializers
from ..models import TipoDocumento


class TipoDocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoDocumento
        fields = [
            'id_tipo_documento',
            'descricao_documento'
        ]
