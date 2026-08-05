"""
4. Aceitando Argumentos na Função Decorada (*args, **kwargs)

Se a função que você quer decorar recebe parâmetros ou
retorna um valor, a função wrapper interna deve repassar
esses argumentos e retornar o resultado:
"""


def log_execucao(func):
    def wrapper(*args, **kwargs):
        print(
            f"Chamando {func.__name__} com argumentos {args} e {kwargs}"
        )
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} finalizada.")
        return resultado
    return wrapper


@log_execucao
def somar(a, b):
    return a + b


res = somar(5, 3)
print(res)
