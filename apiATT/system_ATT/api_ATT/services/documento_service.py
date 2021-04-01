from ..models import Documento, TipoDocumento, Cliente


def getDocumentoByClienteId(id_cliente):
    return Documento.objects.filter(id_cliente=id_cliente)
    

def getDocumentoByTypeAndId(id_cliente, tipo_documento_id):
    try:
        return Documento.objects.get(id_cliente=id_cliente, id_tipo_documento=tipo_documento_id)
    except Exception:
        return None

def getAllDocumentos():
    return Documento.objects.all()


def getDocumentoByNumber(numero_documento):
    try:
        return Documento.objects.get(numero_documento=numero_documento)
    except Exception:
        return None


def registerDocumento(new_documento):
    tipo_documento = TipoDocumento.objects.get(
        id_tipo_documento=new_documento.id_tipo_documento)
    id_cliente = Cliente.objects.get(
        id_cliente=new_documento.id_cliente
    )
    return Documento.objects.create(
        id_tipo_documento=tipo_documento,
        numero_documento=new_documento.numero_documento,
        id_cliente=id_cliente,
        extra_field1=new_documento.extra_field1,
        extra_field2=new_documento.extra_field2,
        extra_field3=new_documento.extra_field3,
        extra_field4=new_documento.extra_field4,
        path=new_documento.path,
        file_ok=new_documento.file_ok
    )


def updateRegistroDocumento(documento_db, new_documento):
    documento_db.numero_documento = new_documento.numero_documento
    documento_db.extra_field1 = new_documento.extra_field1
    documento_db.extra_field2 = new_documento.extra_field2
    documento_db.extra_field3 = new_documento.extra_field3
    documento_db.extra_field4 = new_documento.extra_field4
    documento_db.path = new_documento.path
    documento_db.file_ok = new_documento.file_ok
    documento_db.save(force_update=True)
