"""
Polimorfismo
------------
Conceito: O Polimorfismo é um dos pilares da Orientação a Objetos (POO). A palavra vem do grego (poly = muitas, morph = formas) e significa a capacidade de um mesmo método/mensagem ter comportamentos diferentes dependendo do objeto que o executa.

Em termos práticos: diferentes classes podem implementar um método com o mesmo nome e assinatura, permitindo que você trate esses objetos de forma unificada.

1. Como o Polimorfismo funciona em Python?
Em Python, o polimorfismo é atingido principalmente de duas formas:

    - Herança e Sobrescrita de Métodos (Override): Uma classe filha (subclasse) herda de uma classe pai (superclasse ou classe abstrata) e redefine a implementação de um método.
    
    - Duck Typing (Tipagem de Pato): "Se anda como um pato e canta como um pato, então é um pato". Em Python, por ser uma linguagem dinamicamente tipada, você não precisa necessariamente ter herança direta para usar polimorfismo — basta que os objetos implementem o mesmo método com a mesma assinatura.

O uso mais comum e seguro do polimorfismo na POO clássica é através de Classes Abstratas (abc.ABC), onde a classe pai define o contrato (quais métodos as filhas devem ter).

"""

from abc import ABC, abstractmethod

# Classe abstrata define a interface de contrato


class Notificacao(ABC):
    def __init__(self, mensagem: str) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        """ Métod abstrato que deve ser implementado pelas subclasses """
        pass

# Subclasse 1
# -----------


class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print(f"Enviando E-mail: '{self.mensagem}'")
        return True


# Subclasse 2
# -----------
class NotificacaoSMS(Notificacao):

    def enviar(self) -> bool:
        print(f"Enviando SMS: '{self.mensagem}'")
        return True


# Função polimórfica: recebe QUALQUER notificação e chama o método .enviar()
def notificar_usuario(notificacao: Notificacao) -> None:
    sucesso = notificacao.enviar()
    if sucesso:
        print("Notificação enviada com sucesso\n")


# Uso:
email = NotificacaoEmail("Seu código de verificação é 1234")
sms = NotificacaoSMS("Seu código de verificação é 1234")

# A função notificar_usuario aceita ambos os objetos,
# mas cada um executa seu próprio método enviar()!
notificar_usuario(email)  # Executa o enviar() de NotificacaoEmail
notificar_usuario(sms)  # Executa o enviar() de NotificacaoSMS

"""
2. O Princípio de Substituição de Liskov (LSP)
O Polimorfismo está diretamente ligado ao Princípio de Substituição de Liskov (LSP) (o L do SOLID):

    - Se $S$ é uma subclasse de $T$, então objetos do tipo $T$ podem ser substituídos por objetos do tipo $S$ sem quebrar o programa.

No exemplo acima, a função notificar_usuario espera um objeto do tipo Notificacao. Como NotificacaoEmail e NotificacaoSMS são subclasses de Notificacao, podemos passar qualquer uma delas sem alterar o funcionamento do método notificar_usuario.

"""