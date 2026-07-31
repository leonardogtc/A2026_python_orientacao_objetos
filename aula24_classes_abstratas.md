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

3. O que acontece se uma Subclasse NÃO implementar o método abstrato?
Se você esquecer de implementar um método decorado com `@abstractmethod`, a própria subclasse **se tornará abstrata** e o Python impedirá sua criação:

class NotificacaoWhatsApp(Notificacao):
    pass  # Esqueceu de implementar o método enviar()!

# ❌ Lança erro imediatamente ao tentar instanciar:
w1 = NotificacaoWhatsApp("Olá")
# TypeError: Can't instantiate abstract class NotificacaoWhatsApp with abstract method enviar

4. `@abstractmethod` combinado com `@property` (Propriedade Abstrata)
Você também pode exigir que as subclasses implementem propriedades obrigatórias:

from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, saldo):
        self._saldo = saldo

    # Exige que a subclasse defina a propriedade 'saldo'
    @property
    @abstractmethod
    def saldo(self):
        pass


class ContaCorrente(Conta):
    @property
    def saldo(self):
        return self._saldo


cc = ContaCorrente(1500.0)
print(cc.saldo)  # 1500.0
