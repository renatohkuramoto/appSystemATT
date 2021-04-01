from requests.api import request
from ..models import Dossie, Protocolo
from requests import api
from bs4 import BeautifulSoup


def get_protocolo_by_dossie_id(id_dossie):
    try:
        return Protocolo.objects.get(id_dossie=id_dossie)
    except Exception:
        return None

def get_all_protocolos():
    return Protocolo.objects.all()


def get_protocolo_by_id(id_protocolo):
    try:
        return Protocolo.objects.get(id_protocolo=id_protocolo)
    except Exception:
        return None


def create_protocolo(novo_protocolo):
    

    return Protocolo.objects.create(
        id_dossie=novo_protocolo.id_dossie,
        num_protocolo=novo_protocolo.num_protocolo,
        dt_protocolo=novo_protocolo.dt_protocolo,
        insert_date=novo_protocolo.insert_date,
        status=novo_protocolo.status,
        subsecao=novo_protocolo.subsecao,
        servico=novo_protocolo.servico
    )

def update_protocolo(protocolo_bd, update_fields):
    protocolo_bd.update(**update_fields)
    protocolo_bd.save(force_update=True)


def delete_protocolo(protocolo):
    protocolo.delete()


def consulta_protocolo(protocolo, cpf):
    url = 'http://protocolosfpc.2rm.eb.mil.br/consulta_processo.php'
    _protocolo = int(protocolo)
    _cpf = str(cpf)
    cpf_formatado = '{}.{}.{}-{}'.format(_cpf[:3], _cpf[3:6], _cpf[6:9], _cpf[9:])
    print(cpf_formatado)
    payload = {'cpf_cnpj':0,'txt_cpf_cnpj': cpf_formatado ,'txt_protocolo':f'00{_protocolo}'}
    req = api.post(url,data=payload)
    res = req.text
    bs = BeautifulSoup(res,'html.parser')
    erro_ao_localizar = bs.select_one('#div_msg > strong')
    if erro_ao_localizar:
        print(erro_ao_localizar.text)
        return None
    print('passou')
    status = bs.select_one('#wrap > div > div > center:nth-child(6) > h3 > span').text
    cpf_requerente = bs.select_one('#wrap > div > div > div > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(2)').text
    data_protocolo = bs.select_one('#wrap > div > div > div > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(4)').text
    requerente = bs.select_one('#wrap > div > div > div > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(4)').text
    subsecao = bs.select_one('#wrap > div > div > div > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(2)').text
    servico = bs.select_one('#wrap > div > div > div > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(4)').text

    return {
        'status':status,
        'data_protocolo': data_protocolo, 
        'cpf': cpf_requerente,
        'requerente': requerente,
        'subsecao': subsecao,
        'servico': servico
        }

