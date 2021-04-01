let url_host = 'http://54.39.228.181:8000/api/';


$(document).ready(function() {
    $('#tabelaDocumentos').DataTable();
});

//Tela Documentos
function getClientDocuments() {
    let input_cpf = document.querySelector('input[name=cpf]').value;
    let URL_TO_FETCH = url_host + 'clientes' + `/${input_cpf.toString()}`
    fetch(URL_TO_FETCH, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
        },})
        .then(function(response) {
            response.json().then(function(data) {
                let dados = data['documentos'];
                if (dados) {
                    popula(dados)
                } else {
                    let modal = document.querySelector('.modal-body');
                    if (response.status == 404) {
                        msgModal = 'Cliente não encontrado </br>';
                    }
                    modal.innerHTML = msgModal;
                    $('#modalError').modal('show');
                }
            });
        })
        .catch(function(err) {
            console.error('Failed retrieving information', err);
        });
}


function popula(objeto) {
    let t = $('#tabelaDocumentos').DataTable();

    for (i = 0; i < objeto.length; i++) {
        t.row.add([
            objeto[i]['id_documento'],
            objeto[i]['id_tipo_documento'],
            objeto[i]['numero_documento'],
            objeto[i]['extra_field1'],
            objeto[i]['extra_field2'],
            objeto[i]['extra_field3'],
            objeto[i]['extra_field4'],
            objeto[i]['extra_field5'],
            objeto[i]['extra_field6'],
            objeto[i]['extra_field7']
        ]).draw(false);
    }
}


//Tela Listar Pré Clientes

function listarPreClientes () {
    let URL_TO_FETCH = url_host + 'pre_clientes/'
    fetch(URL_TO_FETCH, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
        },})
        .then(function(response) {
            response.json().then(function(data) {
                console.log(data)
                dados = criaLinks(data.results, 'pre-clientes')
                populaListarCliente(dados)
            });
        })
        .catch(function(err) {
            console.error('Failed retrieving information', err);
        });
}


function criaLinks(objeto, rota) {
    let array = []
    for (var i = 0; i < objeto.length; i++) {
        array.push({
            "nome_completo": `<a href='${rota + '/' + objeto[i]['numero_cpf']}'>${objeto[i]['nome_completo']}</a>`,
            "numero_rg": objeto[i]['numero_rg'],
            "numero_cpf": objeto[i]['numero_cpf'],
            "telefone": objeto[i]['telefone'],
            "logradouro": objeto[i]['logradouro'],
            "activate": objeto[i]['activate'] == false ? 'Não' : 'Sim',
            "delete": `<h6 onclick="modelDeletarPreRegistro(${objeto[i]['numero_cpf']})" style="cursor: pointer;">Deletar <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-x-square-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm3.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/>
          </svg></h6>`
        })
    }
    return array
}

function criaLinksAtivos(objeto, rota) {
    let array = []
    for (var i = 0; i < objeto.length; i++) {
        array.push({
            "nome_completo": `<a href='${rota + '/' + objeto[i]['numero_cpf']}'>${objeto[i]['nome_completo']}</a>`,
            "numero_rg": objeto[i]['numero_rg'],
            "numero_cpf": objeto[i]['numero_cpf'],
            "telefone": objeto[i]['telefone'],
            "logradouro": objeto[i]['logradouro'],
            "activate": objeto[i]['activate'] == false ? 'Não' : 'Sim',
            "delete": `<h6 onclick="modelDeletarRegistroAtivo(${objeto[i]['numero_cpf']})" style="cursor: pointer;">Deletar <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-x-square-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm3.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/>
          </svg></h6>`
        })
    }
    return array
}

function criaLinksProtocolo(objeto, rota) {
    let array = []
    for (var i = 0; i < objeto.length; i++) {
        if (objeto[i].dossies[0].protocolos[0]) {
            array.push({
                "nome_completo": `<a href='${rota + '/' + objeto[i]['numero_cpf']}'>${objeto[i]['nome_completo']}</a>`,
                "num_protocolo": objeto[i].dossies[0].protocolos[0].num_protocolo,
                "numero_rg": objeto[i]['numero_rg'],
                "numero_cpf": objeto[i]['numero_cpf'],
                "telefone": objeto[i]['telefone'],
                "logradouro": objeto[i]['logradouro']
            })
        }
    }
    return array
}

function populaListarCliente(objeto) {
    let t = $('#tabelaClientes').DataTable();
    console.log(objeto)
    t
        .clear()
        .draw();

    for (i = 0; i < objeto.length; i++) {
        t.row.add([
            objeto[i]['nome_completo'],
            objeto[i]['numero_rg'],
            objeto[i]['numero_cpf'],
            objeto[i]['telefone'],
            objeto[i]['logradouro'],
            objeto[i]['activate'],
            objeto[i]['delete']
        ]).draw(false);
    }
}


function populaTabelaProtocolos(objeto) {
    console.log(objeto)
    let t = $('#tabelaClientes').DataTable();
    t
        .clear()
        .draw();

    for (i = 0; i < objeto.length; i++) {
        t.row.add([
            objeto[i]['nome_completo'],
            objeto[i]['num_protocolo'],
            objeto[i]['numero_rg'],
            objeto[i]['numero_cpf'],
            objeto[i]['telefone'],
            objeto[i]['logradouro']
        ]).draw(false);
    }
}


(function() {
    'use strict';
    window.addEventListener('load', function() {
      let forms = document.getElementsByClassName('needs-validation');
      let validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          event.preventDefault();  
          if (form.checkValidity() === false) {
            event.stopPropagation();
          } else {
            let new_button = '<button id="btnCadastrar" class="btn btn-success" type="button" disabled><span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Cadastrando</button>'
            $('#btnCadastrar').remove()
            $('#div-cadastrar').append(new_button)
            return registrarPreCliente();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  })();

function registrarPreCliente() {

    let dados = {}
    dados.nome_completo = $("#inputNomeCliente").val();
    dados.numero_rg = $("#inputRG").val();
    dados.numero_cpf = $("#inputCPF").val();
    dados.data_nascimento = $("#inputDataNascimento").val();
    dados.sexo = $( "#inputSexo option:selected").val();
    dados.telefone = $("#inputTelefone").val();
    dados.cep = $("#inputCEP").val();
    dados.logradouro = $("#inputLogradouro").val();
    dados.bairro = $("#inputBairro").val();
    dados.numero_residencia = $("#inputNumeroResidencia").val();
    dados.complemento = $("#inputComplemento").val();
    dados.cidade = $("#inputCidade").val();
    dados.estado = $( "#inputEstado option:selected").val();
    dados.nacionalidade = $("#inputNacionalidade").val();
    dados.naturalidade = $("#inputNaturalidade").val();

    if ($("#checkEmpregoFixo").prop('checked')) {
        dados.emprego_fixo = 1
    } else {
        dados.emprego_fixo = 0
    }

    if ($("#checkAntecedentes").prop('checked')) {
        dados.possui_antecedentes = 1
    } else {
        dados.possui_antecedentes = 0
    }

    if ($("#checkAceite").prop('checked')) {
        dados.ciente_das_validacoes = 1
    } else {
        dados.ciente_das_validacoes = 0
    }

    let modal = document.querySelector('.modal-body');

    fetch(url_host + 'pre_clientes/', {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token
            },
            body: JSON.stringify(dados),
        })
        .then((res) => {
            if (res.status == 201) {
                msgModal = 'Cliente cadastrado com sucesso!</br>';
                modal.innerHTML = msgModal;
                $("#btn-modal-pre-cadastro").click(function () {
                    redirect_pre_cliente(dados.numero_cpf);
                });
                return $('#modalPreCadastro').modal('show');
            } else if (res.status == 400) {
                msgModal = 'Cliente já existe na base!</br>';
                modal.innerHTML = msgModal;
                $("#btn-modal-pre-cadastro").click(function () {
                    desabilitarCampos();
                });
                $('#modalPreCadastro').modal('show');
            } else {
                msgModal = 'Erro interno. Tente mais tarde.</br>';
                modal.innerHTML = msgModal;
                $("#btn-modal-pre-cadastro").click(function () {
                    desabilitarCampos();
                });
                $('#modalPreCadastro').modal('show');
            }
        })
        .catch((err) => {
            console.log(err)
        });
}

function redirect_pre_cliente(numero_cpf) {
    location.replace('/system-att/pre-clientes/' + numero_cpf)
}


function atualizarPreCadastro() {
    let new_button = '<button id="btnCadastrar" class="btn btn-success" type="button" disabled><span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Salvando</button>'
    $('#btnCadastrar').remove()
    $('#div-cadastrar').append(new_button)
    let dados = {}
    let id_pre_cliente = $("#inputIdCliente").val();
    dados.nome_completo = $("#inputNomeCliente").val();
    dados.numero_rg = $("#inputRG").val();
    dados.numero_cpf = $("#inputCPF").val();
    dados.data_nascimento = $("#inputDataNascimento").val();
    dados.sexo = $("#inputSexo option:selected").val();
    dados.telefone = $("#inputTelefone").val();
    dados.cep = $("#inputCEP").val();
    dados.logradouro = $("#inputLogradouro").val();
    dados.bairro = $("#inputBairro").val();
    dados.numero_residencia = $("#inputNumeroResidencia").val();
    dados.complemento = $("#inputComplemento").val();
    dados.cidade = $("#inputCidade").val();
    dados.estado = $("#inputEstado option:selected").val();
    dados.nacionalidade = $("#inputNacionalidade").val();
    dados.naturalidade = $("#inputNaturalidade").val();

    if ($("#checkEmpregoFixo").prop('checked')) {
        dados.emprego_fixo = 1
    } else {
        dados.emprego_fixo = 0
    }

    if ($("#checkAntecedentes").prop('checked')) {
        dados.possui_antecedentes = 1
    } else {
        dados.possui_antecedentes = 0
    }

    if ($("#checkAceite").prop('checked')) {
        dados.ciente_das_validacoes = 1
    } else {
        dados.ciente_das_validacoes = 0
    }

    let modal = document.querySelector('.modal-body');

    fetch(url_host + 'pre_clientes/' + id_pre_cliente, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token
            },
            body: JSON.stringify(dados),
        })
        .then((res) => {
            if (res.status == 200) {
                msgModal = 'Cliente atualizado com sucesso!</br>';
                modal.innerHTML = msgModal;
                $('#modalPreCadastro').modal('show');
                reloadModalAlterarCadastro(dados.numero_cpf)
            } else if (res.status == 400) {
                msgModal = 'Problema na requisição!</br>';
                modal.innerHTML = msgModal;
                $('#modalPreCadastro').modal('show');
            } else {
                msgModal = 'Erro interno. Tente mais tarde.</br>';
                modal.innerHTML = msgModal;
                $('#modalPreCadastro').modal('show');
            }
        })
        .catch((err) => {
            console.log(err)
        });
}


function atualizarCadastroAtivo() {

    let dados = {}
    let id_pre_cliente = $("#inputIdCliente").val();
    dados.nome_completo = $("#inputNomeCliente").val();
    dados.numero_rg = $("#inputRG").val();
    dados.numero_cpf = $("#inputCPF").val();
    dados.data_nascimento = $("#inputDataNascimento").val();
    dados.sexo = $("#inputSexo option:selected").val();
    dados.telefone = $("#inputTelefone").val();
    dados.cep = $("#inputCEP").val();
    dados.logradouro = $("#inputLogradouro").val();
    dados.bairro = $("#inputBairro").val();
    dados.numero_residencia = $("#inputNumeroResidencia").val();
    dados.complemento = $("#inputComplemento").val();
    dados.cidade = $("#inputCidade").val();
    dados.estado = $("#inputEstado option:selected").val();
    dados.nacionalidade = $("#inputNacionalidade").val();
    dados.naturalidade = $("#inputNaturalidade").val();


    let modal = document.querySelector('.modal-body');

    fetch(url_host + 'clientes/' + id_pre_cliente, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token
            },
            body: JSON.stringify(dados),
        })
        .then((res) => {
            if (res.status == 200) {
                msgModal = 'Cliente atualizado com sucesso!</br>';
                modal.innerHTML = msgModal;
                $('#modalPreCadastro').modal('show');
                reloadModalAlterarCadastroAtivo(dados.numero_cpf)
            } else if (res.status == 400) {
                msgModal = 'Problema na requisição!</br>';
                modal.innerHTML = msgModal;
                $('#modalPreCadastro').modal('show');
            } else {
                msgModal = 'Erro interno. Tente mais tarde.</br>';
                modal.innerHTML = msgModal;
                $('#modalPreCadastro').modal('show');
            }
        })
        .catch((err) => {
            console.log(err)
        });
}


function deletarRegistroAtivarPreRegistro(id_pre_cliente) {
    fetch(url_host + 'pre_clientes/' + id_pre_cliente + '/ativar_cadastro', {
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + access_token
        },
    })
    .then((res) => {
        if (res.status == 204) {
            location.replace('/system-att/listar-clientes-ativos')
        }
    })
    .catch((err) => {
        console.log(err)
    });
}

function ativarCadastroExecute(dados) {
    id_pre_cadastro = $("#inputIdCliente").val();
    fetch(url_host + 'pre_clientes/' + id_pre_cadastro + '/ativar_cadastro', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
        },
        body: JSON.stringify({
            "activate": 1
        }),
    })
    .then((res) => {
        if (res.status == 200) {
            deletarRegistroAtivarPreRegistro(id_pre_cadastro)
        }
    })
    .catch((err) => {
        console.log(err)
    });
}


function deletarPreRegistro(numero_cpf) {
    fetch(url_host + 'pre_clientes/' + numero_cpf, {
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + access_token
        }
    })
    .then((res) => {
        if (res.status == 204) {
            listarPreClientes()
        }
    })
    .catch((err) => {
        console.log(err)
    });
}

function deletarRegistroAtivo(numero_cpf) {
    fetch(url_host + 'clientes/' + numero_cpf, {
        method: 'DELETE',
        headers : {
            'Authorization': 'Bearer ' + access_token
        }
    })
    .then((res) => {
        if (res.status == 204) {
            listarClientesAtivos()
        }
    })
    .catch((err) => {
        console.log(err)
    });
}


function deletarRegistroTelaDadosClientes(numero_cpf) {
    fetch(url_host + 'pre_clientes/' + numero_cpf, {
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + access_token
        }
    })
    .then((res) => {
        if (res.status == 204) {
            location.replace('/system-att/listar-pre-cliente')
        }
    })
    .catch((err) => {
        console.log(err)
    });
}


function deletarRegistroTelaDadosClientesAtivo(numero_cpf) {
    fetch(url_host + 'clientes/' + numero_cpf, {
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + access_token
        }
    })
    .then((res) => {
        if (res.status == 204) {
            location.replace('/system-att/listar-clientes-ativos')
        }
    })
    .catch((err) => {
        console.log(err)
    });
}


function listarClientesAtivos() {
    let URL_TO_FETCH = url_host + 'clientes/'
    fetch(URL_TO_FETCH, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
        },})
        .then(function(response) {
            response.json().then(function(data) {
                dados = criaLinksAtivos(data.results, 'clientes')
                populaListarCliente(dados)
            });
        })
        .catch(function(err) {
            console.error('Failed retrieving information', err);
        });
}


function listarProtocolosClientes() {
    let URL_TO_FETCH = url_host + 'clientes/'
    fetch(URL_TO_FETCH, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
        },})
        .then(function(response) {
            response.json().then(function(data) {
                dados = criaLinksProtocolo(data.results, 'protocolos')
                populaTabelaProtocolos(dados)
            });
        })
        .catch(function(err) {
            console.error('Failed retrieving information', err);
        });
}


(function() {
    'use strict';
    window.addEventListener('load', function() {
      let forms = document.getElementsByClassName('forms-info');
      let validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          event.preventDefault();
          let new_button = '<button id="btnSalvarInfoExtras" class="btn btn-warning" type="button" disabled><span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Salvando</button>'
          $('#btnSalvarInfoExtras').remove()
          $('#div-extras').append(new_button)
          return registarExtraInfo();
        }, false);
      });
    }, false);
  })();


function registarExtraInfo() {
    let dados = {}

    dados.id_cliente = $("#inputIdCliente").val();
    dados.nome_pai = $("#inputPai").val().toString().toUpperCase();
    dados.nome_mae = $("#inputMae").val().toString().toUpperCase();
    dados.profissao = $("#inputProfissao").val().toString().toUpperCase();

    let URL_TO_FETCH = url_host + 'clientes/documentos/extra-info/' + dados.id_cliente;
    fetch(URL_TO_FETCH, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
        },
        body: JSON.stringify(dados),
    })
    .then((res) => {
        if (res.status == 201) {
            location.reload()
        } else if (res.status == 204) {
            location.reload()
        } else {
            msgModal = 'Problema ao efetuar a solicitação.</br>';
            modal.innerHTML = msgModal;
            $('#modalPreCadastro').modal('show');
        }
    })
    .catch((err) => {
        console.log(err)
    });
}


function criaLinksDossie(objeto) {
    let array = []
    for (var i = 0; i < objeto.length; i++) {
        array.push({
            "nome_completo": `<a href='${'dossie/' + objeto[i]['id_cliente']}'>${objeto[i]['nome_completo']}</a>`,
            "numero_rg": objeto[i]['numero_rg'],
            "numero_cpf": objeto[i]['numero_cpf'],
            "telefone": objeto[i]['telefone'],
            "logradouro": objeto[i]['logradouro'],
            "activate": objeto[i]['activate'] == false ? 'Não' : 'Sim'
        })
    }
    return array
}


function populaTableDossie(objeto) {
    let t = $('#tabelaClientes').DataTable();
    console.log(objeto)
    t
        .clear()
        .draw();

    for (i = 0; i < objeto.length; i++) {
        t.row.add([
            objeto[i]['nome_completo'],
            objeto[i]['numero_rg'],
            objeto[i]['numero_cpf'],
            objeto[i]['telefone'],
            objeto[i]['logradouro'],
            objeto[i]['activate']
        ]).draw(false);
    }
}


function listarDossieClientes() {
    let URL_TO_FETCH = url_host + 'clientes/'
    fetch(URL_TO_FETCH, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
        },})
        .then(function(response) {
            response.json().then(function(data) {
                dados = criaLinksDossie(data.results)
                populaTableDossie(dados)
            });
        })
        .catch(function(err) {
            console.error('Failed retrieving information', err);
        });
}


(function() {
    'use strict';
    window.addEventListener('load', function() {
      let forms = document.getElementsByClassName('cadastro-protocolo');
      let validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          event.preventDefault();  
          if (form.checkValidity() === false) {
            event.stopPropagation();
          } else {
            return cadastrar_protocolo();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
})();

function cadastrar_protocolo() {
    let dados = {}
    dados.id_dossie = dados_dossie.id_dossie;
    dados.num_protocolo = $('#inputProtocolo').val();
  
    let modal = document.getElementById('messagem-protocolo');
    let numero_cpf = $('#numero-cpf').text();

    $('#btn-salvar-protocolo').remove()
	  let elemento = '<button class="btn btn-warning" type="button" disabled><span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>Salvando</button>'
	  $('#div-salvar-protocolo').append(elemento)

    fetch(url_host + 'protocolo/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
        },
        body: JSON.stringify(dados),
    })
    .then((res) => {
        if (res.status == 201) {
            msgModal = 'Protocolo registrado com sucesso.</br>';
            modal.innerHTML = msgModal;
            $("#btn-modal-protocolo").click(function () {
                redirect_detalhes_protocolo(numero_cpf);
            });
            $('#modalMessageProtocolo').modal('show');
        } else if (res.status == 204) {
            msgModal = 'Protocolo já cadastrado.</br>';
            modal.innerHTML = msgModal;
            $("#btn-modal-protocolo").click(function () {
                redirect_detalhes_protocolo(numero_cpf);
            });
            $('#modalMessageProtocolo').modal('show');
        } else {
            msgModal = 'Processo não encontrado ou serviço indisponível.</br>';
            modal.innerHTML = msgModal;
            $("#btn-modal-protocolo").click(function () {
                reload_cadastro_protocolo();
            });
            $('#modalMessageProtocolo').modal('show');
        }
    })
    .catch((err) => {
        console.log(err)
    });
  }