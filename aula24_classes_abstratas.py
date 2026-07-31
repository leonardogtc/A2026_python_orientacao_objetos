"""
# Classes Abstratas
  -----------------
**Classes abstratas** são conhecidas em Python como Abasstract Base Classes ou **ABCs**. São classes projetadas para servir como **moldes ou contratos** para outras classes.
Uma classe abstrata **não pode ser instanciada diretamente** e exige que suas subclasses concretas **implementem obrigatoriamente** determinados métodos.

1. PAra que servem as Classes Abstratas?
- **Garantir um Contrato (Interface):** Garantir que todas as subclasses tenham os mesmos métodos essenciais, padronizados a interface da aplicação.
- **Evitar Instanciação Indevida:** Impedir que o desenvolvedor crie objetos de uma classe que é puramente conceitual (ex: instanciar `Animais` em vez de `Cachorro` ou `Gato`).
- **Evitar Erros em Tempo de Execução:** Diferente do `raise NotImplementedError`, o módulo `abc` do Python impede a criação do objeto logo na **instanciação**, capturando erros bem mais cedo.

2. Como criar uma Classe Abstrata em Python?
Em Python, usamos o módulo nativo `abc` (Abstract Base Classes):

* Herdar de `ABC`.
* Decorar os métodos obrigatórios com `@abstractmethod`.
"""
from abc import ABC, abstractmethod


# 1. Classe Abstrata (Molde / Contrato)
class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    # Método abstrato: TODA subclasse é OBRIGADA a implementar!
    @abstractmethod
    def enviar(self):
        pass


# 2. Subclasse Concreta A
class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f"Enviando E-mail com a mensagem: '{self.mensagem}'")


# 3. Subclasse Concreta B
class NotificacaoSMS(Notificacao):
    def enviar(self):
        print(f"Enviando SMS com a mensagem: '{self.mensagem}'")


# ================= USO =================

# ❌ Tentar instanciar a classe abstrata lança ERRO:
# n = Notificacao("Olá")  
# TypeError: Can't instantiate abstract class Notificacao with abstract method enviar

# ✅ Instanciar as subclasses concretas funciona normalmente:
n1 = NotificacaoEmail("Seu código de verificação é 1234")
n1.enviar()  # Output: Enviando E-mail...

n2 = NotificacaoSMS("Sua compra foi aprovada!")
n2.enviar()  # Output: Enviando SMS...
