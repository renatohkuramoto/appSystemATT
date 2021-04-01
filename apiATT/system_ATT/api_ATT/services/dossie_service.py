from ..models import Cliente, Dossie


def getDossieByClienteId(id_cliente):
    try:
        return Dossie.objects.get(id_cliente=id_cliente)
    except Exception:
        return None


def getAllDossies():
    return Dossie.objects.all()


def getDossieById(id_dossie):
    try:
        return Dossie.objects.get(id_dossie=id_dossie)
    except Exception:
        return None


def createDossie(novo_dossie):
    return Dossie.objects.create(
        id_cliente=novo_dossie.id_cliente,
        flag_cadastro_completo=novo_dossie.flag_cadastro_completo,
        flag_copia_rg_cnh=novo_dossie.flag_copia_rg_cnh,
        flag_comprovante_endereco=novo_dossie.flag_comprovante_endereco,
        flag_comprovante_ocupacao=novo_dossie.flag_comprovante_ocupacao,
        flag_certidao_federal=novo_dossie.flag_certidao_federal,
        flag_certidao_estadual=novo_dossie.flag_certidao_estadual,
        flag_certidao_militar=novo_dossie.flag_certidao_militar,
        flag_certidao_eleitoral=novo_dossie.flag_certidao_eleitoral,
        flag_requerimento_comandante=novo_dossie.flag_requerimento_comandante,
        flag_declaracao_antecedentes=novo_dossie.flag_declaracao_antecedentes,
        flag_declaracao_seguranca_acervo=novo_dossie.flag_declaracao_seguranca_acervo,
        flag_declaracao_endereco_acervo=novo_dossie.flag_declaracao_endereco_acervo,
        flag_termo_ciencia_compromisso=novo_dossie.flag_termo_ciencia_compromisso,
        flag_laudo_psicologico=novo_dossie.flag_laudo_psicologico,
        flag_laudo_tecnico=novo_dossie.flag_laudo_tecnico,
        flag_filiacao=novo_dossie.flag_filiacao,
        flag_comprovante_pagamento_gru=novo_dossie.flag_comprovante_pagamento_gru
    )

def updateDossie(dossie_bd, update_fields):
    dossie_bd.update(**update_fields)
    dossie_bd.save(force_update=True)


def deleteDossie(dossie):
    dossie.delete()
