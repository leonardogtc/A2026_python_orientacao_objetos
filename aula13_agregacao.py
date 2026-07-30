"""
2. Agregação (Relação Todo-Parte Independente)
Na Agregação, um objeto maior (o "Todo") agrupa ou contém outros objetos (as "Partes"). No entanto, as partes são criadas fora do todo e podem existir de forma independente.

Exemplo: CarrinhoDeCompras e Produto
O carrinho agrega vários produtos. Se destruirmos o carrinho, os produtos ainda existem no estoque/sistema.
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  # Lista que receberá instâncias de Produto

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def total(self):
        return sum(p.preco for p in self.produtos)


# Criamos os produtos INDEPENDENTEMENTE do carrinho
p1 = Produto("Camiseta", 50.0)
p2 = Produto("Calça", 120.0)

# Agregamos os produtos no carrinho
carrinho = CarrinhoDeCompras()
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)

print(f"Total da compra: R$ {carrinho.total()}")  # Output: Total da compra: R$170.0
# Se apagarmos o carrinho, os produtos ainda EXISTEM na memória!
del carrinho
print(p1.nome, p1.preco)  # Output: Camiseta 50.0