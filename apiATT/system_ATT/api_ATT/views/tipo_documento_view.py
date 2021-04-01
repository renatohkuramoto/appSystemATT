from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import tipo_documento.services
from ..serializers import tipo_documento_serializer


class TipoDocumentoView(APIView):
    def get(self, request, format=None):
        tipo_documento = tipo_documento.services.getAllDocumentsTypes()
        serializer = tipo_documento_serializer.TipoDocumentoSerializer(tipo_documento, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
