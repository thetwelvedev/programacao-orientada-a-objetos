from abc import ABC, abstractmethod
class ElectronicDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def perform_operation(self):
        pass
    
class Smartphone(ElectronicDevice):
    def __init__(self, remetente, destinatario):
        self.remetente = remetente
        self.destinatario = destinatario
        
    def turn_on(self):
        return print("Ligou o Smartphone")

    def turn_off(self):
        return print("Desligou o Smartphone")

    def perform_operation(self):
        return print(f"{self.remetente} enviou uma mensagem para {self.destinatario}")

class Television(ElectronicDevice):
    def __init__(self, canal):
        self.canal = canal
        
    def turn_on(self):
        return print("Ligou a TV")

    def turn_off(self):
        return print("Desligou a TV")
    
    def perform_operation(self):
        return print(f"Mudou para o canal {self.canal}")


if __name__ == "__main__":
    celular = Smartphone("Ben", "Gwen")
    sbt = Television("SBT")

    objects = [celular, sbt]

    for obj in objects:
        obj.turn_on()
        obj.turn_off()
        obj.perform_operation()

    #x = ElectronicDevice()