"""
5. Herança Múltipla (Breve Introdução)
Diferente de linguagens como Java ou C#, Python suporta Herança Múltipla, ou seja, uma classe pode herdar de duas ou mais classes simultaneamente:
"""


class Logavel:
    def log(self, mensagem):
        print(f"[LOG]: {mensagem}")


class Conexao:
    def conectar(self):
        print("Conectado ao servidor.")

# Herda de duas superclasses ao mesmo tempo:


class BancoDeDados(Conexao, Logavel):
    pass


bd = BancoDeDados()
bd.conectar()      # Método herdado de Conexao
bd.log("Sucesso")  # Método herdado de Logavel


"""
Atenção (MRO - Method Resolution Order): Quando uma classe herda de múltiplas superclasses, o Python busca os métodos da esquerda para a direita na ordem de herança. Você pode verificar essa ordem usando NomeDaClasse.mro().

🎯 Resumo
Conceito                    Descrição
Superclasse (Pai)	        =>  Classe base que contém o código generalizado/comum.
Subclasse (Filha)	        =>  Classe que herda da superclasse (class Filha(Pai):).
super()	                    =>  Função para executar métodos da classe pai dentro da filha (muito usada no __init__).
Sobrescrita (Overriding)    =>  Redefinir um método herdado para adaptar o comportamento na subclasse.
"""
