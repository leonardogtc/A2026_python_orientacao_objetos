# Classes Abstratas
  -----------------
**Classes abstratas** são conhecidas em Python como Abasstract Base Classes ou **ABCs**. São classes projetadas para servir como **moldes ou contratos** para outras classes.
Uma classe abstrata **não pode ser instanciada diretamente** e exige que suas subclasses concretas **implementem obrigatoriamente** determinados métodos.

1. PAra que servem as Classes Abstratas?
- **Garantir um Contrato (Interface):** Garantir que todas as subclasses tenham os mesmos métodos essenciais, padronizados a interface da aplicação.
- **Evitar Instanciação Indevida:** Impedir que o desenvolvedor crie objetos de uma classe que é puramente conceitual (ex: instanciar `Animais` em vez de `Cachorro` ou `Gato`).
- **Evitar Erros em Tempo de Execução:** Diferente do `raise NotImplementedError`, o módulo `abc` do Python impede a criação do objeto logo na **instanciação**, capturando erros bem mais cedo.

2. Como criar uma Classe Abstrata em Python?
Em Python, usamos o módulo nativo `abc` (Abstract Base Classes):

* Herdar de `ABC`.
* Decorar os métodos obrigatórios com `@abstractmethod`.