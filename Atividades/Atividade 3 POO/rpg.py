class Entidade:
    def __init__(self, vida_inicial):
        self.vida_inicial = vida_inicial

    def acao(self, inimigo):
        pass


class Guerreiro(Entidade):
    def __init__(self):
        super().__init__(100)

    def acao(self, inimigo):
        dano = 10
        inimigo.vida_inicial -= dano
        print(f"O Guerreiro realiza um ataque corpo a corpo, causando {dano} de dano!")


class Mago(Entidade):
    def __init__(self):
        super().__init__(100)

    def acao(self, inimigo):
        dano = 15
        inimigo.vida_inicial -= dano
        print(f"O Mago lança uma magia poderosa, causando {dano} de dano!")


class Dragao(Entidade):
    def __init__(self):
        super().__init__(100)

    def acao(self, inimigo):
        dano = 20
        inimigo.vida_inicial -= dano
        print(f"O Dragão cospe fogo, causando {dano} de dano!")


class Armadilha(Entidade):
    def __init__(self):
        super().__init__(50)

    def acao(self, inimigo):
        dano = 5
        inimigo.vida_inicial -= dano
        print(f"A Armadilha é ativada, causando {dano} de dano!")


class Combate:
    def __init__(self, lista_de_entidades):
        self.lista_de_entidades = lista_de_entidades

    def simular_combate(self):
        while self.contar_entidades_vivas() > 1:
            for entidade in self.lista_de_entidades:
                if entidade.vida_inicial > 0:  # Verifica se está vivo
                    inimigos = self.obter_inimigos(entidade)
                    if inimigos:  # Se houver inimigos vivos
                        entidade.acao(inimigos[0])  # Ataca o primeiro inimigo da lista
                if self.contar_entidades_vivas() <= 1:  # Verifica se tem pelo menos 2 vivos
                    break

    def contar_entidades_vivas(self):
        return sum(1 for entidade in self.lista_de_entidades if entidade.vida_inicial > 0)

    def obter_inimigos(self, entidade):
        # Retorna uma lista de inimigos, excluindo a própria entidade
        return [e for e in self.lista_de_entidades if e != entidade and e.vida_inicial > 0]

    def add_entidade(self, entidade):
        self.lista_de_entidades.append(entidade)


# Testes
# Instanciando
guerreiro = Guerreiro()
mago = Mago()
dragao = Dragao()
armadilha = Armadilha()

# Colocando as entidades na lista da classe combate
combate = Combate([guerreiro, mago, dragao, armadilha])

# Iniciando o combate
combate.simular_combate()
