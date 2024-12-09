## Exercício Avaliativo 02 - Polimorfismo e Duck Typing

### Parte 01 - Polimorfismo "tradicional"

* Imagine que você está desenvolvendo um sistema de simulação para um zoológico virtual. Todos os animais do zoológico devem ser capazes de emitir um som característico.

- [x] Crie uma classe base chamada Animal com um método chamado emitir_som() (não implemente nada dentro deste método).
- [x] Crie pelo menos três classes que herdam de Animal (Cachorro, Gato, Leao) e implementam o método emitir_som() com sons diferentes, como "Au au", "Miau" e "Rugido", respectivamente.
- [x] Crie uma lista de instâncias dessas classes e use um loop para chamar o método emitir_som() para cada animal.
- [x] Mostre a saída esperada do programa.

Respostas no arquivo abaixo:
[animal.py](./animal.py)

####  Perguntas:
1. Explique como o polimorfismo ajuda a manter o código flexível e reutilizável neste exemplo.
R- Como não necessita alterar a superclasse, você tem a flexibilidade de usar a mesma função mas com as modificações necessárias para classe filha, assim qualquer classe filha pode usar o mesmo método herdado mas com suas particularidades.
2. O que aconteceria se você tentasse criar uma instância da classe Animal diretamente?
R- Funcionaria normalmente se eu tivsse implementado algo nela, as modificações são apenas feitas para as instâncias das classes filhas
    
### Parte 02 - Polimorfismo do python - duck typing

* Você está desenvolvendo um jogo onde personagens podem realizar ações diferentes. Nem todos os personagens precisam ser da mesma classe, mas devem saber executar as ações básicas esperadas pelo jogo.

- [x] Crie três classes (Cavaleiro, Mago, Dragao) e implemente um método atacar() em cada uma, com descrições diferentes (ex.: "O cavaleiro ataca com sua espada").
- [x] Crie uma função chamada executar_ataque(lista_de_personagens) que recebe uma lista de objetos e chama o método atacar() de cada um.
- [x] Teste a função com instâncias das três classes diferentes.

Respostas no arquivo abaixo:
[jogo.py](./jogo.py)

####  Perguntas:

3. Explique por que o método atacar() não precisa estar definido em uma classe base neste caso.
R- Pois para função executar_ataque() as outras classes apenas precisam do comportamento de atacar(), para funcionar corretamente então não a necessidade de as outras classes herdarem esse comportamento de outra classe.
4. O que aconteceria se você passasse um objeto que não possui o método atacar() na lista para a função executar_ataque()?
R- Não rodaria pois para funcionar nela, a única coisa necessária é ter o método atacar()

### Parte 03

Você está desenvolvendo um sistema de combate para um jogo de RPG. No jogo, existem diversos tipos de personagens e criaturas, cada um **com habilidades e formas de ataque únicas**. Esses personagens podem atacar uns aos outros e interagir com elementos do cenário. Além disso, alguns elementos do cenário (como armadilhas) podem causar dano. Seu objetivo é modelar o sistema com os seguintes requisitos:

- [x] Crie uma classe base chamada Entidade:
    * Cada entidade deve ter um atributo vida inicial (ex.: 100 para personagens e 50 para armadilhas).
    * Deve possuir um método acao() que será implementado de forma diferente para cada tipo de entidade. O método acao() de uma entidade deve permitir que ela ataque outra entidade, reduzindo sua vida.
    * Crie pelo menos 4 subclasses ou classes independentes que representam entidades diferentes:
        * Guerreiro: realiza ataques corpo a corpo, causando 10 pontos de dano.
        * Mago: realiza ataques mágicos, causando 15 pontos de dano.
        * Dragao: cospe fogo, causando 20 pontos de dano.
        * Armadilha: é um objeto do cenário que, quando ativado, causa 5 pontos de dano.

- [ ] Crie uma classe chamada Combate
    * Deve ter um atributo de classe que é uma lista das entidades que irão participar do combate.
    * Deve ter o método simular_combate.
        Para cada entidade na lista de entidades, chama o método acao() e imprime o resultado no console.
    * Deve ter um método chamado add_entidade para adicianar entidades para o combate;
        * Esse método recebe uma instância de uma entidade (como Guerreiros, Magos, Dragões ou Armadilhas).
    * Crie um método da classe Combate que atualize a função simular_combate para que o combate continue enquanto pelo menos duas entidades ainda tiverem vida maior que zero.
    
##### Exemplo de saída (parcial e hipotética) esperada:

* O Guerreiro realiza um ataque corpo a corpo, causando 10 de dano!
* O Mago lança uma magia poderosa, causando 15 de dano!
* O Dragão cospe fogo, causando 20 de dano!
* A Armadilha é ativada, causando 5 de dano!

Respostas no arquivo abaixo:
[rpg.py](./rpg.py)
####  Perguntas:

5. Explique como o uso de polimorfismo simplifica a implementação da função simular_combate.
R- Apenas precisei ter o método atacar e parada cada classe filha fiz a modificação necessaria, sendo diferente em cada classe filha e não alterando a classe mão
6. Em que situações o duck typing pode causar erros neste sistema? Como você evitaria esses erros?
R- Caso classe não tivesse o método e para evitar isso poderia usar o tratamento de erro com o para AttributeError que seria esse caso.
7. Qual seria a vantagem de usar classes base versus deixar as classes independentes e confiar no duck typing?
R- Depende da sua aplicação caso queira manter um relação entre classes seria melhor usar classe base, mas se você só quer usar um método de uma classe em uma situação especifica não precisa ter esse laço de herança.