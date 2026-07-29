"""
Atributos de Classe
-------------------
Os Atributos de Classe são variáveis definidas diretamente dentro do bloco da classe (fora de qualquer método).

A principal característica deles é que eles pertencem à classe em si e são compartilhados por TODAS as instâncias criadas a partir dessa classe.

1. Diferença entre Atributo de Classe vs Atributo de Instância

- Atributo de Instância (self.atributo): Pertence a cada objeto individualmente. Mudanças em um objeto não afetam os outros. (Ex: self.nome, self.idade).

- Atributo de Classe (AtributoNoCorpoDaClasse): É compartilhado por todos os objetos. Se alterado na classe, afeta todas as instâncias. (Ex: ano_atual = 2026).
"""


from importlib.resources import _common


class Pessoa:
    # ATRIBUTO DE CLASSE: compartilhado por todas as pessoas
    ano_atual = 2026

    def __init__(self, nome, idade):
        # ATRIBUTO DE INSTÂNCIA: específico de cada pessoa
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        # Acessa o atributo da classe por meio do self(ou Pessoa.ano_atual)
        return self.ano_atual - self.idade

# ===============================
# Instanciando a classe (objetos)
# ===============================


# Criando instâncias
p1 = Pessoa('Ana', 25)
p2 = Pessoa('Carlos', 30)

print(p1.get_ano_nascimento())  # 2026 - 25 = 2001
print(p2.get_ano_nascimento())  # 2026 - 30 = 1996

# Acessando diretamente pela classe ou pelas instâncias:
print(Pessoa.ano_atual)  # 2026
print(p1.ano_atual)      # 2026
print(p2.ano_atual)      # 2026

# =================================================
# O que acontece se alterarmos o Atributo de Classe?
# Se você alterar o valor diretamente na Classe, todas as instâncias existentes e futuras verão o novo valor:

# Alterando o atributo de classe diretamente na CLASSE:
Pessoa.ano_atual = 2027

print(Pessoa.ano_atual)  # 2027
print(p1.ano_atual)      # 2027
print(p2.ano_atual)      # 2027

# Agora todos os objetos refletem a mudança!
print(p1.get_ano_nascimento())  # 2027 - 25 = 2002
print(p2.get_ano_nascimento())  # 2027 - 30 = 1997

# =================================================
# 🚨 Cuidado com o "Sombreamento" (Shadowing)
# Uma pegadinha comum em Python acontece quando tentamos alterar um atributo de classe através de uma instância:

# Ao invés de mudar o atributo de classe, isso CRIA um novo atributo de INSTÂNCIA em p1!
p1.ano_atual = 2030

print(p1.ano_atual)      # 2030 (Lê o atributo de INSTÂNCIA criado em p1)
print(p2.ano_atual)      # 2027 (Continua lendo o atributo de CLASSE)
print(Pessoa.ano_atual)  # 2027 (O atributo da classe NÃO foi modificado!)

# =================================================
# Como o Python busca atributos?
# Quando você digita objeto.atributo, o Python faz uma busca em ordem:
# 1. Procura primeiro no dicionário do próprio objeto (p1.__dict__).
# 2. Se não encontrar, procura no dicionário da classe (Pessoa.__dict__).

print(p1.__dict__)
print(Pessoa.__dict__)

# =================================================
# O que é a função vars()?
# vars() é uma função built-in (nativa) do Python.
# Quando você passa um objeto como argumento para ela (vars(objeto)), ela retorna exatamente o __dict__ desse objeto.

print("*" * 20)
print(p1.__dict__)
print(vars(p1))

"""
Resumo
------
- Use Atributo de Instância para dados únicos de cada objeto (ex: nome, CPF, saldo).
- Use Atributo de Classe para valores constantes ou compartilhados por todos os objetos (ex: ano atual, taxa de juros padrão, contador de instâncias criadas).
- Para alterar o atributo de classe para todo mundo, modifique via NomeDaClasse.atributo = novo_valor.
"""
