"""
Em Python, a relação entre decoradores e classes pode significar duas coisas diferentes:

    1. Classes sendo usadas como Decoradores (uma classe decorando uma função).
    2. Decoradores de Classes (uma função decorando uma classe inteira).

Vamos entender esses dois cenários detalhadamente.

Cenário 1: Usando uma Classe como Decorador
-------------------------------------------
Você pode criar uma classe para agir como decorador de funções. Para isso, a classe precisa implementar o método dunder __call__, permitindo que suas instâncias sejam chamadas como se fossem funções.

Como funciona:
--------------
    * O __init__ da classe recebe a função original que será decorada.
    * O __call__ executa o papel da função wrapper (empacotadora).

Vantagem principal:
-------------------
Classes são ótimas quando o decorador precisa manter um estado (guardar informações entre execuções).

Exemplo: Contador de chamadas de função
"""


class ContadorDeChamadas:
    def __init__(self, func):
        self.func = func
        self.contagem = 0   # Estado mantido entre as chamadas

    def __call__(self, *args, **kwargs):
        self.contagem += 1
        print(f"A função {self.func.__name__} foi chamada {self.contagem} vezes.")
        return self.func(*args, **kwargs)


@ContadorDeChamadas
def ola(nome):
    return f"Olá {nome}"


print(ola("Leonardo"))
print(ola("Ana"))
print(ola("Lúcia"))
print(ola("Oliver"))
