"""
O decorador @property em Python é usado para criar atributos gerenciados (propriedades). Ele permite transformar um método de uma classe em um "atributo somente leitura" ou adicionar lógicas de validação e proteção (encapsulamento) ao ler, alterar ou deletar um valor.

Em termos simples: você chama o método como se fosse um atributo comum, sem usar parênteses ().

1. Para que serve o @property?

    1.1. Acesso Pythonico (Getter): Evita sintaxes no estilo Java/C# como objeto.get_preco(). Em Python, usamos simplesmente objeto.preco.

    1.2. Validação de Dados (Setter): Permite colocar regras antes de atribuir um novo valor (objeto.preco = 50), impedindo valores inválidos (como preços negativos).

    1.3. Atributos Calculados: Permite calcular um valor dinamicamente no momento do acesso.

    1.4. Refatoração Sem Quebrar Código: Se você usava um atributo público self.preco e depois precisou adicionar validação, basta transformar preco em @property sem alterar o modo como o restante do código consome esse atributo.

2. Sintaxe Básica: Getter, Setter e Deleter
Uma propriedade em Python pode ter até 3 partes:

    2.1. Getter (@property): Executado quando você lê o valor (x = obj.atributo).
    
    2.2. Setter (@<nome>.setter): Executado quando você altera/atribui o valor (obj.atributo = novo_valor).
    
    2.3. Deleter (@<nome>.deleter): Executado quando você deleta o atributo (del obj.atributo).
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        # O atributo real é protegido por convenção com sublinhado (_preco)
        self.preco = preco  # Aqui já aciona o setter!

    # 1. GETTER: Define 'preco' como propriedade (somente leitura por padrão)
    @property
    def preco(self):
        return self._preco

    # 2. SETTER: Adiciona validação ao tentar alterar o preco (objeto.preco = valor)
    @preco.setter
    def preco(self, novo_preco):
        if not isinstance(novo_preco, (int, float)):
            raise TypeError("O preço deve ser um número inteiro ou float.")
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo!")

        self._preco = float(novo_preco)

    # 3. DELETER: Opcional, executado ao fazer 'del objeto.preco'
    @preco.deleter
    def preco(self):
        print("Apagando o preço do produto...")
        del self._preco


# ================= HORA DE USAR =================
p1 = Produto("Camiseta", 50.0)

# Lendo o atributo (chama o @property / getter) - Note que NÃO usamos p1.preco()
print(f"{p1.nome} custa R$ {p1.preco}.")

# Alterando o valor (chama o @preco.setter)
p1.preco = 79.90
print(f"\n{p1.nome} custa R$ {p1.preco}.")

# Tentando atribuir valor inválido (o setter lança exceção e protege o objeto):
# p1.preco = -10  # ValueError: O preço não pode ser negativo!
# p1.preco = "Cinquenta"  # TypeError: O preço deve ser um número...


# ================= ATRIBUTO CALCULADO =================
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # Atributo calculado dinamicamente
    @property
    def area(self):
        return self.largura * self.altura


ret = Retangulo(10, 5)
print(ret.area)


"""
Resumo dos Benefícios
---------------------
    1. Sintaxe limpa: objeto.atributo em vez de objeto.get_atributo().
    
    2. Segurança: O atributo privado (ex: _preco) fica protegido por trás do @property e @<prop>.setter.
    
    3. Somente Leitura: Se você definir apenas o @property (getter) sem o @<prop>.setter, o atributo torna-se somente leitura (read-only).
"""