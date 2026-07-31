"""
Conceito
========
Um Mixin é uma classe especial cujo único objetivo é adicionar funcionalidades/métodos extras a outras classes através de herança múltipla.

Ao contrário de uma classe comum, o Mixin não representa uma entidade completa do seu sistema e não é feito para ser instanciado diretamente.

1. Principais Características de um Mixin
    1.1. Não é instanciado sozinho: Você nunca fará log = LogMixin(). Ele só serve para ser herdado por outras classes.
    1.2. Propósito Único: Fornece um comportamento específico e reutilizável (ex: gerar Logs, exportar para JSON, enviar e-mails).
    1.3. Pode ser injetado em qualquer classe: Qualquer classe pode herdar um Mixin, independentemente de sua posição na hierarquia de herança.
    1.4. Convenção de Nome: Costuma-se adicionar a palavra Mixin ao final do nome da classe (ex: LogMixin, JSONMixin, RenderHTMLMixin).

2. Para que serve na prática? (Problema vs Solução)
Imagine que você precisa adicionar a capacidade de gerar Logs para a classe Cliente e para a classe Produto.

    - Sem Mixin: Você teria que duplicar o código do método de log em Cliente e em Produto, ou criar uma herança forçada que não faz sentido conceitual (como fazer Produto herdar de Pessoa).
    - Com Mixin: Você cria a classe LogMixin uma única vez e "plug-and-play" (associa via herança múltipla) onde precisar.

3. Exemplo Prático em Código:
"""

# =================== 1. O MIXIX ===================


class LogMixin:
    """ Mixin que adiciona a funcionalidade de registrar logs. """

    def log(self, mensagem):
        nome_classe = self.__class__.__name__
        print(f"[LOG - {nome_classe}]: {mensagem}")

    def log_error(self, erro):
        nome_classe = self.__class__.__name__
        print(f"[ERRO - {nome_classe}]: {erro}")

# =================== 2. CLASSES DE DOMÍNIO ===================


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

# Cliente 'é uma' Pessoa E 'tem funcionalidade de' LogMixin


class Cliente(Pessoa, LogMixin):
    def salvar(self):
        # Usa o método herdado do Mixin!
        self.log(f"Cliente {self.nome} foi salvo no banco de dados.")


class Produto(LogMixin):    # Não herda de Pessoa, mas ganha o Mixin de Log!
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def comprar(self):
        self.log(f"Produto {self.nome} (R$ {self.preco}) foi comprado.")


# ================= 3. USO =================
c1 = Cliente("Leonardo")
c1.salvar()
# Output: [LOG - Cliente]: Cliente Leonardo foi salvo no banco de dados.
p1 = Produto("Notebook", 4500.0)
p1.comprar()
# Output: [LOG - Produto]: Produto Notebook (R$4500.0) foi comprado.
