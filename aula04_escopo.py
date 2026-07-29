"""
Escopo da classe e de método da classe
---------------------------------------
O escopo em Orientação a Objetos no Python determina onde variáveis e atributos podem ser acessados dentro de uma classe e de seus métodos.

Em Python, existem três níveis de escopo principais dentro de uma classe:

1. Escopo de Método (Variáveis Locais)
Variáveis criadas dentro de um método pertencem apenas àquele método. Elas deixam de existir assim que a execução do método termina e não podem ser acessadas por outros métodos.

2. Escopo de Instância (Atributos self)
Para reutilizar valores entre diferentes métodos de um mesmo objeto, atribuímos esses valores a self. O self conecta os dados ao objeto específico (instância).

3. Escopo da Classe (Atributos de Classe)
Variáveis definidas diretamente no corpo da classe (fora de qualquer método) pertencem ao escopo da própria classe. Elas são compartilhadas por todas as instâncias dessa classe.
"""


class Calculadora:
    # 1. Atributo de CLASSE (disponível em toda a classe e instâncias)
    precisao = 2

    def __init__(self, valor_inicial):
        # 2. Atributo de INSTÂNCIA (disponível para qualquer método via self)
        self.resultado = valor_inicial

    def soma(self, numero):
        # 3. Variável LOCAL do método (existe apenas durante a execução desse método)
        fator = 1
        self.resultado = numero * fator

    def exibir_resultado(self):
        # Tentar acessar 'fator' aqui geraria um NameError
        print(f"Resultado formatado: {round(self.resultado, self.precisao)}")
