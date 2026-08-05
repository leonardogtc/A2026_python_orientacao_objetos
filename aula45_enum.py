# Enum
# ----
# O Enum (abreviação de Enumeration ou Enumeração) em Python é um recurso do
# módulo padrão enum usado para definir um conjunto de constantes com nomes
# significativos e valores imutáveis.

from enum import Enum

# 1. Criando um Enum


class StatusPedido(Enum):
    PENDENTE = 1
    PROCESSANDO = 2
    ENVIADO = 3
    ENTREGUE = 4
    CANCELADO = 5


# Acessando o Enum
status = StatusPedido.PENDENTE

print(status)
print(status.name)
print(status.value)
