"""
Em Python, decoradores (decorators) são uma forma limpa e elegante de modificar ou estender o comportamento de uma função ou método sem alterar diretamente o seu código-fonte.

1. Conceito Base: Funções são Objetos de Primeira Classe
    Para entender decoradores, é preciso lembrar que em Python funções podem:

    1.1. Ser atribuídas a variáveis.
    1.2. Ser passadas como argumentos para outras funções.
    1.3. Ser criadas dentro de outras funções (funções aninhadas) e retornadas por elas.

2. O que é uma Função Decoradora?
    Uma função decoradora é simplesmente uma função que:

    - Recebe outra função como parâmetro.
    - Define uma função interna (wrapper ou empacotadora) que adiciona funcionalidades antes ou depois da chamada original.
    - Retorna a função interna.

Exemplo sem o açúcar sintático @:
"""


def meu_decorador(funcao_original):
    def wrapper():
        print("-> Ação executada ANTES da função original")
        funcao_original
        print("-> Ação executada DEPOIS da função original.")
    return wrapper


"""
3. A Sintaxe @ (Syntactic Sugar)
O Python possui uma sintaxe facilitada usando o símbolo @. 
Colocar @meu_decorador acima de uma função é exatamente o
mesmo que fazer minha_funcao = meu_decorador(minha_funcao).
"""


@meu_decorador
def minha_funcao():
    print("Executando a minha função principal!")


# Aplicando o decorador manualmente:
# minha_funcao = meu_decorador(minha_funcao)
minha_funcao()
