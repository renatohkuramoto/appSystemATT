
from django.urls import path
from .views import (cliente_view,
                    documento_view,
                    info_view,
                    pre_cliente_view,
                    dossie_view,
                    protocolo_view,
                    protocolo_details_view,
                    file_view,
                    informacoes_extras,
                    usuario_view,
                    token_view)

urlpatterns = [
     path('clientes/', cliente_view.ClienteList.as_view(), name='cliente-list'),
     path('clientes/<cpf>', cliente_view.ClienteDetail.as_view(), name='cliente-detail'),
     path('clientes/documentos/', documento_view.DocumentoList.as_view(), name='documento-list'),
     path('clientes/info/last-registers/', info_view.InfoCliente.as_view(), name='list-lastRegisters'),
     path('clientes/info/cliente-ativo/<id>', info_view.InfoClienteAtivo.as_view(), name='info-cliente-ativo'),
     path('clientes/info/list-types-documents/', info_view.InfoListDocumentsType.as_view(), name='list-documents-type'),
     path('clientes/documentos/<id_cliente>', documento_view.DocumentoDetail.as_view(), name='documento-detail'),
     path('clientes/documentos/download/<number>', documento_view.DownloadDocuments.as_view(), name='documento-download'),
     path('clientes/documentos/extra-info/<id>', informacoes_extras.InfoExtra.as_view(), name="client-extra-info"),
     path('pre_clientes/', pre_cliente_view.PreClienteList.as_view(), name='pre-cliente-list'),
     path('pre_clientes/<cpf>', pre_cliente_view.PreClienteDetail.as_view(), name='pre-cliente-detail'),
     path('pre_clientes/<cpf>/ativar_cadastro', pre_cliente_view.AtivarClienteDetail.as_view(), name='ativar-cliente-detail'),
     path('clientes/dossie/<id_cliente>', dossie_view.DossieDetail.as_view(), name='dossie-list'),
     path('protocolo/',protocolo_view.ProtocoloListar.as_view(), name='protocolo-list'),
     path('protocolo/create/', protocolo_view.ProtocoloCriar.as_view(), name='protocolo-create'),
     path('protocolo/<int:pk>/', protocolo_view.ProtocoloDetalhadoUpdateDelete.as_view(), name='protocolo-detail-update-delete'),
     path('protocolo/details/', protocolo_details_view.ProtocoloDetailsListarCriar.as_view(), name='protocolo-details'),
     path('files/', file_view.FileUploadView.as_view(), name='file-upload'),
     path('files/list/', file_view.FileListView.as_view(), name='file-list'),
     path('clientes/documentos/viewer/<number>', documento_view.DownloadDocuments.as_view(), name='viewer-documents'),
     path('clientes/documentos/download-all-documents/<id>', documento_view.DownloadAllDocuments.as_view(), name='download-all-documents'),
     path('usuarios/', usuario_view.UsuarioList.as_view(), name='usuario-list'),
     path('token/validate-token/', token_view.ValidateToken.as_view(), name='token-validate-list'),
     ]
