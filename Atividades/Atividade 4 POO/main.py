from tributavel import Tributavel
from conta import Conta, ContaCorrente, SeguroDeVida
from manipulador_tributaveis import ManipuladorDeTributaveis

# Registrar classes como subclasses virtuais de Tributavel
Tributavel.register(ContaCorrente)
Tributavel.register(SeguroDeVida)

# Criar objetos
cc = ContaCorrente("João", "123-4")
cc.deposita(1000.0)

seguro = SeguroDeVida(100.0, "José", "345-77")

# Teste direto
print(cc.get_valor_imposto())  # Output: 10.0
print(seguro.get_valor_imposto())  # Output: 55.0

# Lista de tributáveis
lista_tributaveis = [cc, seguro]

# Manipulador de tributáveis
mt = ManipuladorDeTributaveis()
total = mt.calcula_impostos(lista_tributaveis)
print(total)  # Output: 65.0

# Teste com ContaPoupanca
class ContaPoupanca(Conta):
    pass

cp = ContaPoupanca("Maria", "123-6")
lista_tributaveis.append(cp)
total = mt.calcula_impostos(lista_tributaveis)
print(total)  # Output: 65.0 (ContaPoupanca não é tributável)

# Teste com ContaInvestimento
class ContaInvestimento(Conta):
    def get_valor_imposto(self):
        return self._saldo * 0.03

Tributavel.register(ContaInvestimento)

ci = ContaInvestimento("Carlos", "789-0")
ci.deposita(5000.0)
lista_tributaveis.append(ci)
total = mt.calcula_impostos(lista_tributaveis)
print(total)  # Output: 215.0 (10 + 55 + 150)
