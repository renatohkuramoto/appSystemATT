from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import pre_cliente_service, tipo_documento_service, cliente_service
from ..serializers import pre_cliente_serializer, tipo_documento_serializer, cliente_ativo_serializer
from rest_framework.pagination import PageNumberPagination


class InfoCliente(APIView):
    def get(self, request, format=None):
        pagination = PageNumberPagination()
        clientes = pre_cliente_service.getAllClients()
        result = pagination.paginate_queryset(clientes, request)
        serializer = pre_cliente_serializer.PreClienteSerializer(result, many=True)
        return pagination.get_paginated_response(serializer.data)
    
    
class InfoClienteAtivo(APIView):
    def get(self, request, id, format=None):
        cliente = cliente_service.getClientById(id)
        if (cliente):
            serializer = cliente_ativo_serializer.ClienteSerializer(cliente)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class InfoListDocumentsType(APIView):
    def get(self, request, format=None):
        tipos = tipo_documento_service.getDocumentsType()
        serializer = tipo_documento_serializer.TipoDocumentoSerializer(tipos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
