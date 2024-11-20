class Historico:
    def __init__(self):
        self.transacoes = []

    def adiciona_transacao(self, descricao):
        self.transacoes.append(descricao)

    def exibe_historico(self):
        print("Histórico de transações:")
        for i, transacao in enumerate(self.transacoes):
            print(f"{i+1}. {transacao}")

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Conta:
    def __init__(self, numero, titular, saldo, limite, data):
        self.numero = numero
        self.titular = titular # Instância de Cliente 
        self.saldo = saldo
        self.limite = limite
        self.data = data # Instância de Data
        self.historico = Historico()

    def deposita(self, valor)-> None:
        self.saldo += valor

    def saca(self, valor)-> None:
        self.saldo -= valor
    
    def extrato(self)-> None:
        print(f"Nome: {self.titular.nome} {self.titular.sobrenome}\nCPF: {self.titular.cpf}\nNúmero: {self.numero} \nSaldo: R$ {self.saldo:.2f}")

    def saca(self, valor) -> bool:
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
        
    def transfere_para(self, destino, valor) -> bool:
        if self.saca(valor):
            destino.deposita(valor)
            self.historico.adiciona_transacao(
                f"Transferência de R$ {valor:.2f} para a conta {destino.numero} de {destino.titular.nome} {destino.titular.sobrenome}."
            )
            destino.historico.adiciona_transacao(
                f"Recebimento de transferência de R$ {valor:.2f} da conta {self.numero} de {self.titular.nome} {self.titular.sobrenome}."
            )
            return True
        else:
            return False
        
    def data_abertura(self, data) -> None:
        print(f"Data de abertura: {self.data.dia:02d}/{self.data.mes:02d}/{self.data.ano}")

if __name__ == '__main__':
    #Passando os clientes
    cliente1 = Cliente("Leonardo", "Castro", "123.456.789-00")
    cliente2 = Cliente("Maria", "Santos", "987.654.321-00")

    data1 = Data(1, 2, 2024)
    data2 = Data(31, 12, 2022)

    conta1 = Conta('121-2', cliente1, 2000.0, 3000.0, data1)
    conta2 = Conta('121-3', cliente2, 1500.0, 2000.0, data2)

    #print(type(conta))
    #print(conta.numero)
    #print(conta.titular)
    conta1.extrato()
    conta1.data_abertura(data1)
    print("-"*20)
    conta2.extrato()
    conta2.data_abertura(data2)
    print("-"*20)
    conta1.deposita(200)
    conta1.extrato()
    print("-"*20)
    conta2.saca(100)
    conta2.extrato()
    print("-"*20)
    conta1.transfere_para(conta2, 1000)
    conta2.extrato()
    print("-"*20)
    conta1.extrato()
    print("-"*20)
    conta1.historico.exibe_historico()
    print("-"*20)
    conta2.historico.exibe_historico()

"""
12- Podemos criar uma Conta sem um Cliente ? Não, pois é obrigatório ter um titular que no caso é a instância de cliente
E um Cliente sem uma Conta ? Pois ele pois não tem dependencia da classe Conta
14- Faz sentido criar um objeto do tipo Historico sem uma Conta? Não, pois precisa do histórico de transações de conta
"""