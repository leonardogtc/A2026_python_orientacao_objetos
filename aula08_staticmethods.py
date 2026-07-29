"""
Métodos Estáticos (@staticmethods)

Em Python, um método estático (@staticmethod) é uma função que reside dentro de uma classe, mas não possui acesso nem ao estado da instância (self) nem ao estado da classe (cls).

Ele funciona exatamente como uma função comum fora da classe, porém é colocado dentro da classe para fins de organização e coesão de código.
--------------
1. Principais Características

    - Decorador: É definido com a anotação @staticmethod.

    - Sem Parâmetro Implícito: Não recebe self nem cls automaticamente como primeiro argumento.

    - Independência: Não pode alterar atributos da instância nem da classe (a menos que a classe/instância seja passada explicitamente como argumento).

    - Chamada: Pode ser chamado diretamente pela classe (MinhaClasse.metodo()) ou por uma instância dela (objeto.metodo()).

2. Comparativo Rápido dos Métodos em Python
Tipo de Método	    Decorador	    1º Parâmetro	Acesso a...
Instância	        (nenhum)	    self	        Atributos e métodos do objeto/instância
Classe	            @classmethod	cls	            Atributos e métodos da própria Classe
Estático	        @staticmethod	(nenhum)	    Apenas aos argumentos passados para ele
"""


class Pessoa:
    especie = "homo Sapiens"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # 1. Método de instância (opera nos dados do objeto)
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    # 2. Método de classe (opera nos dados da classe / construtor alternativo)
    @classmethod
    def criar_com_ano_nascimento(cls, nome, ano_nascimento):
        idade = 2026 - ano_nascimento
        return cls(nome, idade)

    # 3. Método Estático (função utilitária isolada)
    @staticmethod
    def e_maior_de_idade(idade):
        """ Não usa 'self' ou 'cls'. É uma lógica pura relacionada a pessoa."""
        return idade >= 18


# ===== Usando o método estático =====
# Chamada direta pela classe (sem precisar instanciar):
print(Pessoa.e_maior_de_idade(20))
print(Pessoa.e_maior_de_idade(10))

# Também pode ser chamado por uma instância diferente:
p1 = Pessoa("Ana", 21)
print(p1.e_maior_de_idade(p1.idade))

"""
Quando usar @staticmethod?
==========================
Use métodos estáticos quando você tiver uma função utilitária/auxiliar que tem forte relação conceitual com a classe, mas que não precisa ler ou alterar nada do objeto ou da classe.

Exemplos comuns de uso:

1. Validações: Validar CPF, e-mail, formato de senha ou data antes de criar um objeto.
2. Conversões/Formatações: Converter unidades de medida, formatar strings ou moedas.
3. Cálculos puros: Algoritmos matemáticos independentes que auxiliam as operações da classe.
"""
