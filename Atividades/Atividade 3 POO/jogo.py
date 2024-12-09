class Cavaleiro:
    def atacar(self):
        return "Cavaleiro ataca com sua espada"
    
class Mago:
    def atacar(self):
        return "Mago ataca com sua magia"
    
class Dragao:
    def atacar(self):
        return "Dragão ataca com fogo"
    
def executar_ataque(lista_de_personagens):
    for personsagem in lista_de_personagens:
        print(personsagem.atacar())

# Instâncias das classes
cavaleiro = Cavaleiro()
mago = Mago()
dragao = Dragao()

# Testando a função
personagens = [cavaleiro, mago, dragao]
executar_ataque(personagens)