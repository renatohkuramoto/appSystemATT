from django.core.exceptions import RequestDataTooBig
from requests.api import request
from ..models import Protocolo
from ..serializers import ProtocoloSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from ..services import protocolo_service, dossie_service, cliente_service
from ..entities import protocolo_entity


class ProtocoloListar(ListAPIView):
    queryset = Protocolo.objects.all()
    serializer_class = ProtocoloSerializer


class ProtocoloCriar(APIView):
    def post(self, request, format=None):
        serializer = ProtocoloSerializer(data=request.data)
        if (serializer.is_valid()):
            id_dossie = serializer.data['id_dossie']
            num_protocolo = serializer.data['num_protocolo']
            if (protocolo_service.get_protocolo_by_dossie_id(id_dossie)):
                return Response(data={'msg': [{'id_dossie': 'Already Exists'}]},
                                status=status.HTTP_204_NO_CONTENT)
            _dossie = dossie_service.getDossieById(id_dossie)
            _cliente = cliente_service.getClientById(_dossie.id_cliente_id)
            new_data = protocolo_service.consulta_protocolo(num_protocolo,_cliente.numero_cpf)
            if not new_data:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            id_dossie = dossie_service.getDossieById(id_dossie)
            dt_protocolo = new_data['data_protocolo']
            protocolo_status = new_data['status']
            subsecao = new_data['subsecao']
            servico = new_data['servico']
            novo_protocolo = protocolo_entity.Protocolo(id_dossie,num_protocolo,dt_protocolo,serializer.data['insert_date'],protocolo_status,subsecao,servico)
            if(protocolo_service.create_protocolo(novo_protocolo)):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProtocoloDetalhadoUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Protocolo.objects.all()
    serializer_class = ProtocoloSerializer
