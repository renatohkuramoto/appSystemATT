from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from ..services import pre_cliente_service
from ..serializers import pre_cliente_serializer
from ..entities import pre_cliente_entity
from validate_docbr import CPF


class PreClienteList(APIView):
    '''
        Métodos da tabela Cliente sem parâmetros
    '''
    def get(self, request, format=None):
        pagination = PageNumberPagination()
        clientes = pre_cliente_service.getAllClients()
        result = pagination.paginate_queryset(clientes, request)
        serializer = pre_cliente_serializer.PreClienteSerializer(result,
                                                                 many=True)
        return pagination.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = pre_cliente_serializer.PreClienteSerializer(data=request.data)
        if serializer.is_valid():
            nome_completo = serializer.data['nome_completo'].upper()
            numero_rg = serializer.data['numero_rg']
            numero_cpf = serializer.data['numero_cpf']
            data_nascimento = serializer.data['data_nascimento']
            sexo = serializer.data['sexo'].upper()
            telefone = serializer.data['telefone']
            cep = serializer.data['cep']
            logradouro = serializer.data['logradouro'].upper()
            bairro = serializer.data['bairro'].upper()
            numero_residencia = serializer.data['numero_residencia']
            complemento = serializer.data['complemento'].upper()
            cidade = serializer.data['cidade'].upper()
            estado = serializer.data['estado'].upper()
            nacionalidade = serializer.data['nacionalidade'].upper()
            naturalidade = serializer.data['naturalidade'].upper()
            emprego_fixo = serializer.data['emprego_fixo']
            possui_antecedentes = serializer.data['possui_antecedentes']
            ciente_das_validacoes = serializer.data['ciente_das_validacoes']
            #valida_cpf = CPF()
            '''if (not valida_cpf.validate(cpf)):
                return Response(data={"msg": [{"cpf_cliente": "invalid"}]},
                                status=status.HTTP_400_BAD_REQUEST)'''
            if (pre_cliente_service.getClientByCPF(numero_cpf)):
                return Response(
                    data={"msg": [{"cpf_cliente": "Already exists"}]},
                    status=status.HTTP_400_BAD_REQUEST
                )
            novo_cliente = pre_cliente_entity.PreCliente(
                                                    nome_completo,
                                                    numero_rg,
                                                    numero_cpf,
                                                    data_nascimento,
                                                    sexo,
                                                    telefone,
                                                    cep,
                                                    logradouro,
                                                    bairro,
                                                    numero_residencia,
                                                    complemento,
                                                    cidade,
                                                    estado,
                                                    nacionalidade,
                                                    naturalidade,
                                                    emprego_fixo,
                                                    possui_antecedentes,
                                                    ciente_das_validacoes
                                                )
            pre_cliente_service.registerClient(novo_cliente)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PreClienteDetail(APIView):
    '''
        Métodos da tabela Cliente com parâmetros
    '''
    def get(self, request, cpf, format=None):
        cliente = pre_cliente_service.getClientByCPF(cpf)
        if (cliente):
            serializer = pre_cliente_serializer.PreClienteSerializer(cliente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data={"msg": [{"cpf_cliente": "Nof Found"}]},
                        status=status.HTTP_404_NOT_FOUND)

    def put(self, request, cpf, format=None):
        cliente_bd = pre_cliente_service.getClientById(cpf)
        if (cliente_bd is not None):
            serializer = pre_cliente_serializer.PreClienteSerializer(cliente_bd, data=request.data)
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
                emprego_fixo = serializer.validated_data['emprego_fixo']
                possui_antecedentes = serializer.validated_data['possui_antecedentes']
                ciente_das_validacoes = serializer.validated_data['ciente_das_validacoes']
                #if (valida_cpf.validate(cpf)):
                cliente_update = pre_cliente_entity.PreCliente(
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
                    naturalidade=naturalidade,
                    emprego_fixo=emprego_fixo,
                    possui_antecedentes=possui_antecedentes,
                    ciente_das_validacoes=ciente_das_validacoes
                )
                pre_cliente_service.updateCliente(cliente_bd, cliente_update)
                return Response(request.data, status=status.HTTP_200_OK)
            """return Response(data={"msg": [{"cpf_client": "invalid"}]},
                                status=status.HTTP_400_BAD_REQUEST)"""
            return Response(serializer.data,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"msg": [{"cpf_cliente": "Nof Found"}]},
                        status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, cpf, format=None):
        cliente = pre_cliente_service.getClientByCPF(cpf)
        if (cliente):
            pre_cliente_service.deleteCliente(cliente)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={"msg": [{"cpf_cliente": "Nof Found"}]},
                        status=status.HTTP_404_NOT_FOUND)


class AtivarClienteDetail(APIView):
    def put(self, request, cpf, format=None):
        cliente_bd = pre_cliente_service.getClientById(cpf)
        if (cliente_bd is not None):
            activate = request.data['activate']
            pre_cliente_service.ativarPreCliente(cliente_bd, activate)
            return Response(status=status.HTTP_200_OK)
        return Response(data={"msg": [{"cpf_cliente": "Nof Found"}]},
                        status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, cpf, format=None):
        cliente = pre_cliente_service.getClientById(cpf)
        if (cliente):
            pre_cliente_service.deleteCliente(cliente)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={"msg": [{"cpf_cliente": "Nof Found"}]},
                        status=status.HTTP_404_NOT_FOUND)
