"""
Cenário 2: Decoradores de Classes (Decorando uma Classe Inteira)
Da mesma forma que decoramos funções, podemos passar uma classe inteira como argumento para uma função decoradora. O decorador pode modificar a classe, adicionar métodos ou atributos a ela e depois retorná-la.

O próprio @dataclass da biblioteca padrão do Python é um grande exemplo de decorador de classe.

Exemplo 1: Adicionando métodos ou atributos dinamicamente a uma classe
"""


def adicionar_repr(cls):
    """Decorador de classe que adiciona um __repr__ padrão à classe."""

    def meu_repr(self):
        # Pega o nome da classe e seus atributos em formato dict
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f"{class_name}({class_dict})"
        return class_repr

    # Injeta um novo método na classe recebida
    cls.__repr__ = meu_repr
    return cls  # Retorna a classe modificada

# Bizu:
# Leo, quando estiver estudando se ficar com dúvida remova o decorator!


@adicionar_repr
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa("Leonardo", "Gomes")
print(p1)
