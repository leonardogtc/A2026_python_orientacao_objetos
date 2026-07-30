"""
Classes
-------

    1. Crie uma classe Carro (Nome)
    2. Crie uma classe Motor (Nome)
    3. Crie uma classe Fabricante (Nome)
    4. Faça uma ligação entre Carro e Motor - Use "Composition" ou "Aggregation" para compor o carro.
    5. Crie uma instância de Carro e adicione uma instância da classe Motor
    6. Faça uma ligação entre Carro e Fabricante - Use "Composition" ou "Aggregation" para compor o carro.
        
"""


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def carro(self):
        return self.nome

    @carro.setter
    def carro(self, valor):
        self.nome = valor

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome

    @property
    def motor(self):
        return self.nome

    @motor.setter
    def motor(self, valor):
        self.nome = valor


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

    @property
    def fabricante(self):
        return self.nome

    @fabricante.setter
    def fabricante(self, valor):
        self.nome = valor


# Instanciando
carro1 = Carro("Fusca")
motor1 = Motor("1.6")
fabricante1 = Fabricante("Volkswagen")

carro1.motor = motor1
carro1.fabricante = fabricante1

print(carro1.carro)
print(carro1.motor.motor)
print(carro1.fabricante.fabricante)
