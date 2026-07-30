"""
4. Sobrescrita de Métodos (Method Overriding)
A subclasse pode redefinir (sobrescrever) um método herdado para alterar ou personalizar seu comportamento:
"""


class Animal:
    def fazer_som(self):
        print("Som genérico de animal...")


class Cachorro(Animal):
    # Sobrescrevendo o método fazer_som da classe pai
    def fazer_som(self):
        print("Au Au!")


class Gato(Animal):
    # Sobrescrevendo o método fazer_som da classe pai
    def fazer_som(self):
        print("Miau!")


# Instanciando
c = Cachorro()
g = Gato()

# Usando métodos sobrescritos
c.fazer_som()  # Output: Au Au!
g.fazer_som()  # Output: Miau!