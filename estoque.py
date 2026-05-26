from utils import registrar_log


class Estoque:
    def __init__(self, produtos=None):
        self.produtos = produtos if produtos else []
        self.ordenar_produtos()

    def ordenar_produtos(self):
        self.produtos.sort(key=lambda produto: produto.codigo)

    def cadastrar_produto(self, produto):
        if self.buscar_por_codigo(produto.codigo):
            print("Código já existente.")
            return

        self.produtos.append(produto)
        self.ordenar_produtos()

        registrar_log(f"Produto cadastrado: {produto.nome}")

    def editar_produto(self, codigo, nome, categoria, preco, quantidade):
        produto = self.buscar_por_codigo(codigo)

        if produto:
            produto.nome = nome
            produto.categoria = categoria
            produto.preco = preco
            produto.quantidade = quantidade

            registrar_log(f"Produto editado: {produto.nome}")

            print("Produto atualizado.")
        else:
            print("Produto não encontrado.")

    def remover_produto(self, codigo):
        produto = self.buscar_por_codigo(codigo)

        if produto:
            self.produtos.remove(produto)

            registrar_log(f"Produto removido: {produto.nome}")

            print("Produto removido.")
        else:
            print("Produto não encontrado.")

    def buscar_por_codigo(self, codigo):
        inicio = 0
        fim = len(self.produtos) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2

            if self.produtos[meio].codigo == codigo:
                return self.produtos[meio]

            if self.produtos[meio].codigo < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1

        return None

    def buscar_por_nome(self, nome):
        resultado = []

        for produto in self.produtos:
            if nome.lower() in produto.nome.lower():
                resultado.append(produto)

        return resultado

    def registrar_venda(self, codigo, quantidade):
        produto = self.buscar_por_codigo(codigo)

        if not produto:
            print("Produto não encontrado.")
            return

        if quantidade > produto.quantidade:
            print("Estoque insuficiente.")
            return

        produto.quantidade -= quantidade

        registrar_log(
            f"Venda realizada: {produto.nome} | Quantidade: {quantidade}"
        )

        print("Venda realizada.")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return

        for produto in self.produtos:
            self.exibir_produto(produto)

    def listar_por_categoria(self, categoria):
        encontrados = False

        for produto in self.produtos:
            if produto.categoria.lower() == categoria.lower():
                self.exibir_produto(produto)
                encontrados = True

        if not encontrados:
            print("Nenhum produto encontrado.")

    def relatorio_estoque_baixo(self, limite):
        encontrados = False

        for produto in self.produtos:
            if produto.quantidade < limite:
                self.exibir_produto(produto)
                encontrados = True

        if not encontrados:
            print("Nenhum produto com estoque baixo.")

    @staticmethod
    def exibir_produto(produto):
        print(f"Código: {produto.codigo}")
        print(f"Nome: {produto.nome}")
        print(f"Categoria: {produto.categoria}")
        print(f"Preço: R$ {produto.preco:.2f}")
        print(f"Quantidade: {produto.quantidade}")
        print("-" * 40)