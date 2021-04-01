from django.core.exceptions import RequestDataTooBig
from ..models import ProtocoloDetails
from ..serializers import ProtocoloDetailsSerializer
from rest_framework.generics import ListCreateAPIView, DestroyAPIView 
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status


class ProtocoloDetailsListarCriar(ListCreateAPIView):
    queryset = ProtocoloDetails.objects.all()
    serializer_class = ProtocoloDetailsSerializer
