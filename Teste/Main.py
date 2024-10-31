from Filme import Filme
# Importando a classe Filme do módulo Filme.py
# Usamos "from Filme import Filme" para acessar a classe Filme diretamente
# dentro do script. Dessa forma, podemos criar uma instância de Filme sem 
# precisar referenciar o módulo.

# Instanciando um objeto da classe Filme
meu_filme = Filme()  # Criação do objeto Filme

# Atribuindo valores ao objeto
meu_filme.set_nome("O poderoso chefão")
meu_filme.set_ano_de_lancamento(1970)
meu_filme.set_duracao_em_minutos(180)

# Chamando o método para exibir a ficha técnica
meu_filme.exibe_ficha_tecnica()

# Avaliações
meu_filme.avalia(8)
meu_filme.avalia(5)
meu_filme.avalia(10)

# Exibindo o total de avaliações e a média
print("Total de avaliações:", meu_filme.get_total_de_avaliacoes())
print("Média das avaliações:", meu_filme.pega_media())