"""
3. Composição (Relação Todo-Parte Dependente)
Na Composição, a classe principal é a dona absoluta das suas partes. Ela própria cria as instâncias das outras classes internamente. Se o objeto pai for destruído, todos os seus objetos filhos são destruídos junto com ele.

Exemplo: Cliente e Endereco
Um endereço pertence a um determinado cliente. Se o registro do cliente for apagado do sistema, o endereço atrelado a ele também deixa de existir.
"""
class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

    def __del__(self):
        print(f"Endereço '{self.rua}, {self.cidade}' foi apagado da memória!")


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []  # Lista de endereços compostos

    def inserir_endereco(self, rua, cidade):
        # A COMPOSIÇÃO ocorre aqui: a própria classe Cliente instancia Endereco!
        self.enderecos.append(Endereco(rua, cidade))

    def listar_enderecos(self):
        for end in self.enderecos:
            print(f"{self.nome} mora em: {end.rua}, {end.cidade}")


# Criamos o cliente e mandamos ele criar seus endereços
cliente1 = Cliente("Maria")
cliente1.inserir_endereco("Av. Paulista", "São Paulo")
cliente1.inserir_endereco("Rua das Flores", "Campinas")

cliente1.listar_enderecos()

print("\n--- Apagando o cliente ---")
# Ao apagar o cliente1, todos os objetos Endereco criados por ele são DESTRUÍDOS!
del cliente1
# Output:
# --- Apagando o cliente ---
# Endereço 'Av. Paulista, São Paulo' foi apagado da memória!
# Endereço 'Rua das Flores, Campinas' foi apagado da memória!


"""
🎯 Guia Prático: Como escolher qual usar?
    1. Associação: "O objeto A usa o objeto B" (ex: Pessoa usa Ferramenta).

    2. Agregação: "O objeto A tem/contém objetos B, mas os B existem sozinhos" (ex: Empresa tem Funcionarios).
    
    3. Composição: "O objeto A é dono dos objetos B e é responsável por criá-los e destruí-los" (ex: Casa possui Quartos).
"""