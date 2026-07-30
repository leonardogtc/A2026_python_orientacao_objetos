"""
Na Programação Orientada a Objetos, Associação, Agregação e Composição são três formas de relacionar classes onde um objeto "tem" outro objeto (relação "tem-um" / has-a).

A principal diferença entre elas está no nível de acoplamento e na dependência do ciclo de vida entre os objetos.

📊 Resumo Comparativo Rápido:
-------------------------------------------------------------------------------------------
Relação	    |   Acoplamento |   Ciclo de Vida dos Objetos   |   Exemplo
-------------------------------------------------------------------------------------------
Associação  |   Fraco       |   Totalmente independentes    =>  Escritor e Caneta
            |               |   (Existem separadamente)
-------------------------------------------------------------------------------------------
Agregação   |   Médio       |   O "TODO" agrupa "PARTES",   =>  CarrinhoDeCompras e Produto
            |               |   mas as "PARTES" existem
            |               |   sem o "TODO".
-------------------------------------------------------------------------------------------
Composição  |   Forte       |   As "PARTES" pentencem ao    => Cliente e Endereco
            |               |   "TODO". Se o "TODO" morre,
            |               |   as "PARTES" morrem.
-------------------------------------------------------------------------------------------

1. Associação (Relação Fraca)
Na Associação, dois objetos estão ligados e podem interagir entre si, mas nenhum é dono do outro. Se apagar um objeto, o outro continua existindo normalmente.

Exemplo: Escritor e Caneta
Um escritor pode usar uma caneta para escrever, mas o escritor existe sem a caneta e a caneta existe sem o escritor.
"""


class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None  # Associação: inicialmente não tem ferramenta


class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print(f"Caneta {self.marca} está escrevendo...")


# Criando um objeto de forma independente
escritor = Escritor("Machado de Assis")
caneta = Caneta("Bic")

# Associando os objetos
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

# Se deletarmos o escritos a caneta continua existindo
del escritor
print(caneta.marca)
