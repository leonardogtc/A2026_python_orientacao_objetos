"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod


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


class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero: int, saldo: float = 0.0,
                 limite: float = 0.0):
        super().__init__(agencia, numero, saldo)
        self._limite = limite

    def sacar(self, valor: float) -> bool:
        saldo_disponivel = self._saldo + self._limite
        if valor > 0 and valor <= saldo_disponivel:
            self._saldo -= valor
            return True
        return False


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> bool:
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            return True
        return False


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: Conta):
        super().__init__(nome, idade)
        self.conta = conta


class Banco:
    def __init__(self):
        self.agencias = []
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        self.contas.append(cliente.conta)

    def autenticar(self, cliente: Cliente, conta: Conta) -> bool:
        # Checa se a agência pertence ao banco
        if conta.agencia not in self.agencias:
            return False
        # Checa se o cliente pertence ao banco
        if cliente not in self.clientes:
            return False
        # Checa se a conta pertence ao banco
        if conta not in self.contas:
            return False
        # Checa se a conta fornecida é realmente do cliente
        if cliente.conta is not conta:
            return False

        return True

    def sacar(self, cliente: Cliente, conta: Conta, valor: float) -> bool:
        if self.autenticar(cliente, conta):
            return conta.sacar(valor)
        print("Autenticação falhou. Saque não permitido.")
        return False
