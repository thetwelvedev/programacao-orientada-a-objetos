class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total


# Testando o manipulador
if __name__ == '__main__':
    from conta import ContaCorrente
    from seguro_de_vida import SeguroDeVida

    cc1 = ContaCorrente('123-4', 'João', 1000.0)
    cc2 = ContaCorrente('123-5', 'José', 2000.0)
    seguro1 = SeguroDeVida(100.0, 'José', '345-77')
    seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')

    lista_tributaveis = [cc1, cc2, seguro1, seguro2]

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(f"Total de impostos: R${total:.2f}")
