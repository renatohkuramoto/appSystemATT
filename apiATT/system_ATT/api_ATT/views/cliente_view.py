from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from ..services import cliente_service
from ..serializers import cliente_serializer
from ..entities import cliente_entity
from validate_docbr import CPF


class ClienteList(APIView):
    '''
        Métodos da tabela Cliente sem parâmetros
    '''
    def get(self, request, format=None):
        pagination = PageNumberPagination()
        clientes = cliente_service.getAllClients()
        result = pagination.paginate_queryset(clientes, request)
        serializer = cliente_serializer.ClienteSerializer(result, many=True)
        return pagination.get_paginated_response(serializer.data)


class ClienteDetail(APIView):
    '''
        Métodos da tabela Cliente com parâmetros
    '''
    def get(self, request, cpf, format=None):
        cliente = cliente_service.getClientByCPF(cpf)
        if (cliente):
            serializer = cliente_serializer.ClienteSerializer(cliente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data={"msg": [{"cpf_cliente": "Nof Found"}]},
                        status=status.HTTP_404_NOT_FOUND)

    def put(self, request, cpf, format=None):
        cliente_bd = cliente_service.getClientById(cpf)
        if (cliente_bd is not None):
            serializer = cliente_serializer.ClienteSerializer(cliente_bd, data=request.data)
            if serializer.is_valid():
                #valida_cpf = CPF()
                nome_completo = serializer.validated_data['nome_completo'].upper()
                numero_rg = serializer.validated_data['numero_rg']
                numero_cpf = serializer.validated_data['numero_cpf']
                data_nascimento = serializer.validated_data['data_nascimento']
                sexo = serializer.validated_data['sexo']
                telefone = serializer.validated_data['telefone']
                cep = serializer.validated_data['cep']
                logradouro = serializer.validated_data['logradouro'].upper()
                bairro = serializer.validated_data['bairro'].upper()
                numero_residencia = serializer.validated_data['numero_residencia']
                complemento = serializer.validated_data['complemento'].upper()
                cidade = serializer.validated_data['cidade'].upper()
                estado = serializer.validated_data['estado'].upper()
                nacionalidade = serializer.validated_data['nacionalidade'].upper()
                naturalidade = serializer.validated_data['naturalidade'].upper()
                #if (valida_cpf.validate(cpf)):
                cliente_update = cliente_entity.Cliente(
                    nome_completo=nome_completo,
                    numero_rg=numero_rg,
                    numero_cpf=numero_cpf,
                    data_nascimento=data_nascimento,
                    sexo=sexo,
                    telefone=telefone,
                    cep=cep,
                    logradouro=logradouro,
                    bairro=bairro,
                    numero_residencia=numero_residencia,
                    complemento=complemento,
                    cidade=cidade,
                    estado=estado,
                    nacionalidade=nacionalidade,
                    naturalidade=naturalidade
                )
                cliente_service.updateCliente(cliente_bd, cliente_update)
                return Response(request.data, status=status.HTTP_200_OK)
            """return Response(data={"msg": [{"cpf_client": "invalid"}]},
                                status=status.HTTP_400_BAD_REQUEST)"""
            return Response(serializer.data,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"msg": [{"cpf_cliente": "Nof Found"}]},
                        status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, cpf, format=None):
        cliente = cliente_service.getClientByCPF(cpf)
        if (cliente):
            cliente_service.deleteCliente(cliente)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={"msg": [{"cpf_cliente": "Nof Found"}]},
                        status=status.HTTP_404_NOT_FOUND)
