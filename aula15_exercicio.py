"""
Classes
-------

    1. Crie uma classe Carro (Nome)
    2. Crie uma classe Motor (Nome)
    3. Crie uma classe Fabricante (Nome)
    4. Faça uma ligação entre Carro e Motor - Use "Composition" ou "Aggregation" para compor o carro.
        def inserir_motor(self, nome):
            self._motor = Motor(nome)
        def listar_motor(self):
            return self._motor
    5. Crie uma instância de Carro e adicione uma instância da classe Motor

    6. Faça uma ligação entre Carro e Fabricante - Use "Composition" ou "Aggregation" para compor o carro.
        def inserir_fabricante(self, nome):
            self._fabricante = Fabricante(nome)
        def listar_fabricante(self):
            return self._fabricante
"""


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
