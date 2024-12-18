from abc import ABC, abstractmethod
import random

class Personagem(ABC):
    def __init__(self, nome: str):
        self.nome = nome
        self.energia = random.randint(5, 10) #Decidi que a nergia que cada personagem recebe vai variar entre 5 e 10
        self.sorte = random.randint(1, 6)
        self.historico_batalhas = []

    def incremento(self, quantidade):
        self.energia += quantidade
        if self.energia > 10: #Esse if controla o valor de energia e não deixa passar de 10
            self.energia = 10

    def decremento(self, quantidade):
        self.energia -= quantidade
        if self.energia <= 0:
            print(f"{self.nome} morreu.")
            self.energia = 0 # Mesmo que um ataque faça ele ficar -1 por exemplo de energia no final ele vai ter 0 de energia

    @abstractmethod
    def sorteio(self): 
        pass

    def interagir(self, outro_personagem): #Ducktyping - assume que o outro_personagem tem o atributo nome
        #Antes de interagir verifica se algum personagem está morto
        if(self.energia == 0):
            print(f"{self.nome} morreu então não pode interagir")
            return
        elif(outro_personagem.energia == 0):
            print(f"{outro_personagem.nome} morreu então não pode interagir")
            return
        print(f"{self.nome} está falando com {outro_personagem.nome}.")

class Mocinho(Personagem):
    def sorteio(self): #Uso da classe abstrata da classe mãe
        return random.randint(1, 6)

    def alimentar(self):
        if(self.energia > 0):
            print(f"{self.nome} está se alimentando.")
            self.incremento(2) #Os mocinhos ganham 2 pontos 
        else:
            print(f"{self.nome} está morto e não pode se alimnetar.")

    def lutar(self, outro_personagem):
        #Sorteando o valor de cada personagem
        mocinho = self.sorteio()
        vilao = outro_personagem.sorteio()
        if(mocinho > vilao):
            self.incremento(2) #Vencedor ganha 2 pontos
            outro_personagem.decremento(2) #Derrotado perde 2 pontos
            batalha_vencedor = f"{self.nome} bateu no {outro_personagem.nome}"
            batalha_perdedor = f"{outro_personagem.nome} apanhou de {self.nome}"
            #Coloca os históricos tanto do vencedor quanto do perdedor
            self.historico_batalhas.append(batalha_vencedor)
            outro_personagem.historico_batalhas.append(batalha_perdedor)
        elif(vilao > mocinho):
            outro_personagem.incremento(2)
            self.decremento(2)
            batalha_vencedor = f"{outro_personagem.nome} bateu no {self.nome}"
            batalha_perdedor = f"{self.nome} apanhou de {outro_personagem.nome}"
            self.historico_batalhas.append(batalha_perdedor)
            outro_personagem.historico_batalhas.append(batalha_vencedor)
        elif(mocinho == vilao):
            self.decremento(1) #Quando empata ambos perdem 1 ponto
            outro_personagem.decremento(1)
            empate_mocinho = f"{self.nome} empatou com {outro_personagem.nome}"
            empate_vilao = f"{outro_personagem.nome} empatou com {self.nome}"
            #Vai ser armazendado cada empate
            self.historico_batalhas.append(empate_mocinho)
            outro_personagem.historico_batalhas.append(empate_vilao)

    def conversar(self):
        print(f"{self.nome} está conversando.")

    def interagir(self, outro_personagem): #Polimorfismo
        #Antes de interagir verifica se algum personagem está morto
        if(self.energia == 0):
            print(f"{self.nome} morreu então não pode interagir")
            return
        elif(outro_personagem.energia == 0):
            print(f"{outro_personagem.nome} morreu então não pode interagir")
            return
        print(f"{self.nome} está conversando com {outro_personagem.nome}.") 
        outro_personagem.incremento(1) #Ao conversar o alvo recebe 1 ponto

class Vilao(Personagem):
    def sorteio(self):
        return random.randint(1, 6)

    def atacar(self, outro_personagem):
        print(f"{self.nome} está atacando {outro_personagem.nome}.")
        outro_personagem.decremento(2)

    def zombar(self):
        print(f"{self.nome} está zombando.")

    def lutar(self, outro_personagem):
        #Sorteando o valor de cada personagem
        vilao = self.sorteio()
        mocinho = outro_personagem.sorteio()
        if(vilao > mocinho):
            self.incremento(2) #Vencedor ganha 2 pontos
            outro_personagem.decremento(2) #Derrotado perde 2 pontos
            batalha_vencedor = f"{self.nome} bateu no {outro_personagem.nome}"
            batalha_perdedor = f"{outro_personagem.nome} apanhou de {self.nome}"
            #Coloca os históricos tanto do vencedor quanto do perdedor
            self.historico_batalhas.append(batalha_vencedor)
            outro_personagem.historico_batalhas.append(batalha_perdedor)
        elif(mocinho > vilao):
            outro_personagem.incremento(2)
            self.decremento(2)
            batalha_vencedor = f"{outro_personagem.nome} bateu no {self.nome}"
            batalha_perdedor = f"{self.nome} apanhou de {outro_personagem.nome}"
            self.historico_batalhas.append(batalha_perdedor)
            outro_personagem.historico_batalhas.append(batalha_vencedor)
        elif(vilao == mocinho):
            self.decremento(1) #Quando empata ambos perdem 1 ponto
            outro_personagem.decremento(1)
            empate_mocinho = f"{outro_personagem.nome} empatou com {self.nome}"
            empate_vilao = f"{self.nome} empatou com {outro_personagem.nome}"
            #Vai ser armazendado cada empate
            self.historico_batalhas.append(empate_vilao)
            outro_personagem.historico_batalhas.append(empate_mocinho)
    
    def alimentar(self): #Não especificava esse método nessa classe porém na regra de alimentação os vilões também tem regra de alimentação
        if(self.energia > 0):
            print(f"{self.nome} está se alimentando.")
            self.incremento(3) #Os vilões ganham 3 pontos
        else:
            print(f"{self.nome} está morto e não pode se alimnetar.")

    def interagir(self, outro_personagem): #Polimorfismo
        #Antes de interagir verifica se algum personagem está morto
        if(self.energia == 0):
            print(f"{self.nome} morreu então não pode interagir")
            return
        elif(outro_personagem.energia == 0):
            print(f"{outro_personagem.nome} morreu então não pode interagir")
            return
        print(f"{self.nome} está zombando de {outro_personagem.nome}.") 
        outro_personagem.decremento(1) #Ao ser zombado o alvo perde 1 ponto

#Área de teste
"""
#Instânciando o objeto
mocinho = Mocinho("Herói")
vilao = Vilao("Vilão")

#Testando método lutar
mocinho.lutar(vilao)
vilao.lutar(mocinho)

print(f"Histórico do {mocinho.nome}: {mocinho.historico_batalhas}")
print(f"Histórico do {vilao.nome}: {vilao.historico_batalhas}")

#Testando método alimentar
print(f"Energia Mocinho antes: {mocinho.energia}")
print(f"Energia Vilão antes: {vilao.energia}")
mocinho.alimentar()
vilao.alimentar()
print(f"Energia Mocinho depois: {mocinho.energia}")
print(f"Energia Vilão depois: {vilao.energia}")

#Testando execeder a alimentação
mocinho.energia = 10
mocinho.alimentar()
print(f"Energia Mocinho(vida máxima): {mocinho.energia}")

#Testando alimentar um morto
vilao.energia = 0
vilao.alimentar()
print(f"Energia Vilão(morto): {vilao.energia}")

#Testando método interagir
print(f"Energia Vilão antes: {vilao.energia}")
mocinho.interagir(vilao)
print(f"Energia Vilão depois: {vilao.energia}")

print(f"Energia Mocinho antes: {mocinho.energia}")
vilao.interagir(mocinho)
print(f"Energia Mocinho depois: {mocinho.energia}")

#Teste com um personagem morto
vilao.decremento(vilao.energia) #Vai retirar toda a vida do vilão
mocinho.interagir(vilao)
"""