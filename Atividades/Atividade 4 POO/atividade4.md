## Exercício Avaliativo - Classes Abstratas

### Parte 01

* Você foi contratado para desenvolver um sistema que gerencie diferentes tipos de dispositivos eletrônicos. Cada dispositivo pode executar uma funcionalidade específica, como ligar, desligar, ou realizar uma operação característica.
* Implemente uma classe abstrata chamada ElectronicDevice e duas subclasses que representem dispositivos específicos. Utilize conceitos de classes abstratas e métodos abstratos.

#### Classe Abstrata ElectronicDevice:
- [x] Deve possuir um método abstrato chamado turn_on que liga o dispositivo.
- [x] Deve possuir um método abstrato chamado turn_off que desliga o dispositivo.
- [x] Deve possuir um método abstrato chamado perform_operation que executa uma funcionalidade específica do dispositivo.

#### Subclasses:

 - [x] **Smartphone:**
* Implementa os métodos abstratos.
* O método perform_operation deve simular o envio de uma mensagem.

 - [x] **Television:**
* Implementa os métodos abstratos.
* O método perform_operation deve simular a mudança de canal.

#### Programa Principal:

- [x] Instancie objetos das classes Smartphone e Television.
- [x] Use os métodos implementados para ligar, desligar e executar uma operação com cada dispositivo.

#### Questões 

* O que acontece se você tentar instanciar a classe ElectronicDevice diretamente?
R- Aparece um erro TypeError: Can't instantiate abstract class ElectronicDevice without an implementation for abstract methods 'perform_operation', 'turn_off', 'turn_on'. Ela é apenas uma classe modelo e não pode ser usada diretamente para criar objetos.
* Por que é importante que o método perform_operation seja abstrato na classe base?
R- Pois se ele nãomfor abstratato as classes filhas não teram a obrigatoriedade de implementá-lo.
* Como você pode garantir que qualquer novo dispositivo implementará os métodos obrigatórios?
R- Criando a superclasse abstrata e seus métodos sendo abstratos a subclasses só vão serem instânciadas se elas implementarem os métodos abstratos.

### Parte 02

Desenvolva um sistema para gerenciar funcionários de uma empresa. Existem diferentes tipos de funcionários, como desenvolvedores e gerentes, e cada um tem suas responsabilidades específicas. O sistema também deve calcular o salário baseado em suas funções e gerenciar os projetos atribuídos.

#### Classe Abstrata Employee:

- [x] Atributos: name, id.
- [x] Métodos abstratos:
    * calculate_salary: Retorna o salário do funcionário.
    * get_responsibilities: Retorna as responsabilidades do cargo.

#### Subclasses:

- [X] Developer:
    * Salário fixo mais bônus por projeto.
    * Responsabilidade: "Escrever código".
- [x] Manager:
    * Salário fixo mais um bônus proporcional ao número de funcionários gerenciados.
    * Responsabilidade: "Gerenciar equipe".

#### Classe Project:

- [x] Atributos: name, employees (lista de Employee).
- [x] Métodos:
    * add_employee: Adiciona um funcionário ao projeto.
    * calculate_total_cost: Soma os salários de todos os funcionários do projeto.

#### Programa Principal:

- [x] Crie objetos de Developer e Manager.
- [x] Atribua-os a um projeto.
- [x] Exiba os custos do projeto e as responsabilidades de cada funcionário.

## Exercício Avaliativo

* Faça os execícios da seção 10.7 e 10.9, 11.4 e 11.6 da apostila **py14** da caelum. Envie as soluções pelo SIGAA. As soluções podem ser enviadas através de um arquivo compactado ou arquivo com o link do github com seu código;