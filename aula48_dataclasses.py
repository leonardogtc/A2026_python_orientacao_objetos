# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int

    def __post_init__(self):
        if self.idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        if not self.nome:
            raise ValueError("Nome não pode ser vazio.")

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


p1 = Pessoa("João", 30)
print(p1)
