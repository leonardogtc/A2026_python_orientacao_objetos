# Polimorfismo: Exemplo mais didático.

from abc import ABC, abstractmethod


class Animal:

    @abstractmethod
    def falar(self) -> None:
        """ Método genérico que deve ser implementado pelas filhas. """
        pass


class Cachorro(Animal):
    def falar(self) -> str:
        return "Au au"


class Gato(Animal):
    def falar(self) -> str:
        return "Miau Miau"


class Pato(Animal):
    def falar(self) -> str:
        return "Quá quá"


animais = [Cachorro(), Gato(), Pato()]

for animal in animais:
    print(animal.falar())
