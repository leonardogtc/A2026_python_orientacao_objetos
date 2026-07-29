"""
MÉTODOS DE CLASSE
=================
Os Métodos de Classe (class methods) são métodos que pertencem à classe em si e não a uma instância (objeto) específica.

1. O que caracteriza um Método de Classe?

1.1. É decorado com o @classmethod.
1.2. Recebe cls como seu primeiro parâmetro (em vez de self).

    1.2.1. self faz referência à instância (objeto).
    1.2.2. cls faz referência à própria Classe (class).

1.3. Pode ser chamado diretamente pela classe sem precisar criar um objeto antes (ex: Pessoa.metodo_de_classe()).

2. Para que servem? (Principais Casos de Uso)
    2.1. O uso mais comum de métodos de classe é a criação de Factory Methods (Métodos Construtores Alternativos). Eles oferecem maneiras diferentes de criar e instanciar um objeto da classe além do __init__ padrão (Sobrecarga de construtor).

    2.2. Acessar ou Modificar o Estado da Classe
    Se você precisa de uma variável compartilhada por todas as instâncias da classe, o método de classe é a forma limpa de manipulá-la.
"""

import collections
from datetime import date


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Construtor alternativo a partir do ano de nascimento
    @classmethod
    def criar_por_ano_nascimento(cls, nome, ano_nascimento):
        idade = date.today().year - ano_nascimento
        return cls(nome, idade)


# Forma tradicional
p1 = Pessoa("Ana", 28)

# Usando o construtor alternativo
p2 = Pessoa.criar_por_ano_nascimento("Leonardo", 1971)
print(f"{p2.nome} tem {p2.idade} anos")

# Acessar ou modificar o estado da classe


class Funcionario:
    aumento_percentual = 1.05   # Atributo da classe (5% de aumento padrão)

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_aumento(self):
        self.salario *= self.aumento_percentual

    @classmethod
    def definir_novo_aumento(cls, novo_percentual):
        cls.aumento_percentual = novo_percentual


f1 = Funcionario('João', 3000)
f2 = Funcionario('Maria', 5000)

# Alterar o aumento para todos os funcionarios através da classe:
Funcionario.definir_novo_aumento(1.10)

f1.aplicar_aumento()
f2.aplicar_aumento()

print(f1.salario)
print(f2.salario)
