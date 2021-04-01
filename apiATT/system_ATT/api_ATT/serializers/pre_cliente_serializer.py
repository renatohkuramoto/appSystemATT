from rest_framework import serializers
from ..models import PreCliente


class PreClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreCliente
        ordering = ['id_pre_cliente']
        fields = [
                    'id_pre_cliente',
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
                    'emprego_fixo',
                    'possui_antecedentes',
                    'ciente_das_validacoes',
                    'activate',
                    'insert_date'
                ]
