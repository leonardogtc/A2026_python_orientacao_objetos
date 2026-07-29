# Para criar uma classe uso a palavra reservada class
# Para chamar uma classe uso parenteses
# Para instanciar uma classe uso a palavra reservada instanciar

class Pessoa:
    # O ... serve como placeholder, indicando que a classe está vazia, ou seja,
    # não tem nada dentro dela. Uma classe é como uma planta baixa de um
    # objeto, ela define as características e comportamentos que o objeto terá
    ...


# instanciar a classe
p1 = Pessoa()
p1.nome = "Leonardo"
p1.sobrenome = "Tavares"

p2 = Pessoa()
p2.nome = 'Oliver'
p2.sobrenome = 'Tavares'

p1_tipo = type(p1)
p2_tipo = type(p2)

print(p1_tipo)
print(p2_tipo)
print(p1.nome)
print(p2.nome)
