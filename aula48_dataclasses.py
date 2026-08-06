# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

# Importa a função dataclass do módulo dataclasses para usar na criação da
# classe.
from dataclasses import dataclass


# Define a classe Pessoa e usa o decorador @dataclass para gerar métodos
# automaticamente.
@dataclass
class Pessoa:
    # Define o atributo nome como uma string.
    nome: str
    # Define o atributo idade como um inteiro.
    idade: int

    # Método especial chamado automaticamente após a criação do objeto.
    def __post_init__(self):
        # Verifica se a idade informada é negativa e gera um erro caso seja.
        if self.idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        # Verifica se o nome está vazio e gera um erro caso esteja.
        if not self.nome:
            raise ValueError("Nome não pode ser vazio.")

    # Método especial que define como o objeto será mostrado como texto.
    def __str__(self):
        # Retorna uma mensagem legível com o nome e a idade da pessoa.
        return f"Nome: {self.nome}, Idade: {self.idade}"


# Cria uma instância da classe Pessoa com nome e idade.
p1 = Pessoa("João", 30)
# Exibe o objeto na tela usando o método __str__.
print(p1)
