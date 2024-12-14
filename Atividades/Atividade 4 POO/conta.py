from tributavel import Tributavel

class Conta:
    def __init__(self, titular, numero):
        self._titular = titular
        self._numero = numero
        self._saldo = 0.0

    def deposita(self, valor):
        self._saldo += valor

    def __repr__(self):
        return f"Conta(numero={self._numero}, titular={self._titular}, saldo={self._saldo})"

class ContaCorrente(Conta):
    def get_valor_imposto(self):
        return self._saldo * 0.01

class SeguroDeVida:
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

    def __repr__(self):
        return f"SeguroDeVida(valor={self._valor}, titular={self._titular}, numero_apolice={self._numero_apolice})"

class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

    def __str__(self):
        return f"Conta {self._numero} | Titular: {self._titular} | Saldo: R${self._saldo:.2f}"


class ContaCorrente(Conta, Tributavel):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10

    def get_valor_imposto(self):
        return self._saldo * 0.01


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


if __name__ == '__main__':
    c = Conta('123-4', 'João', 1000.0)
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(c)
    print(cc)
    print(cp)
