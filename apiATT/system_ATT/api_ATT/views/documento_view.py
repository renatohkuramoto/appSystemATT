from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.documento_serializer import DocumentoSerializer
from ..entities.documento_entity import Documento
from ..services import documento_service
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from ..config import path_documents
from django.views.decorators.clickjacking import xframe_options_exempt
import os
from PyPDF2 import PdfFileReader, PdfFileMerger


class DocumentoList(APIView):
    def get(self, request, format=None):
        clientes = documento_service.getAllDocumentos()
        serializer = DocumentoSerializer(clientes, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            documento = documento_service.getDocumentoByNumber(
                serializer.data['numero_documento']
                )
            
            if (documento == None):
                documento = documento_service.getDocumentoByTypeAndId(
                    serializer.data['id_cliente'],
                    serializer.data['id_tipo_documento']
                )
                
            if (documento != None and documento.id_tipo_documento.id_tipo_documento > 4):
                numero_documento = documento.numero_documento
            else:
                numero_documento = serializer.data['numero_documento']

            new_documento = Documento(
                    serializer.data['id_tipo_documento'],
                    serializer.data['id_cliente'],
                    numero_documento,
                    serializer.data['extra_field1'],
                    serializer.data['extra_field2'],
                    serializer.data['extra_field3'],
                    serializer.data['extra_field4'],
                    serializer.data['path'],
                    serializer.data['file_ok']
                )

            if (documento):
                print(documento.id_documento)
                new_documento.path = self.saveFileDocumento(request)
                documento_service.updateRegistroDocumento(
                    documento,
                    new_documento
                )
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                new_documento.path = self.saveFileDocumento(request)
                documento_service.registerDocumento(new_documento)
                return Response(status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def saveFileDocumento(self, request):
        if request.FILES:
            file = request.FILES['path']
            location = path_documents(request.data['id_cliente'])
            fs = FileSystemStorage(location=location)
            filename = fs.save(file.name, file)
            return filename
        return None


class DocumentoDetail(APIView):
    def get(self, request, id_cliente, format=None):
        documento = documento_service.getDocumentoByClienteId(id_cliente)
        if (documento):
            serializer = DocumentoSerializer(documento)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data=[],
                        status=status.HTTP_404_NOT_FOUND)


class DownloadDocuments(APIView):
    @xframe_options_exempt
    def get(self, request, number, format=None):
        documento = documento_service.getDocumentoByNumber(number)
        if (documento):
            file = documento.path
            file_path = path_documents(documento.id_cliente.id_cliente) + f'/{str(file)}'
            file_pointer = open(file_path, 'rb')
            response = FileResponse(file_pointer)
            return response
        return Response(status=status.HTTP_404_NOT_FOUND)
    

class DownloadAllDocuments(APIView):
    @xframe_options_exempt
    def get(self, request, id, format=None):
        documents = documento_service.getDocumentoByClienteId(id)
        if (documents):
            id_cliente = documents[0].id_cliente.id_cliente
            file_path = path_documents(id_cliente)
            try :
                os.remove(file_path + f'/{id_cliente}_full.pdf')
            except Exception:
                pass
            pdf_files = [arq for arq in os.listdir(file_path) if arq.endswith('pdf')]
            merger = PdfFileMerger()

            for arq in pdf_files:
                merger.append(PdfFileReader(os.path.join(file_path, arq), "rb"))
                
            full_file = f'{id_cliente}_full.pdf'
            merger.write(os.path.join(file_path, full_file))
            file_pointer = open(file_path + f'/{full_file}', 'rb')
            response = FileResponse(file_pointer)
            return response
        return Response(status=status.HTTP_404_NOT_FOUND)
