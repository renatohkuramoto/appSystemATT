from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import info_extra_serializer as I_serializer
from ..services import informacoes_extra_service as EI
from ..entities import informacoes_extras_entity as Entity_Info


class InfoExtra(APIView):
    def get(self, request, id, format=None):
        info = EI.get_extra_info_by_id(id)
        if (info):
            serializer = I_serializer.InfoExtraSerializer(info)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        info = EI.get_extra_info_by_id(id)
        serializer = I_serializer.InfoExtraSerializer(data=request.data)

        if (serializer.is_valid()):
            nova_info = Entity_Info.InformacoesExtras(
                    serializer.data['nome_pai'],
                    serializer.data['nome_mae'],
                    serializer.data['profissao'],
                    serializer.data['id_cliente']
                )
            if (info):
                EI.update_extra_info(info, nova_info)
                return Response(status=status.HTTP_204_NO_CONTENT)
            EI.register_extra_info(nova_info)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
