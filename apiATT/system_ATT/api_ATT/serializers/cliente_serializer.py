from rest_framework import serializers
from ..models import Cliente
from .protocolo_serializer import ProtocoloSerializer
from .documento_serializer import DocumentoSerializer
from .info_extra_serializer import InfoExtraSerializer
from .dossie_serializer import DossieSerializer


class ClienteSerializer(serializers.ModelSerializer):

    protocolos = ProtocoloSerializer(many=True, read_only=True)
    documentos = DocumentoSerializer(many=True, read_only=True)
    informacoes_extras = InfoExtraSerializer(many=True, read_only=True)
    dossies = DossieSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        ordering = ['id_cliente']
        fields = [
                    'id_cliente',
                    'nome_completo',
                    'numero_rg',
                    'numero_cpf',
                    'data_nascimento',
                    'sexo',
                    'telefone',
                    'cep',
                    'logradouro',
                    'bairro',
                    'numero_residencia',
                    'complemento',
                    'cidade',
                    'estado',
                    'nacionalidade',
                    'naturalidade',
                    'activate',
                    'insert_date',
                    'informacoes_extras',
                    'documentos',
                    'dossies',
                    'protocolos'
                ]
