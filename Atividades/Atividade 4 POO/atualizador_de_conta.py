from conta import Conta, ContaCorrente, ContaPoupanca

class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0.0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta):
        print(f"Saldo anterior da conta {conta._numero}: R${conta.saldo:.2f}")
        conta.atualiza(self._selic)
        print(f"Saldo atualizado da conta {conta._numero}: R${conta.saldo:.2f}")
        self._saldo_total += conta.saldo


# Teste do AtualizadorDeContas
if __name__ == '__main__':
    c = Conta('123-4', 'João', 1000.0)
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    adc = AtualizadorDeContas(0.01)
    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print(f"Saldo total: R${adc.saldo_total:.2f}")
