from tributavel import TributavelMixIn

class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 42 + self._valor * 0.05

    def __str__(self):
        return f"Seguro de Vida | Titular: {self._titular} | Valor: R${self._valor:.2f} | Apólice: {self._numero_apolice}"
