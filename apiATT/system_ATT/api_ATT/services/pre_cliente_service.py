from ..models import PreCliente


def getLastRegisters():
    return PreCliente.objects.raw('SELECT * FROM api_ATT_precliente ORDER BY id_pre_cliente DESC LIMIT 10')


def getAllClients():
    return PreCliente.objects.all()


def getClientById(id):
    try:
        return PreCliente.objects.get(id_pre_cliente=id)
    except Exception:
        return None


def getClientByCPF(numero_cpf):
    try:
        return PreCliente.objects.get(numero_cpf=numero_cpf)
    except Exception:
        return None


def registerClient(novo_cliente):
    return PreCliente.objects.create(
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
        nacionalidade=novo_cliente.nacionalidade,
        naturalidade=novo_cliente.naturalidade,
        emprego_fixo=novo_cliente.emprego_fixo,
        possui_antecedentes=novo_cliente.possui_antecedentes,
        ciente_das_validacoes=novo_cliente.ciente_das_validacoes
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
    cliente_bd.emprego_fixo = cliente_update.emprego_fixo
    cliente_bd.possui_antecedentes = cliente_update.possui_antecedentes
    cliente_bd.ciente_das_validacoes = cliente_update.ciente_das_validacoes
    cliente_bd.save(force_update=True)


def deleteCliente(cliente):
    cliente.delete()


def ativarPreCliente(cliente_bd, status):
    cliente_bd.activate = status
    cliente_bd.save(force_update=True)
