"""
O modo pythônico de lidar com Getters e Setters baseia-se na filosofia do Python de simplicidade, sintaxe limpa e na premissa conhecida na comunidade como "We are all consenting adults here" (Somos todos adultos maduros aqui).

1. O Modo NÃO-Pythônico (Estilo Java / C#)
Em linguagens como Java ou C++, ensina-se a criar atributos privados por padrão e escrever métodos get_...() e set_...() para absolutamente tudo, mesmo sem validação:

# ❌ NÃO-PYTHÔNICO (Evite isso em Python!)
class Caneta:
    def __init__(self, cor):
        self._cor = cor

    def get_cor(self):
        return self._cor

    def set_cor(self, cor):
        self._cor = cor

c = Caneta("Azul")
print(c.get_cor())  # Verborrágico!
c.set_cor("Preta")

Por que isso não é pythônico?

    🔹Polui a classe com métodos desnecessários se você só está guardando e lendo a variável.
    🔹Deixa a sintaxe de uso engessada e verborrágica (c.get_cor() em vez de c.cor).

2. O Modo Pythônico (Regra de Ouro)
O modo pythônico segue duas regras fundamentais:

🔹 Regra 1: Se não há validação/lógica extra, use atributos públicos diretos
Em Python, não criamos getters e setters "preventivos". Se o atributo só armazena um valor, use-o diretamente:

# ✅ PYTHÔNICO (Simples e direto)
class Caneta:
    def __init__(self, cor):
        self.cor = cor  # Atributo público simples!

c = Caneta("Azul")
print(c.cor)    # Leitura direta
c.cor = "Preta" # Escrita direta

🔹 Regra 2: Precisa de validação ou cálculo? Use @property (Princípio do Acesso Uniforme)
Se no futuro o requisito mudar e você precisar validar o valor (ou calcular algo), você usa o decorador @property.

O segredo aqui é que a sintaxe para quem usa a classe NÃO MUDA (c.cor continua sendo c.cor e c.cor = "Preta" continua sendo atribuição simples):

# ✅ PYTHÔNICO COM VALIDAÇÃO (Usando @property)
class Caneta:
    def __init__(self, cor):
        # Ao atribuir self.cor aqui, o @cor.setter já é acionado na criação!
        self.cor = cor

    @property
    def cor(self):
        # Getter: formata ou retorna a variável interna _cor
        return self._cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        # Setter: aplica regras de proteção/validação
        if not nova_cor or not isinstance(nova_cor, str):
            raise ValueError("A cor deve ser uma string válida!")
        self._cor = nova_cor


# Para quem usa o objeto, a interface é exatamente a mesma (sem get_cor / set_cor):
c = Caneta("Azul")
print(c.cor)      # Retorna 'AZUL' (passou pelo @property getter)

c.cor = "Preta"   # Passou pelo @cor.setter
print(c.cor)      # Retorna 'PRETA'

# c.cor = ""      # ValueError: A cor deve ser uma string válida!

"""

# ✅ PYTHÔNICO COM VALIDAÇÃO (Usando @property)


class Caneta:
    def __init__(self, cor):
        # Ao atribuir self.cor aqui, o @cor.setter já é acionado na criação!
        self.cor = cor

    @property
    def cor(self):
        # Getter: formata ou retorna a variável interna _cor
        return self._cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        # Setter: aplica regras de proteção/validação
        if not nova_cor or not isinstance(nova_cor, str):
            raise ValueError("A cor deve ser uma String válida!")
        self._cor = nova_cor


# Para quem usa o objeto, a interface é exatamente a mesma (sem get_cor / set_cor):
c = Caneta("Azul")
print(c.cor)

c.cor = "Preta"
print(c.cor)
