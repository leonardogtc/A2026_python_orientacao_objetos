import json


class JSONMixin:
    """Adiciona a capacidade de converter qualquer objeto em JSON."""

    def para_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)


class Carro(JSONMixin):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


meu_carro = Carro("Volkswagen", "Fusca", 1972)
# Usa o método para_json() fornecido pelo Mixin
print(meu_carro.para_json())
