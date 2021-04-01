from .data_config import Api, credenciais, url_auth
import requests
from base64 import b64encode


def get_bearer_token(username, password):
    data = {
        "grant_type": "password",
        "client_id": credenciais()['client_id'],
        "client_secret": credenciais()['secret'],
        "username": username,
        "password": password
    }
    r = requests.post(url_auth(), json=data)
    return r.json()


def refresh_access_token(refresh_token, access_token):
    data = {
        "grant_type": "refresh_token",
        "client_id": credenciais()['client_id'],
        "client_secret": credenciais()['secret'],
        "refresh_token":  access_token
    }
    r = requests.post(url_auth(), json=data)
    if (r.status_code in [400, 401, 404, 500]):
        return None
    return r.json()


def getRegisters(token):
    bearer = 'Bearer ' + token
    header = {'Authorization': bearer}
    r = requests.get(Api() + 'clientes/info/last-registers/', headers=header)
    return r.json()['results']


def getListDocumentsTypes(token):
    bearer = 'Bearer ' + token
    header = {'Authorization': bearer}
    r = requests.get(url=Api() + 'clientes/info/list-types-documents/', headers=header)
    return r.json()


def getDocumentsByCliente(id_cliente):
    r = requests.get(url=Api() + 'clientes/' + id_cliente)
    return r.json()


def listarPreCliente(cpf, token):
    bearer = 'Bearer ' + token
    header = {'Authorization': bearer}
    r = requests.get(url=Api() + 'pre_clientes/' + cpf, headers=header)
    return r.json()


def listarClienteAtivo(cpf, token):
    bearer = 'Bearer ' + token
    header = {'Authorization': bearer}
    r = requests.get(url=Api() + 'clientes/' + cpf, headers=header)
    return r.json()

def listarExtraInfo(id_cliente, token):
    try:
        bearer = 'Bearer ' + token
        header = {'Authorization': bearer}
        r = requests.get(url=Api() + 'clientes/documentos/extra-info/' + str(id_cliente), headers=header)
        return r.json()
    except Exception:
        return None
    
    
def getClienteInfo(id_cliente, token):
    bearer = 'Bearer ' + token
    header = {'Authorization': bearer}
    try:
        r = requests.get(url=Api() + 'clientes/info/cliente-ativo/' + str(id_cliente), headers=header)
        return r.json()
    except Exception:
        return {}
    

def getDossie(id_cliente, token):
    bearer = 'Bearer ' + token
    header = {'Authorization': bearer}
    try:
        r = requests.get(url=Api() + 'clientes/dossie/' + str(id_cliente), headers=header)
        return r.json()
    except Exception:
        return {}


def is_valid_token(token):
    bearer = 'Bearer ' + token
    header = {'Authorization': bearer}
    try:
        r = requests.get(Api() + 'token/validate-token/', headers=header)
        if (r.status_code == 200):
            return True
        return None
    except Exception:
        return None
    

def get_data_requerimentos(cpf, token):
    bearer = 'Bearer ' + token
    header = {'Authorization': bearer}
    try:
        res = requests.get(url=Api()+f'clientes/{cpf}', headers=header)
        return res.json()
    except Exception:
        return {}
