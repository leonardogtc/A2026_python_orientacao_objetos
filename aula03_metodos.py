# Métodos em instâncias da classe
# O nome self é uma convenção (poderia ser "qualquer_coisa")
# Hard Coder - É algo que é escrito diretamente no código.

class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def ligar(self):
        print(f'O carro {self.marca} {self.modelo} está ligado')

    def desligar(self):
        print(f'O carro {self.marca} {self.modelo} está desligado')

    def acelerar(self, velocidade):
        self.velocidade += velocidade
        print(f'O carro {self.marca} {self.modelo} está acelerando')

    def frear(self, velocidade):
        self.velocidade -= velocidade
        print(f'O carro {self.marca} {self.modelo} está freando')


# Instanciar a classe
c1 = Carro("Fiat", "Uno", 2022, 120)
c1.ligar()
c1.acelerar(100)
c1.frear(50)
c1.desligar()

c2 = Carro("Ford", "Fusion", 2024, 180)
c2.ligar()
c2.acelerar(150)
c2.frear(100)
c2.desligar()
