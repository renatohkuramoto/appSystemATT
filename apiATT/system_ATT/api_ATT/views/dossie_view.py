from api_ATT.models import Dossie
from api_ATT.serializers.dossie_serializer import DossieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from ..services import dossie_service, cliente_service
from ..serializers import dossie_serializer
#from ..entities import dossie_entity
from validate_docbr import CPF


class DossieList(APIView):
    '''
        Métodos da tabela Dossiê sem parâmetros
    '''
    def get(self, request, format=None):
        pagination = PageNumberPagination()
        dossies = dossie_service.getAllDossies()
        result = pagination.paginate_queryset(dossies, request)
        serializer = dossie_serializer.DossieSerializer(result, many=True)
        return pagination.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DossieSerializer(data=request.data)
        if (serializer.is_valid()):
            print(serializer.data)
            id_cliente = serializer.data['id_cliente']
            if (dossie_service.getDossieByClienteId(id_cliente)):
                return Response(data={'msg': [{'numero_documento': 'Already Exists'}]},
                                status=status.HTTP_400_BAD_REQUEST)
            id_cliente = serializer.data['id_cliente']
            flag_cadastro_completo = serializer.data['flag_cadastro_completo'] 
            flag_copia_rg_cnh = serializer.data['flag_copia_rg_cnh'] 
            flag_comprovante_endereco = serializer.data['flag_comprovante_endereco']
            flag_comprovante_ocupacao = serializer.data['flag_comprovante_ocupacao']
            flag_certidao_federal = serializer.data['flag_certidao_federal']
            flag_certidao_estadual = serializer.data['flag_certidao_estadual']
            flag_certidao_militar = serializer.data['flag_certidao_militar']
            flag_certidao_eleitoral = serializer.data['flag_certidao_eleitoral']
            flag_requerimento_comandante = serializer.data['flag_requerimento_comandante']
            flag_declaracao_antecedentes = serializer.data['flag_declaracao_antecedentes']
            flag_declaracao_seguranca_acervo = serializer.data['flag_declaracao_seguranca_acervo']
            flag_declaracao_endereco_acervo = serializer.data['flag_declaracao_endereco_acervo']
            flag_termo_ciencia_compromisso = serializer.data['flag_termo_ciencia_compromisso']
            flag_laudo_psicologico = serializer.data['flag_laudo_psicologico']
            flag_laudo_tecnico = serializer.data['flag_laudo_tecnico']
            flag_filiacao = serializer.data['flag_filiacao']
            flag_comprovante_pagamento_gru= serializer.data['flag_comprovante_pagamento_gru']
            instancia_cliente = cliente_service.getClientById(id_cliente)
            novo_dossie = Dossie(
                id_cliente=instancia_cliente,
                flag_cadastro_completo=flag_cadastro_completo,
                flag_copia_rg_cnh=flag_copia_rg_cnh,
                flag_comprovante_endereco=flag_comprovante_endereco,
                flag_comprovante_ocupacao=flag_comprovante_ocupacao,
                flag_certidao_federal=flag_certidao_federal,
                flag_certidao_estadual=flag_certidao_estadual,
                flag_certidao_militar=flag_certidao_militar,
                flag_certidao_eleitoral=flag_certidao_eleitoral,
                flag_requerimento_comandante=flag_requerimento_comandante,
                flag_declaracao_antecedentes=flag_declaracao_antecedentes,
                flag_declaracao_seguranca_acervo=flag_declaracao_seguranca_acervo,
                flag_declaracao_endereco_acervo=flag_declaracao_endereco_acervo,
                flag_termo_ciencia_compromisso=flag_termo_ciencia_compromisso,
                flag_laudo_psicologico=flag_laudo_psicologico,
                flag_laudo_tecnico=flag_laudo_tecnico,
                flag_filiacao=flag_filiacao,
                flag_comprovante_pagamento_gru=flag_comprovante_pagamento_gru
                )

            dossie_service.createDossie(novo_dossie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DossieDetail(APIView):
    '''
        Métodos da tabela Dossie com parâmetros
    '''
    def get(self, request, id_cliente, format=None):
        dossie = dossie_service.getDossieByClienteId(id_cliente)
        if (dossie):
            serializer = dossie_serializer.DossieSerializer(dossie)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id_cliente, format=None):
        dossie_bd = dossie_service.getDossieByClienteId(id_cliente)
        if (dossie_bd is not None):
            serializer = dossie_serializer.DossieSerializer(data=request.data)
            if serializer.is_valid():
                update_fields = request.data
                dossie_service.updateCliente(dossie_bd, update_fields)
                return Response(request.data, status=status.HTTP_200_OK)
            return Response(serializer.data,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"msg": [{"id_cliente": "Not Found"}]},
                        status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id_cliente, format=None):
        dossie = dossie_service.getDossieByClienteId(id_cliente)
        if (dossie):
            dossie_service.deleteDossie(dossie)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={"msg": [{"id_cliente": "Nof Found"}]},
                        status=status.HTTP_404_NOT_FOUND)
