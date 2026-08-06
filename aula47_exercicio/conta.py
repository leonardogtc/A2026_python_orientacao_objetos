from abc import ABC, abstractmethod


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


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade


class Conta(ABC):
    def __init__(self, agencia: int, numero: int, saldo: float = 0.0):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            return True
        return False

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')


@adicionar_repr
class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero: int, saldo: float = 0.0,
                 limite: float = 0.0):
        super().__init__(agencia, numero, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor: float) -> bool:
        saldo_disponivel = self._saldo + self._limite
        if valor > 0 and valor <= saldo_disponivel:
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return True

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return False


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> bool:
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return True
        return False


class Cliente(Pessoa):
    ...


cc1 = ContaCorrente(14, 148036, 100)
print(cc1)
cc1.sacar(80.00)
print(cc1)
print(10 * '-')
cc2 = ContaCorrente(14, 142836, 1000, 5000)
print(cc2)
print(10 * '-')
