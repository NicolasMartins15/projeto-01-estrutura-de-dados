class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "categoria": self.categoria,
            "preco": self.preco,
            "quantidade": self.quantidade
        }

    @staticmethod
    def from_dict(dados):
        return Produto(
            dados["codigo"],
            dados["nome"],
            dados["categoria"],
            dados["preco"],
            dados["quantidade"]
        )