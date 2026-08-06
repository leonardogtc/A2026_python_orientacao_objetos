classDiagram
    class Pessoa {
        <<Abstract>>
        # string _nome
        # int _idade
        + nome() string
        + idade() int
    }

    class Cliente {
        - Conta _conta
        + conta() Conta
        + conta(Conta conta) void
    }

    class Conta {
        <<Abstract>>
        # int _agencia
        # int _numero
        # float _saldo
        + agencia() int
        + numero() int
        + saldo() float
        + depositar(float valor) bool
        + sacar(float valor)* bool
    }

    class ContaCorrente {
        - float _limite
        + limite() float
        + sacar(float valor) bool
    }

    class ContaPoupanca {
        + sacar(float valor) bool
    }

    class Banco {
        - list~Cliente~ _clientes
        - list~int~ _agencias
        - list~Conta~ _contas
        + autenticar(Cliente cliente, Conta conta) bool
        + sacar(Cliente cliente, Conta conta, float valor) bool
    }

    Pessoa <|-- Cliente : Herança
    Cliente o-- Conta : Agregação
    Conta <|-- ContaCorrente : Herança
    Conta <|-- ContaPoupanca : Herança
    Banco o-- Cliente : Agregação
    Banco o-- Conta : Agregação