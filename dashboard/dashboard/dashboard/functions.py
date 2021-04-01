from .models import Cliente


def getDays(list_objects):
    days = {}
    for obj in list_objects:
        if obj['insert_date'][0:10] in days:
            days[obj['insert_date'][0:10]] += 1
        else:
            days[obj['insert_date'][0:10]] = 1
    return days


def getListRegisters(dict_getDays):
    registers = []
    for reg in dict_getDays:
        registers.append(reg.values())
    return registers


def getLastRegisters(lista):
    list_clientes = []
    for result in lista:
        list_clientes.append(Cliente(result['id_pre_cliente'],
                                     result['nome_completo'],
                                     result['telefone']))
    return list_clientes


def getTypesDocuments(lista):
    types = {}
    for item in lista:
        if item['id_tipo_documento'] not in types:
            types[item['id_tipo_documento']] = item['descricao_documento']
    return types


def getDocumentsObject(dicionario, list_types):
    dicionario = dicionario['documentos'][0]
    result = {}
    for key, values in dicionario.items():
        if (key != 'id_cliente'):
            if (values is not None and values != 'null'):
                if (key == 'id_tipo_documento'):
                    result[key] = list_types[values]
                else:
                    result[key] = values
    return(result)


def getEstados():
    return {
                "AC": "Acre (AC)",
                "AL": "Alagoas (AL)",
                "AP": "Amapá (AP)",
                "AM": "Amazonas (AM)",
                "BA": "Bahia (BA)",
                "CE": "Ceará (CE)",
                "DF": "Distrito Federal (DF)",
                "ES": "Espírito Santo (ES)",
                "GO": "Goiás (GO)",
                "MA": "Maranhão (MA)",
                "MT": "Mato Grosso (MT)",
                "MS": "Mato Grosso do Sul (MS)",
                "MG": "Minas Gerais (MG)",
                "PA": "Pará (PA)",
                "PB": "Paraíba (PB)",
                "PR": "Paraná (PR)",
                "PE": "Pernambuco (PE)",
                "PI": "Piauí (PI)",
                "RJ": "Rio de Janeiro (RJ)",
                "RN": "Rio Grande do Norte (RN)",
                "RS": "Rio Grande do Sul (RS)",
                "RO": "Rondônia (RO)",
                "RR": "Roraima (RR)",
                "SC": "Santa Catarina (SC)",
                "SP": "São Paulo (SP)",
                "SE": "Sergipe (SE)",
                "TO": "Tocantins (TO)"
    }

def ordernaJsonDossie(json):
    complete = {}
    incomplete = {}
    for element in json:
        if(json[element] == True):
            complete[element] = json[element]
        else:
            incomplete[element] = json[element]
    complete.update(incomplete)
    return complete

def mascara_cpf(numero_cpf):
    if len(numero_cpf) < 11:
        number = numero_cpf.zfill(11)
        return '{}.{}.{}-{}'.format(number[:3], number[3:6], number[6:9], number[9:])
    return '{}.{}.{}-{}'.format(numero_cpf[:3], numero_cpf[3:6], numero_cpf[6:9], numero_cpf[9:])