from flask import Blueprint, render_template, request, session, redirect, url_for
import requests, json, base64, re, os
from flask_cors import CORS
from .data_config import Api
from .services import *
from .models import Cliente
from .functions import *
from flask_weasyprint import HTML, render_pdf
from datetime import date
from functools import wraps
from intuitlib.exceptions import AuthClientError


dashboard = Blueprint('dashboard', __name__,
                      static_folder='static',
                      template_folder='templates',
                      static_url_path='/dashboard/static')

CORS(dashboard)

bearer_token = {}

def validate_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        global bearer_token
        if ('username' not in session.keys()):
            return redirect(url_for('.index'))
        if ('error' in bearer_token.keys()):
            return redirect(url_for('.index'))
        if (bearer_token):
            token = bearer_token['access_token']
            refresh_token = bearer_token['refresh_token']
            valid_token = is_valid_token(token)
            if (valid_token is None):
                new_token = refresh_access_token(refresh_token, token)
                if (new_token):
                    bearer_token = new_token
                    return bearer_token
                else:
                    return redirect(url_for('.index'))
        else:
            return redirect(url_for('.index'))
        return f(*args, **kwargs)
    return decorated


@dashboard.route('/', methods=['GET', 'POST'])
def index():
    global bearer_token
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        bearer_token = get_bearer_token(username, password)
        if ('error' in bearer_token.keys()):
            return render_template('login.html', error=1)
        session['username'] = username
        return redirect(url_for('.dash'))
    elif request.method == 'GET':
        return render_template('login.html')


@dashboard.route('/system-att/dashboard')
@validate_token
def dash():
    result_api = getRegisters(bearer_token['access_token'])
    ocorrencias = getDays(result_api)
    registros = list(ocorrencias.values())
    datas = list(ocorrencias.keys())

    range_graphic = len(registros)

    list_clientes = getLastRegisters(result_api)

    return render_template('dashboard.html',
                           type='Dashboard',
                           registros=registros,
                           total=int(sum(registros)),
                           datas=datas,
                           range_graphic=range_graphic + 5,
                           list_clientes=list_clientes,
                           token=bearer_token['access_token'])


@dashboard.route('/system-att/suporte')
@validate_token
def suporte():
    return render_template('suporte.html', type='Suporte')


@dashboard.route('/system-att/pre-clientes', methods=['GET', 'POST'])
@validate_token
def pre_clientes():
    global bearer_token
    opcao_sexual = {"MASC": "Masculino", "FEM": "Feminino"}
    estados = getEstados()
    return render_template('pre-clientes.html',
                           type='Pré cadastro de clientes',
                           estados=estados,
                           sexualidade=opcao_sexual,
                           token=bearer_token['access_token'])
    


@dashboard.route('/system-att/pre-clientes/<cpf>', methods=['GET'])
@validate_token
def listar_pre_clientes_detalhes(cpf):
    global bearer_token
    result_api = listarPreCliente(str(cpf), bearer_token['access_token'])
    opcao_sexual = {"MASC": "Masculino", "FEM": "Feminino"}
    estados = getEstados()
    return render_template('dados-pre-clientes.html',
                           type='Gerenciar cliente: {}'.format(result_api['nome_completo']),
                           result_api=json.dumps(result_api),
                           estados=estados,
                           sexualidade=opcao_sexual,
                           token=bearer_token['access_token'])


@dashboard.route('/system-att/clientes/<cpf>', methods=['GET', 'POST'])
@validate_token
def listar(cpf):
    global bearer_token
    result_api = listarClienteAtivo(str(cpf), bearer_token['access_token'])
    tipos_documentos = getTypesDocuments(getListDocumentsTypes(bearer_token['access_token']))
    extra_info =  listarExtraInfo(result_api['id_cliente'], bearer_token['access_token'])
    opcao_sexual = {"MASC": "Masculino", "FEM": "Feminino"}
    estados = getEstados()
    return render_template('dados-clientes-ativos.html',
                           type='Cliente: {}'.format(result_api['nome_completo']),
                           result_api=json.dumps(result_api),
                           sexualidade=opcao_sexual,
                           estados=estados,
                           tipos_documentos=tipos_documentos,
                           cpf=result_api['numero_cpf'],
                           extra_info=json.dumps(extra_info),
                           token=bearer_token['access_token'])


@dashboard.route('/system-att/usuarios')
@validate_token
def usuarios():
    return render_template('usuario.html',
                           type='Gerenciamento de usuários do sistema')


@dashboard.route('/system-att/listar-pre-cliente')
@validate_token
def listar_pre_clientes():
    global bearer_token
    return render_template('listar-pre-clientes.html',
                           type='Listar Pré-Clientes',
                           token=bearer_token['access_token'])


@dashboard.route('/system-att/listar-clientes-ativos')
@validate_token
def listar_clientes_ativos():
    global bearer_token
    return render_template('listar-clientes-ativos.html',
                           type='Listar Clientes Ativos',
                           token=bearer_token['access_token'])


@dashboard.route('/system-att/requerimento/<cpf>')
@validate_token
def requerimento_comandante(cpf):
    global bearer_token
    data = get_data_requerimentos(cpf, bearer_token['access_token'])
    html = render_template('requerimento_comandante.html',data=data)
    return render_pdf(HTML(string=html))


@dashboard.route('/system-att/dsa/<cpf>')
@validate_token
def dsa(cpf):
    global bearer_token
    data = get_data_requerimentos(cpf, bearer_token['access_token'])
    html = render_template('dsa.html',data=data, hoje=date.today())
    return render_pdf(HTML(string=html))


@dashboard.route('/system-att/endereco_acervo/<cpf>')
@validate_token
def endereco_acervo(cpf):
    global bearer_token
    data = get_data_requerimentos(cpf, bearer_token['access_token'])
    html = render_template('endereco_acervo.html',data=data, hoje=date.today())
    return render_pdf(HTML(string=html))


@dashboard.route('/system-att/termo_ciencia/<cpf>')
@validate_token
def termo_ciencia(cpf):
    global bearer_token
    data = get_data_requerimentos(cpf, bearer_token['access_token'])
    html = render_template('termo_ciencia.html',data=data, hoje=date.today())
    return render_pdf(HTML(string=html))


@dashboard.route('/system-att/procuracao/<cpf>')
@validate_token
def procuracao(cpf):
    global bearer_token
    data = get_data_requerimentos(cpf, bearer_token['access_token'])
    html = render_template('procuracao.html',data=data, hoje=date.today())
    return render_pdf(HTML(string=html))


@dashboard.route('/system-att/clientes/documentos/viewer/<numero_documento>')
@validate_token
def view_documento(numero_documento):
    global bearer_token
    text = json.dumps(numero_documento)
    return render_template('pdf-viewer.html',
                           contents=text,
                           token=bearer_token['access_token'])


@dashboard.route('/system-att/dossie')
@validate_token
def listar_dossie():
    global bearer_token
    return render_template('listar-dossie.html',
                           token=bearer_token['access_token'])
    
    
@dashboard.route('/system-att/dossie/<id>')
@validate_token
def dossie(id):
    global bearer_token
    dossie = getDossie(id, bearer_token['access_token'])
    filiacao = listarExtraInfo(id, bearer_token['access_token'])
    dados_cliente = getClienteInfo(id, bearer_token['access_token'])
    return render_template('dossie.html',
                           dossie=json.dumps(dossie),
                           id_dossie=dossie['id_dossie'],
                           filiacao=json.dumps(filiacao),
                           dados_cliente=dados_cliente,
                           token=bearer_token['access_token'])
    
    
@dashboard.route('/system-att/dossie/<id_cliente>/gerar-pdf')
@validate_token
def gerar_pdf(id_cliente):
    global bearer_token
    text = id_cliente
    return render_template('viewer-all-pdfs.html',
                           contents=text,
                           token=bearer_token['access_token'])


@dashboard.route('/system-att/protocolos')
@validate_token
def listar_protocolos():
    global bearer_token
    return render_template('listar-protocolos.html',
                           type='Listagem de protocolos',
                           token=bearer_token['access_token'])
    
    
@dashboard.route('/system-att/protocolos/<cpf>')
@validate_token
def detalhes_protocolo(cpf):
    global bearer_token
    result_api = listarClienteAtivo(str(cpf),bearer_token['access_token'])
    num_cpf = mascara_cpf(result_api['numero_cpf'])
    return render_template('dados-protocolo.html',
                           type='Detalhes do Protocolo',
                           result_api=json.dumps(result_api),
                           cliente=result_api,
                           cpf=num_cpf,
                           token=bearer_token['access_token'])

@dashboard.route('/logout')
def logout():
    global bearer_token
    bearer_token = {}
    session.clear()
    return redirect(url_for('.index'))