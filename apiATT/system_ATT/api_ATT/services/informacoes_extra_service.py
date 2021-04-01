from ..models import InformacoesExtraCliente, Cliente


def get_extra_info_by_id(id_cliente):
    try:
        return InformacoesExtraCliente.objects.get(id_cliente=id_cliente)
    except Exception:
        return None


def register_extra_info(info):
    cliente = Cliente.objects.get(id_cliente=info.id_cliente)
    return InformacoesExtraCliente.objects.create(
        id_cliente=cliente,
        nome_pai=info.nome_pai,
        nome_mae=info.nome_mae,
        profissao=info.profissao
    )


def update_extra_info(info_db, new_info):
    info_db.nome_pai = new_info.nome_pai
    info_db.nome_mae = new_info.nome_mae
    info_db.profissao = new_info.profissao
    info_db.save(force_update=True)
