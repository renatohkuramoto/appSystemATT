from django.http import request
from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import file_service
from ..models import File
from ..serializers.file_serializer import FileSerializer


class FileUploadView(APIView):
    permission_classes = []
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileDownloadView(APIView):
    def get(self, request, id):
        _file = file_service.getFileById(id)
        if(_file):
            file_path = _file.file.path
            file_pointer = open(file_path,'rb')
            response = FileResponse(file_pointer)
            return response
        return Response(status=status.HTTP_400_BAD_REQUEST)
