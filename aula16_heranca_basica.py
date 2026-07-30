"""
Herança é um dos pilares fundamentais da Programação Orientada a Objetos (POO).

Ela permite criar uma nova classe (chamada de Subclasse, Classe Filha ou Derivada) que reaproveita e estende os atributos e métodos de uma classe já existente (chamada de Superclasse, Classe Pai ou Base).

Mnemônica de relacionamento:
Associação/Agregação/Composição: Relação do tipo "Tem-um" (has-a) — ex: O Carro tem um Motor.
Herança: Relação do tipo "É-um" (is-a) — ex: O Cliente é uma Pessoa.

- Associação/Agregação/Composição: Relação do tipo "Tem-um" (has-a) — ex: O Carro tem um Motor.
- Herança: Relação do tipo "É-um" (is-a) — ex: O Cliente é uma Pessoa.

1. Por que usar Herança?
    1.1. Reutilização de Código (DRY - Don't Repeat Yourself): Evita duplicar código comum em várias classes.
    1.2. Especialização: Permite que a classe filha herde tudo o que é comum e adicione apenas o que for específico dela.
    1.3. Organização Hierárquica: Facilita a manutenção do sistema definindo uma estrutura clara entre os conceitos.

2. Sintaxe Básica
Em Python, a herança é definida simplesmente colocando o nome da classe pai entre parênteses após o nome da classe filha.

"""
# Superclasse ou classe Pai


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_completo(self):
        print(f"{self.nome} {self.sobrenome}")


# Subclasse (Classe Filha) - Herda de Pessoa
class Cliente(Pessoa):
    pass


class Aluno(Pessoa):
    pass


# Instanciando
c1 = Cliente("Leonardo", "Gonçalves")
a1 = Aluno("Oliver", 'Pontes')

# Tanto Cliente quanto Aluno possuem o método falar_nome_completo() herdado de Pessoa!
c1.falar_nome_completo()  # Output: Leonardo Gonçalves
a1.falar_nome_completo()  # Output: Maria Silva
