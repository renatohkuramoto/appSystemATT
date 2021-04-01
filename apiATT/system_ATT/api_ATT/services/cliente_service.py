from ..models import Cliente


def getLastRegisters():
    return Cliente.objects.raw('SELECT * FROM api_ATT_cliente ORDER BY id_cliente DESC LIMIT 10')


def getAllClients():
    return Cliente.objects.all()


def getClientByCPF(numero_cpf):
    try:
        return Cliente.objects.get(numero_cpf=numero_cpf)
    except Exception:
        return None


def getClientById(id):
    try:
        return Cliente.objects.get(id_cliente=id)
    except Exception:
        return None


def registerClient(novo_cliente):
    return Cliente.objects.create(
        nome_completo=novo_cliente.nome_completo,
        numero_rg=novo_cliente.numero_rg,
        numero_cpf=novo_cliente.numero_cpf,
        data_nascimento=novo_cliente.data_nascimento,
        sexo=novo_cliente.sexo,
        telefone=novo_cliente.telefone,
        cep=novo_cliente.cep,
        logradouro=novo_cliente.logradouro,
        bairro=novo_cliente.bairro,
        numero_residencia=novo_cliente.numero_residencia,
        complemento=novo_cliente.complemento,
        cidade=novo_cliente.cidade,
        estado=novo_cliente.estado,
        nacionalidade=novo_cliente.nacionalidade
    )


def updateCliente(cliente_bd, cliente_update):
    cliente_bd.nome_completo = cliente_update.nome_completo
    cliente_bd.numero_rg = cliente_update.numero_rg
    cliente_bd.numero_cpf = cliente_update.numero_cpf
    cliente_bd.data_nascimento = cliente_update.data_nascimento
    cliente_bd.sexo = cliente_update.sexo
    cliente_bd.telefone = cliente_update.telefone
    cliente_bd.cep = cliente_update.cep
    cliente_bd.logradouro = cliente_update.logradouro
    cliente_bd.bairro = cliente_update.bairro
    cliente_bd.numero_residencia = cliente_update.numero_residencia
    cliente_bd.complemento = cliente_update.complemento
    cliente_bd.cidade = cliente_update.cidade
    cliente_bd.estado = cliente_update.estado
    cliente_bd.nacionalidade = cliente_update.nacionalidade
    cliente_bd.naturalidade = cliente_update.naturalidade
    cliente_bd.save(force_update=True)


def deleteCliente(cliente):
    cliente.delete()
