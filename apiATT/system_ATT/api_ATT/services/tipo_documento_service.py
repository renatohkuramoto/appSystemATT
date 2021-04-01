from ..models import TipoDocumento


def getDocumentsType():
    return TipoDocumento.objects.all()
