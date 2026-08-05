"""
6. Exemplo Prático: Medidor de Tempo de Execução
Um dos usos mais comuns de decoradores é para medição
de desempenho, autenticação, caching ou geração de logs:
"""
import time
from functools import wraps


def cronometro(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(
            f"A função '{func.__name__}' levou {fim - inicio:.4f}s para executar.")
        return resultado
    return wrapper


@cronometro
def processar_dados():
    time.sleep(1)   # Simula um processamento demorado


processar_dados()

"""
Resumo
    - Decorador: Função que envelopa outra função para modificar seu comportamento.
    - Sintaxe @: Atalho para aplicar a função decoradora sobre a função definida abaixo.
    - Uso comum: Validação de permissões, medir tempo de execução, registros de log, controle de fluxo (ex: cache de funções).
"""
