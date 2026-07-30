"""
3. A Função super() e Especialização de Atributos
Quando a classe filha precisa de atributos próprios além dos atributos herdados, usamos a função super() para chamar o __init__ da classe pai e repassar os argumentos comuns.
"""


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def apresentar(self):
        print(
            f"Olá, sou {self.nome} {self.sobrenome} e tenho {self.idade} anos.")


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, idade, renda):
        # super() chama o __init__ da classe Pai (Pessoa)
        super().__init__(nome, sobrenome, idade)
        # Atributo exclusivo da classe Cliente
        self.renda = renda


class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, idade, matricula):
        # super() chama o __init__ da classe Pai (Pessoa)
        super().__init__(nome, sobrenome, idade)
        # Atributo exclusivo da classe Aluno:
        self.matricula = matricula


c1 = Cliente("Ana", "Manuela", 30, 5000.0)
a1 = Aluno("Alice", "Spinola", 12, "07A012026")

c1.apresentar()  # Output: Olá, sou Ana e tenho 30 anos.
print(f"Renda do Cliente: R$ {c1.renda}")

a1.apresentar()  # Output: Olá, sou Pedro e tenho 20 anos.
print(f"Matrícula do Aluno: {a1.matricula}")

help(Cliente)
