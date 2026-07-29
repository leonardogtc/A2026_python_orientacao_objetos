"""
Mantendo estados dentro da classe
---------------------------------
Mantendo o estado dentro da classe (ou estado da instância) é um dos pilares da Orientação a Objetos.

O que é o "Estado" de um objeto?
O estado nada mais é do que a representação dos dados e informações armazenados nos atributos (self.atributo) de um objeto em um determinado momento. (Velocidade Instantânea na Física)

Diferente de funções comuns (que executam um bloco de código e "esquecem" tudo quando terminam), um objeto lembra do seu histórico. Ele retém o valor dos seus atributos entre chamadas de métodos.

Exemplo Prático: Uma Câmera
---------------------------
Imagine uma classe Camera que pode estar filmando ou não. O valor da variável self.filmando representa o estado atual da câmera.
"""


class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        # Define o estado inicial (False = não está filmando)
        self.filmando = filmando

    def filmar(self):
        """ Método para iniciar a filmangem da câmera! """
        if self.filmando:
            print(f"{self.nome} já está filmando!")
            return

        print(f"{self.nome} começou a filmar...")
        self.filmando = True    # ALTERA o estado do objeto para True

    def parar_filmar(self):
        if not self.filmando:
            print(f"{self.nome} NÃO está filmando no momento...")
            return

        print(f"{self.nome} parou de filmar.")
        self.filmando = False   # ALTERA o estado do objeto para False

    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar enquanto está filmando!")
            return

        print(f"{self.nome} tirou uma fotografia! 📸")


# ================================================
# Instanciando e Testando a manutenção do objeto
# ================================================
c1 = Camera('Canon')
c2 = Camera('Sony')

# 1. c1 começa com o estado self.filmando = False
c1.fotografar()     # Canon tirou uma foto! 📸

# 2. Alterando o estado de c1
c1.filmar()         # Canon começou a filmar...
c1.filmar()         # Canon JÁ está filmando... (consultou o estado mantido)

# 3. Tentar fotografar com o estado alterado
c1.fotografar()     # Canon não pode fotografar enquanto está filmando!

# 4. O estado de c2 é INDEPENDENTE do estado de c1!
c2.fotografar()     # Sony tirou uma foto! 📸 (c2 continua com self.filmando = False)

# 5. Parando a filmagem de c1
c1.parar_filmar()   # Canon parou de filmar.
c1.fotografar()     # Canon tirou uma foto! 📸 (estado voltou para False)


"""
Por que isso é importante?
--------------------------
1. Persistência de Dados: Você não precisa passar o status da câmera como parâmetro toda vez que chamar um método. O próprio objeto guarda essa informação.

2. Independência de Instâncias: Duas instâncias (c1 e c2) possuem estados totalmente independentes. Mudar o estado de c1 não afeta c2.

3. Evita Variáveis Globais: Sem classes, você teria que controlar o estado com variáveis globais (o que torna o código difícil de manter e propenso a bugs).
"""