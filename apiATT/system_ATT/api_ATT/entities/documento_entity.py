class Documento:
    def __init__(self, id_tipo_documento, id_cliente, numero_documento,
                 extra_field1, extra_field2, extra_field3,
                 extra_field4, path, file_ok):
        self.id_tipo_documento = id_tipo_documento
        self.id_cliente = id_cliente
        self.numero_documento = numero_documento
        self.extra_field1 = extra_field1
        self.extra_field2 = extra_field2
        self.extra_field3 = extra_field3
        self.extra_field4 = extra_field4
        self.path = path
        self.file_ok = file_ok
