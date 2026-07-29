# Para criar uma classe uso a palavra reservada class
# Para chamar uma classe uso parenteses
# Para instanciar uma classe uso a palavra reservada instanciar
# Hard Coder - É algo que é escrito diretamente no código.

class Pessoa:
    # O __init__ é um método especial chamado de construtor
    # Ele é chamado automaticamente quando uma instância da classe é criada
    # O self é uma referência à instância da classe
    # Os outros parâmetros são os dados que serão passados para a instância
    # O método __init__ sempre retorna None, então não é necessário usar a
    # palavra reservada return
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


# Instanciar a classe
p1 = Pessoa("Leonardo", "Tavares")
p2 = Pessoa("Oliver", "Tavares")

p1_tipo = type(p1)
p2_tipo = type(p2)

print(p1_tipo)
print(p2_tipo)
print(p1.nome)
print(p2.nome)
