"""
5. Preservando Metadados com functools.wraps
Quando decoramos uma função, ela passa a ser o wrapper.
Isso altera seu nome (__name__) e sua documentação (__doc__).
Para evitar isso, usa-se o decorador @wraps do módulo functools:
"""
from functools import wraps


def meu_decorador(func):
    @wraps(func)    # Preserva os metadados da func original
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@meu_decorador
def diga_ola():
    """Esta função diz olá."""
    print("Olá!")


print(diga_ola.__name__)    # Mantém "diga_ola" em vez de "wrapper"