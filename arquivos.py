import json
from produto import Produto

ARQUIVO_DADOS = "dados.json"


def salvar_produtos(produtos):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(
            [produto.to_dict() for produto in produtos],
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def carregar_produtos():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return [Produto.from_dict(item) for item in dados]
    except FileNotFoundError:
        return []