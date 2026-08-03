"""
4. Polimorfismo por Duck Typing em Python
Diferente de linguagens estaticamente tipadas (como Java ou C#), em Python duas classes não precisam ter a mesma superclasse para serem tratadas de forma polimórfica:
"""


class Cachorro:
    def falar(self) -> str:
        return "Au au"


class Gato:
    def falar(self) -> str:
        return "Miau miau"


class Relogio:
    def falar(self) -> str:
        return "Tic-tac"


def fazer_falar(object):
    # Não importa a classe do objeto, desde que ele tenha o método .falar()
    print(object.falar())

fazer_falar(Cachorro())
fazer_falar(Gato())
fazer_falar(Relogio())

"""
Vantagens do Polimorfismo

    - Desacoplamento: Seu código depende de interfaces/contratos, não de implementações concretas.
    
    - Extensibilidade: Para adicionar um novo tipo de notificação (ex: NotificacaoWhatsApp), basta criar a classe e implementar o método enviar(). A função notificar_usuario continuará funcionando sem mudar uma única linha de código.
    
    - Reutilização e Organização: Reduz duplicação de estruturas condicionais (if/elif/else para checar tipos).
"""