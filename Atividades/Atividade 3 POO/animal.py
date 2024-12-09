class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

class Leao(Animal):
    def emitir_som(self):
        return "Roooaaar!"

#Lista de instâncias    
animais = [Cachorro(), Gato(), Leao()]

for animal in animais:
    print(animal.emitir_som())