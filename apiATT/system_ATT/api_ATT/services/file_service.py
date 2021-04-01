from ..models import File


def getFileById(id_file):
    try:
        return File.objects.get(id=id_file)
    except Exception:
        return None