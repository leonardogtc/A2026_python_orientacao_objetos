from enum import Enum


class StatusPedido(Enum):
    PENDENTE = "Pendente"
    PAGO = "Pago"
    ENVIADO = "Enviado"


class Pedido:
    def __init__(self, cliente: str):
        self.cliente = cliente
        self.status = StatusPedido.PENDENTE  # Estado inicial

    def pagar(self):
        if self.status == StatusPedido.PENDENTE:
            self.status = StatusPedido.PAGO
            print(f"Pedido de {self.cliente} pago com sucesso!")
        else:
            print(
                f"Não é possível pagar um pedido no status: {self.status.value}"
            )

    def enviar(self):
        if self.status == StatusPedido.PAGO:
            self.status = StatusPedido.ENVIADO
            print(f"Pedido de {self.cliente} enviado!")
        else:
            print("O pedido precisa estar PAGO antes de ser enviado.")


# Testando a classe Pedido com o Enum
pedido1 = Pedido("Leonardo")
print(pedido1.status.value)  # Pendente

pedido1.enviar()  # O pedido precisa estar PAGO antes de ser enviado.
pedido1.pagar()  # Pedido de Leonardo pago com sucesso!
pedido1.enviar()  # Pedido de Leonardo enviado!
