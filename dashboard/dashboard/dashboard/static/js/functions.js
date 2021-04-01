function FormataRG(rg) {
  rg = rg.replace(/\D/g, "");
  rg = rg.replace(/(\d{1,2})(\d{3})(\d{3})(\d{1})$/, "$1.$2.$3-$4");
  return rg
}

// Função para validar CPF página clientes.html
function validaCPF() {

  let elementCPF = document.getElementById('inputCPF');
  let strCPF = elementCPF.value;
  let Soma;
  let Resto;
  Soma = 0;
  if (strCPF == "00000000000") return false;

  for (i = 1; i <= 9; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (11 - i);
  Resto = (Soma * 10) % 11;

  if ((Resto == 10) || (Resto == 11)) Resto = 0;
  if (Resto != parseInt(strCPF.substring(9, 10))) {
    elementCPF.style.border = "solid #FF0000";
    return false
  }

  Soma = 0;
  for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (12 - i);
  Resto = (Soma * 10) % 11;

  if ((Resto == 10) || (Resto == 11)) Resto = 0;
  if (Resto != parseInt(strCPF.substring(10, 11))) {
    elementCPF.style.border = 'solid #FF0000'
    return false
  }
  elementCPF.style.border = 'solid #36C91C';
  return true;
}


// Função que preenche os dados de endereço após digitar o CEP
function preencheLogradouro() {
  let cep = document.getElementById('inputCEP');

  let URL_TO_FETCH = `https://viacep.com.br/ws/${cep.value}/json/`

  fetch(URL_TO_FETCH)
    .then(function(response) {
      response.json().then(function(data) {
        if (!data.erro) {
          document.getElementById('inputLogradouro').value = data['logradouro'];
          document.getElementById('inputBairro').value = data['bairro'];
          document.getElementById('inputCidade').value = data['localidade'];
          document.getElementById('inputEstado').value = data['uf'];
        }
      });
    })
}


function habilitarCampos() {
  $('#inputNomeCliente').attr('disabled', false);
  $('#inputRG').attr('disabled', false);
  $('#inputCPF').attr('disabled', false);
  $('#inputDataNascimento').attr('disabled', false);
  $('#inputSexo').attr('disabled', false);
  $('#inputTelefone').attr('disabled', false);
  $('#inputCEP').attr('disabled', false);
  $('#inputLogradouro').attr('disabled', false);
  $('#inputBairro').attr('disabled', false);
  $('#inputNumeroResidencia').attr('disabled', false);
  $('#inputComplemento').attr('disabled', false);
  $('#inputCidade').attr('disabled', false);
  $('#inputEstado').attr('disabled', false);
  $('#inputNacionalidade').attr('disabled', false);
  $('#inputNaturalidade').attr('disabled', false);
  $('#checkEmpregoFixo').attr('disabled', false);
  $('#checkAntecedentes').attr('disabled', false);
  $('#checkAceite').attr('disabled', false);
  $('#btnNovo').attr('disabled', true);
  $('#btnCadastrar').attr('disabled', false);
  $('#btnCancelar').attr('disabled', false);
}

function desabilitarCampos() {
  limparCampos()
  $('#inputNomeCliente').attr('disabled', true);
  $('#inputRG').attr('disabled', true);
  $('#inputCPF').attr('disabled', true);
  $('#inputCPF').css('background', '');
  $('#inputDataNascimento').attr('disabled', true);
  $('#inputSexo').attr('disabled', true);
  $('#inputTelefone').attr('disabled', true);
  $('#inputCEP').attr('disabled', true);
  $('#inputLogradouro').attr('disabled', true);
  $('#inputBairro').attr('disabled', true);
  $('#inputNumeroResidencia').attr('disabled', true);
  $('#inputComplemento').attr('disabled', true);
  $('#inputCidade').attr('disabled', true);
  $('#inputEstado').attr('disabled', true);
  $('#inputNacionalidade').attr('disabled', true);
  $('#inputNaturalidade').attr('disabled', true);
  $('#checkEmpregoFixo').attr('disabled', true);
  $('#checkAntecedentes').attr('disabled', true);
  $('#checkAceite').attr('disabled', true);
  $('#btnNovo').attr('disabled', false);
  $('#btnCadastrar').attr('disabled', true);
  $('#btnCancelar').attr('disabled', true);
}

function desabilitarCamposCadastrado() {
  $('#inputNomeCliente').attr('disabled', true);
  $('#inputRG').attr('disabled', true);
  $('#inputCPF').attr('disabled', true);
  $('#inputCPF').css('background', '');
  $('#inputDataNascimento').attr('disabled', true);
  $('#inputSexo').attr('disabled', true);
  $('#inputTelefone').attr('disabled', true);
  $('#inputCEP').attr('disabled', true);
  $('#inputLogradouro').attr('disabled', true);
  $('#inputBairro').attr('disabled', true);
  $('#inputNumeroResidencia').attr('disabled', true);
  $('#inputComplemento').attr('disabled', true);
  $('#inputCidade').attr('disabled', true);
  $('#inputEstado').attr('disabled', true);
  $('#inputNacionalidade').attr('disabled', true);
  $('#inputNaturalidade').attr('disabled', true);
  $('#checkEmpregoFixo').attr('disabled', true);
  $('#checkAntecedentes').attr('disabled', true);
  $('#checkAceite').attr('disabled', true);
  $('#btnNovo').attr('disabled', false);
  $('#btnCadastrar').attr('disabled', true);
  $('#btnCancelar').attr('disabled', true);
}

function limparCampos() {
  $('#form_cadastro_clientes').each(function() {
    this.reset();
  });
}

function populaCamposPreCliente(data) {
  console.log(data)
  $('#inputIdCliente').val(data.id_pre_cliente);
  $('#inputNomeCliente').val(data.nome_completo);
  $('#inputRG').val(data.numero_rg);
  $('#inputCPF').val(data.numero_cpf);
  $('#inputDataNascimento').val(data.data_nascimento);
  $('#inputSexo').val(data.sexo);
  $('#inputTelefone').val(data.telefone);
  $('#inputCEP').val(data.cep);
  $('#inputLogradouro').val(data.logradouro);
  $('#inputBairro').val(data.bairro);
  $('#inputNumeroResidencia').val(data.numero_residencia);
  $('#inputComplemento').val(data.complemento);
  $('#inputCidade').val(data.cidade);
  $('#inputEstado').val(data.estado);
  $('#inputNacionalidade').val(data.nacionalidade);
  $('#inputNaturalidade').val(data.naturalidade);
  $('#checkEmpregoFixo').prop("checked", data.emprego_fixo);
  $('#checkAntecedentes').prop("checked", data.possui_antecedentes);
  $('#checkAceite').prop("checked", data.ciente_das_validacoes);
  $('#checkStatus').prop("checked", data.activate);
}


function populaCamposClientesAtivos(data, tipos_documentos, extra_info) {
  $('#inputIdCliente').val(data.id_cliente);
  $('#inputNomeCliente').val(data.nome_completo);
  $('#inputRG').val(data.numero_rg);
  $('#inputCPF').val(data.numero_cpf);
  $('#inputDataNascimento').val(data.data_nascimento);
  $('#inputSexo').val(data.sexo);
  $('#inputTelefone').val(data.telefone);
  $('#inputCEP').val(data.cep);
  $('#inputLogradouro').val(data.logradouro);
  $('#inputBairro').val(data.bairro);
  $('#inputNumeroResidencia').val(data.numero_residencia);
  $('#inputComplemento').val(data.complemento);
  $('#inputCidade').val(data.cidade);
  $('#inputEstado').val(data.estado);
  $('#inputNacionalidade').val(data.nacionalidade);
  $('#inputNaturalidade').val(data.naturalidade);
  $('#checkStatus').prop("checked", data.activate);

  if (extra_info) {
    $('#inputPai').val(extra_info.nome_pai);
    $('#inputMae').val(extra_info.nome_mae);
    $('#inputProfissao').val(extra_info.profissao);
  }

  let tipo, numero, status, nova_linha;
  for (var i = 0; i < data.documentos.length; i++) {
    tipo = `<td>${tipos_documentos[data.documentos[i].id_tipo_documento]}</td>`
    numero = `<td id="docNumber">${data.documentos[i].numero_documento}</td>`
    status = `<td>${data.documentos[i].file_ok == false ? '<span class="badge badge-danger">Upload Pendente</span>' : `<span style="cursor: pointer;" onclick="viewerDocumento('${data.documentos[i].numero_documento}')" class="badge badge-success">Vizualizar PDF</span>`}</td>`
    nova_linha = `<tr>${tipo + numero + status}</tr>`
    $("#documentoTable").append(nova_linha);
  }

  if (extra_info) {
    let tipo = `<td>Nome do Pai</td>`
    let descricao = extra_info.nome_pai? `<td>${extra_info.nome_pai}</td>` : '<td></td>'
    let info_status = extra_info.nome_pai? '<td><span class="badge badge-success">Enviado</span></td>' : '<td><span class="badge badge-danger">Pendente</span></td>'
    let linha = `<tr>${tipo + descricao + info_status}</tr>`
    $("#ExtraInfoTable").append(linha);

    tipo = `<td>Nome da Mãe</td>`
    descricao = extra_info.nome_mae? `<td>${extra_info.nome_mae}</td>` : '<td></td>'
    info_status = extra_info.nome_mae? '<td><span class="badge badge-success">Enviado</span></td>' : '<td><span class="badge badge-danger">Pendente</span></td>'
    linha = `<tr>${tipo + descricao + info_status}</tr>`
    $("#ExtraInfoTable").append(linha);

    tipo = `<td>Profissão</td>`
    descricao = extra_info.profissao? `<td>${extra_info.profissao}</td>` : '<td></td>'
    info_status = extra_info.profissao? '<td><span class="badge badge-success">Enviado</span></td>' : '<td><span class="badge badge-danger">Pendente</span></td>'
    linha = `<tr>${tipo + descricao + info_status}</tr>`
    $("#ExtraInfoTable").append(linha);
  }
}


function reloadModalAlterarCadastro(numero_cpf) {
  $("#btnModal").on('click', function() {
    location.replace('/system-att/pre-clientes/' + numero_cpf)
  });
}

function reloadModalAlterarCadastroAtivo(numero_cpf) {
  $("#btnModal").on('click', function() {
    location.replace('/system-att/clientes/' + numero_cpf)
  });
}

function ativarCadastroEventoModal() {
  $("#btnAtivarCadastro").on('click', function() {
    let new_button = '<button id="btnAtivarCadastro" class="btn btn-primary" type="button" disabled><span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Ativando...</button>'
    $('#btnAtivarCadastro').remove()
    $('#div-ativar').append(new_button)
    ativarCadastroExecute()
  });
}

function ativarPreCadastro() {
  let modal = document.getElementById('textModalAtivarPreCadastro');
  msgModal = 'Deseja ativar o cadastro?</br>';
  modal.innerHTML = msgModal;
  $('#modalAtivarCadastro').modal('show');
  ativarCadastroEventoModal()
}


function onclickDeletar(numero_cpf) {
  let cpf = numero_cpf
  $("#btnDeletar").on('click', function() {
    deletarPreRegistro(cpf)
  });
}

function onclickDeletarAtivos(numero_cpf) {
  let cpf = numero_cpf
  $("#btnDeletar").on('click', function() {
    deletarRegistroAtivo(cpf)
  });
}

function modelDeletarPreRegistro(numero_cpf) {
  let cpf = numero_cpf
  let modal = document.getElementById('dadosModalDeletar');
  msgModal = 'Deseja excluir o registro?.</br>';
  modal.innerHTML = msgModal;
  $('#modalDeletar').modal('show');
  onclickDeletar(cpf)
}

function modelDeletarRegistroAtivo(numero_cpf) {
  let cpf = numero_cpf
  let modal = document.getElementById('dadosModalDeletar');
  msgModal = 'Deseja excluir o registro?.</br>';
  modal.innerHTML = msgModal;
  $('#modalDeletar').modal('show');
  onclickDeletarAtivos(cpf)
}

function modelDeletarTelaDadosPreCliente() {
  let cpf = $('#inputCPF').val();
  deletarRegistroTelaDadosClientes(cpf);
}

function modelDeletarTelaDadosClienteAtivo() {
  let cpf = $('#inputCPF').val();
  deletarRegistroTelaDadosClientesAtivo(cpf);
}


function atualizarModalDocumentos() {

  let campos = {}
  campos.numero_documento = '<div class="form-group col-md-6" id="divNumeroDocumento"> <label for="inputNumeroDocumento">Número do documento</label><input type="number" class="form-control" id="inputNumeroDocumento" required/></div>'
  campos.rg_data_expedicao = '<div class="form-group col-md-6" id="divDataExpedicao"> <label for="inputExpedicao">Campo Data Expedição</label><input type="date" class="form-control" id="inputExpedicao" required/></div>'
  campos.rg_orgao_emissor = '<div class="form-group col-md-6" id="divOrgaoEmissor"> <label for="inputOrgaoEmissor">Orgão Emissor</label><input type="text" class="form-control" id="inputOrgaoEmissor" required/></div>'
  campos.cnh_validade = '<div class="form-group col-md-6" id="divCnhValidade"> <label for="inputCnhValidade">Validade CNH</label><input type="date" class="form-control" id="inputCnhValidade" required/></div>'
  campos.titulo_zona = '<div class="form-group col-md-6" id="divTituloZona"> <label for="inputTituloZona">Zona</label><input type="text" class="form-control" id="inputTituloZona" required/></div>'
  campos.titulo_secao = '<div class="form-group col-md-6" id="divTituloSecao"> <label for="inputTituloSecao">Seção</label><input type="text" class="form-control" id="inputTituloSecao" required/></div>'
  campos.titulo_municipio = '<div class="form-group col-md-6" id="divTituloMunicipio"> <label for="inputTituloMunicipio">Município</label><input type="text" class="form-control" id="inputTituloMunicipio" required/></div>'

  let choice = $("#inputTipoDocumento option:selected").val() <= 4 ? $("#inputTipoDocumento option:selected").val() : 'others';
  console.log($("#inputTipoDocumento option:selected").val())
  switch (choice) {
    case '1':
      $('#divNumeroDocumento').remove()
      $('#divDocumentos').append(campos.numero_documento)
      $('#divDocumentos').append(campos.rg_data_expedicao)
      $('#divDocumentos').append(campos.rg_orgao_emissor)
      $('#divCnhValidade').remove()
      $('#divTituloZona').remove()
      $('#divTituloSecao').remove()
      $('#divTituloMunicipio').remove()
      $('#inputNumeroDocumento').val($('#inputRG').val())
      break;
    case '2':
      $('#divNumeroDocumento').remove()
      $('#divDocumentos').append(campos.numero_documento)
      $('#divDataExpedicao').remove()
      $('#divOrgaoEmissor').remove()
      $('#divCnhValidade').remove()
      $('#divTituloZona').remove()
      $('#divTituloSecao').remove()
      $('#divTituloMunicipio').remove()
      $('#inputNumeroDocumento').val($('#inputCPF').val())
      break;
    case '3':
      $('#divNumeroDocumento').remove()
      $('#divDocumentos').append(campos.numero_documento)
      $('#divDataExpedicao').remove()
      $('#divOrgaoEmissor').remove()
      $('#divTituloZona').remove()
      $('#divTituloSecao').remove()
      $('#divTituloMunicipio').remove()
      $('#divDocumentos').append(campos.cnh_validade)
      break;
    case '4':
      $('#divNumeroDocumento').remove()
      $('#divDocumentos').append(campos.numero_documento)
      $('#divDataExpedicao').remove()
      $('#divOrgaoEmissor').remove()
      $('#divCnhValidade').remove()
      $('#divDocumentos').append(campos.titulo_zona)
      $('#divDocumentos').append(campos.titulo_secao)
      $('#divDocumentos').append(campos.titulo_municipio)
      break;
    case 'others':
      $('#divDataExpedicao').remove()
      $('#divOrgaoEmissor').remove()
      $('#divCnhValidade').remove()
      $('#divTituloZona').remove()
      $('#divTituloSecao').remove()
      $('#divTituloMunicipio').remove()
      $('#divNumeroDocumento').remove()
    default:
      $('#divDataExpedicao').remove()
      $('#divOrgaoEmissor').remove()
      $('#divCnhValidade').remove()
      $('#divTituloZona').remove()
      $('#divTituloSecao').remove()
      $('#divTituloMunicipio').remove()
      $('#divNumeroDocumento').remove()
  }
}

$(document).ready(function() {
  $("#form-documentos").on('submit', function(e) {
    e.preventDefault();
    let tipo = $("#inputTipoDocumento option:selected").text();
    let data = new FormData()

    switch (tipo) {
      case "CPF":
        data.append('path', document.getElementById('inputFile').files[0])
        data.append('numero_documento', $("#inputNumeroDocumento").val())
        data.append('id_cliente', $("#inputIdCliente").val())
        data.append('id_tipo_documento', $("#inputTipoDocumento option:selected").val())
        data.append('file_ok', 1)
        break;
      case "RG":

        data.append('path', document.getElementById('inputFile').files[0])
        data.append('numero_documento', $("#inputNumeroDocumento").val())
        data.append('id_cliente', $("#inputIdCliente").val())
        data.append('id_tipo_documento', $("#inputTipoDocumento option:selected").val())
        data.append('extra_field1', $("#inputExpedicao").val())
        data.append('extra_field2', $("#inputOrgaoEmissor").val().toUpperCase())
        data.append('file_ok', 1)
        break;
      case "TITULO ELEITOR":
        data.append('path', document.getElementById('inputFile').files[0])
        data.append('numero_documento', $("#inputNumeroDocumento").val())
        data.append('id_cliente', $("#inputIdCliente").val())
        data.append('id_tipo_documento', $("#inputTipoDocumento option:selected").val())
        data.append('extra_field1', $("#inputTituloZona").val())
        data.append('extra_field2', $("#inputTituloSecao").val())
        data.append('extra_field3', $("#inputTituloMunicipio").val().toUpperCase())
        data.append('file_ok', 1)
        break;
      case "CNH":
        data.append('path', document.getElementById('inputFile').files[0])
        data.append('numero_documento', $("#inputNumeroDocumento").val())
        data.append('id_cliente', $("#inputIdCliente").val())
        data.append('id_tipo_documento', $("#inputTipoDocumento option:selected").val())
        data.append('extra_field1', $("#inputCnhValidade").val())
        data.append('file_ok', 1)
        break;
      default:
        data.append('path', document.getElementById('inputFile').files[0])
        data.append('numero_documento', md5(document.getElementById('inputFile').files[0].name.split('.')[0]).slice(0, 15))
        data.append('id_cliente', $("#inputIdCliente").val())
        data.append('id_tipo_documento', $("#inputTipoDocumento option:selected").val())
        data.append('file_ok', 1)
    }

    let new_button = '<button id="btnSalvarDocumento" class="btn btn-warning" type="button" disabled><span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Enviando</button>'
    $('#btnSalvarDocumento').remove()
    $('#div-enviar').append(new_button)

    let URL_TO_FETCH = url_host + 'clientes/documentos/'
    fetch(URL_TO_FETCH, {
        method: 'PUT',
        headers : {
          'Authorization': 'Bearer ' + access_token
        },
        body: data,
      })
      .then((res) => {
        if (res.status == 201 || res.status == 204) {
          location.reload()
        } else {
          console.log('ERROR')
        }
      })
      .catch((err) => {
        console.log(err)
      });
  });
})

function viewerDocumento(numero_documento) {
  window.open(`/system-att/clientes/documentos/viewer/${numero_documento}`)
}

function gerar_pdf(id_cliente) {
  window.open(`/system-att/dossie/${id_cliente}/gerar-pdf`)
}

function desabilitarCamposAtivo() {
  $('#inputNomeCliente').attr('disabled', true);
  $('#inputRG').attr('disabled', true);
  $('#inputCPF').attr('disabled', true);
  $('#inputCPF').css('background', '');
  $('#inputDataNascimento').attr('disabled', true);
  $('#inputSexo').attr('disabled', true);
  $('#inputTelefone').attr('disabled', true);
  $('#inputCEP').attr('disabled', true);
  $('#inputLogradouro').attr('disabled', true);
  $('#inputBairro').attr('disabled', true);
  $('#inputNumeroResidencia').attr('disabled', true);
  $('#inputComplemento').attr('disabled', true);
  $('#inputCidade').attr('disabled', true);
  $('#inputEstado').attr('disabled', true);
  $('#inputNacionalidade').attr('disabled', true);
  $('#inputNaturalidade').attr('disabled', true);
  $('#checkEmpregoFixo').attr('disabled', true);
  $('#checkAntecedentes').attr('disabled', true);
  $('#checkAceite').attr('disabled', true);
  $('#btnNovo').attr('disabled', false);
  $('#btnCadastrar').attr('disabled', true);
  $('#btnCancelar').attr('disabled', true);
}

var dados_dossie;
function popula_dossie(dados, extra_info) {
  dados_dossie = dados;
  let complete = {};
  let incomplete = {};
  let tipo;

  if (extra_info) {
    if (extra_info.nome_pai != '' & extra_info.nome_mae != ''){
      dados.flag_filiacao = true
    } else {
      dados.flag_filiacao = false
    }
    if (extra_info.profissao != '' && Object.keys(incomplete).length === 0) {
      dados.flag_cadastro_completo = true
    }
  }

  for (d in dados) {
    if (dados[d] === true) {
      if (d === 'flag_cadastro_completo') tipo = 'Cadastro Completo'
      else if (d === 'flag_copia_rg_cnh') tipo = 'Cópia RG ou CNH'
      else if (d === 'flag_comprovante_endereco') tipo = 'Comprovante Endereço'
      else if (d === 'flag_comprovante_ocupacao') tipo = 'Comprovante Ocupação'
      else if (d === 'flag_certidao_federal') tipo = 'Certidão Federal'
      else if (d === 'flag_certidao_estadual') tipo = 'Certidão Estadual'
      else if (d === 'flag_certidao_militar') tipo = 'Certidão Militar'
      else if (d === 'flag_certidao_eleitoral') tipo = 'Certidão Eleitoral'
      else if (d === 'flag_requerimento_comandante') tipo = 'Requerimento Comandante'
      else if (d === 'flag_declaracao_antecedentes') tipo = 'Declaração Antecedentes'
      else if (d === 'flag_declaracao_seguranca_acervo') tipo = 'Declaração Acervo'
      else if (d === 'flag_declaracao_endereco_acervo') tipo = 'Endereço Acervo'
      else if (d === 'flag_termo_ciencia_compromisso') tipo = 'Termo Compromisso'
      else if (d === 'flag_laudo_psicologico') tipo = 'Laudo Psicológico'
      else if (d === 'flag_laudo_tecnico') tipo = 'Laudo Tecnico'
      else if (d === 'flag_filiacao') tipo = 'Filiação'
      else if (d === 'flag_comprovante_pagamento_gru') tipo = 'Pagamento GRU'
      complete[tipo] = dados[d]
    } else if (dados[d] === false) {
      if (d === 'flag_cadastro_completo') tipo = 'Cadastro Completo'
      else if (d === 'flag_copia_rg_cnh') tipo = 'Cópia RG ou CNH'
      else if (d === 'flag_comprovante_endereco') tipo = 'Comprovante Endereço'
      else if (d === 'flag_comprovante_ocupacao') tipo = 'Comprovante Ocupação'
      else if (d === 'flag_certidao_federal') tipo = 'Certidão Federal'
      else if (d === 'flag_certidao_estadual') tipo = 'Certidão Estadual'
      else if (d === 'flag_certidao_militar') tipo = 'Certidão Militar'
      else if (d === 'flag_certidao_eleitoral') tipo = 'Certidão Eleitoral'
      else if (d === 'flag_requerimento_comandante') tipo = 'Requerimento Comandante'
      else if (d === 'flag_declaracao_antecedentes') tipo = 'Declaração Antecedentes'
      else if (d === 'flag_declaracao_seguranca_acervo') tipo = 'Declaração Acervo'
      else if (d === 'flag_declaracao_endereco_acervo') tipo = 'Endereço Acervo'
      else if (d === 'flag_termo_ciencia_compromisso') tipo = 'Termo Compromisso'
      else if (d === 'flag_laudo_psicologico') tipo = 'Laudo Psicológico'
      else if (d === 'flag_laudo_tecnico') tipo = 'Laudo Tecnico'
      else if (d === 'flag_filiacao') tipo = 'Filiação'
      else if (d === 'flag_comprovante_pagamento_gru') tipo = 'Pagamento GRU'
      incomplete[tipo] = dados[d]
    }
  }

  let tipo_dossie, satus_dossie, nova_linha;
  for (element in complete) {
    tipo_dossie = `<td>${element}</td>`
    satus_dossie = `<td>${complete[element] == true ? '<span class="badge badge-success">Concluído</span>' : `<span class="badge badge-danger">Pendente</span>`}</td>`
    nova_linha = `<tr>${tipo_dossie + satus_dossie}</tr>`
    $("#dossieTableInfo").append(nova_linha);
  }

  for (element in incomplete) {
    tipo_dossie = `<td>${element}</td>`
    satus_dossie = `<td>${complete[element] == true ? '<span class="badge badge-success">Concluído</span>' : `<span class="badge badge-danger">Pendente</span>`}</td>`
    nova_linha = `<tr>${tipo_dossie + satus_dossie}</tr>`
    $("#dossieTableInfo").append(nova_linha);
  }

  if (Object.keys(incomplete).length === 0) {
    $('#btnImprimir').attr('disabled', false);
    $('#btnCadastrarProtocolo').attr('disabled', false);
  }
}

function reload_cadastro_protocolo() {
  location.reload()
}

function popula_detalhes_protocolo(dados) {
  result_api = dados
  let dossie, protocolo, data_protocolo, subsecao, servico, status, nova_linha;
  for (var i = 0; i < dados.dossies[0].protocolos.length; i++) {
    dossie = `<td>${dados.dossies[0].protocolos[i].id_dossie}</td>`;
    protocolo = `<td>${dados.dossies[0].protocolos[i].num_protocolo}</td>`;
    data_protocolo = `<td>${dados.dossies[0].protocolos[i].dt_protocolo}</td>`;
    subsecao = `<td>${dados.dossies[0].protocolos[i].subsecao}</td>`;
    servico = `<td>${dados.dossies[0].protocolos[i].servico}</td>`;
    status = `<td>${dados.dossies[0].protocolos[i].status}</td>`;
    nova_linha = `<tr>${dossie + protocolo + data_protocolo + subsecao + servico + status}</tr>`
    console.log(nova_linha)
    $("#protocolo-table").append(nova_linha);
  }
}

function redirect_detalhes_protocolo(numero_cpf) {
  location.replace('/system-att/protocolos/' + numero_cpf)
}