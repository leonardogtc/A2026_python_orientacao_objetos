class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa.")
        self._idade = valor

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio.")
        self._nome = valor

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, email: str):
        super().__init__(nome, idade)
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor:
            raise ValueError("Email inválido.")
        self._email = valor

    def __str__(self):
        return f"{super().__str__()}, Email: {self.email}"


if __name__ == "__main__":
    pessoa = Pessoa("João", 30)
    print(pessoa)

    cliente = Cliente("Maria", 25, "maria@example.com")
    print(cliente)
