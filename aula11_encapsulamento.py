"""
Encapsulamento é um dos pilares fundamentais da Programação Orientada a Objetos (POO). Ele consiste em agrupar dados (atributos) e comportamentos (métodos) dentro de uma classe e proteger o acesso direto a dados sensíveis, garantindo a integridade do objeto.

1. A Filosofia do Encapsulamento em Python
Em linguagens como Java, C# ou C++, existem palavras-chave estritas (public, protected, private) que impedem o compilador de acessar atributos protegidos.

Em Python não existem modificadores de acesso restritivos por padrão. O Python adota a filosofia: "We are all consenting adults here" (Somos todos adultos consentidos aqui).

Em vez de proibir o acesso via código no compilador, o Python usa convenções de nomenclatura com o caractere _ (sublinhado) para indicar a visibilidade aos desenvolvedores.

2. Os 3 Níveis de Visibilidade em Python

Nível:	            Público
Convenção:          nome
Descrição:          Acesso livre em qualquer lugar.
Acesso Externo:     ✅ Permitido

Nível:	            Protegido
Convenção:          _nome
Descrição:          Uso interno da classe e subclasses (convenção).
Acesso Externo:     ⚠️ Acessível (mas não recomendado)

Nível:	            Privado
Convenção:          __nome
Descrição:          "Forte" proteção interna (Name Mangling).
Acesso Externo:     ❌ Ocultado (mas acessível por truque)
"""


class ContaBancaria:
    def __init__(self, titular, saldo, senha):
        # 1. Atributo PÚBLICO: qualquer um pode ler/alterar livremente
        self.titular = titular

        # 2. Atributo PROTEGIDO (_): convenção que indica "uso interno"
        self._saldo = saldo

        # 3. Atributo PRIVADO (__): ativa Name Mangling (desfiguração de nome)
        self.__senha = senha

    # Método público para alterar o saldo de forma segura
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")

    # Método privado interno
    def __validar_senha(self, senha_digitada):
        return self.__senha == senha_digitada


# ================= HORA DE TESTAR ===============

conta = ContaBancaria('Leonardo', 10000.0, '1234')

# 1. PÚBLICO: Acesso livre
print(conta.titular)  # Output: Leonardo
conta.titular = "Leonardo Gonçalves"

# 2. PROTEGIDO (_): O Python PERMITE acessar, mas a convenção diz para NÃO FAZER isso por fora!
print(conta._saldo)   # Funciona, mas quebra a boa prática!

# 3. PRIVADO (__): O Python esconde este atributo
# print(conta.__senha)  # ❌ AttributeError: 'ContaBancaria' object has no attribute '__senha'

"""
4. O que é o Name Mangling (Desfiguração de Nomes)? ⚠️❌
Quando você usa dois sublinhados (__atributo), o Python renomeia o atributo internamente adicionando _NomeDaClasse antes dele.

No exemplo acima, __senha vira internamente: _ContaBancaria__senha.

Se você realmente quiser (embora não deva), ainda consegue acessar:
"""
print(conta._ContaBancaria__senha)

# Para que serve o __ afinal? O principal objetivo do __ não é a segurança contra hackers, mas sim evitar conflitos de nomes (sobreescrita acidental) quando uma subclasse herda dessa classe.

# 5. Encapsulamento com @property (O jeito Pythônico)
# Em Python, a forma perfeita de aplicar encapsulamento é combinar atributos protegidos (_atributo) com o decorador @property:


class BaseDeDados:
    def __init__(self):
        self._dados = {}    # Atributo protegido

    # @property permite LER os dados de forma controlada (Getter)
    @property
    def dados(self):
        return self._dados

    # Método seguro para INSERIR dados
    def inserir_cliente(self, id_cliente, nome):
        if id_cliente not in self._dados:
            self._dados[id_cliente] = nome
        else:
            print("Cliente já cadastrado!")


db = BaseDeDados()
db.inserir_cliente(1, "Ana")
db.inserir_cliente(2, "João")

# Lemos a propriedade com sintaxe limpa:
print(db.dados)  # {1: 'Ana', 2: 'João'}

# Impedimos a sobrescrita acidental do dicionário inteiro por fora:
# db.dados = "qualquer coisa"  # AttributeError: can't set attribute

"""
Resumo:
-------
    1. Público (atributo): Pode ser usado em qualquer lugar.
    2. Protegido (_atributo): Indica convenção de uso interno. Respeite o _!
    3. Privado (__atributo): Ativa Name Mangling para evitar conflitos em herança.
    4. Encapsulamento Pythônico: Use _atributo + @property para expor dados com segurança e elegância.
"""
