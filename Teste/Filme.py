class Filme:
    # Inicializador para definir os atributos da classe
    def __init__(self, nome="", ano_de_lancamento=0, incluindo_no_plano=False, duracao_em_minutos=0):
        self.nome = nome
        self.ano_de_lancamento = ano_de_lancamento
        self.incluindo_no_plano = incluindo_no_plano
        self.duracao_em_minutos = duracao_em_minutos
        self.soma_das_avaliacoes = 0
        self.total_de_avaliacoes = 0

    # Getters para acessar os atributos da instância
    def get_nome(self):
        return self.nome

    def get_ano_de_lancamento(self):
        return self.ano_de_lancamento

    def get_incluindo_no_plano(self):
        return self.incluindo_no_plano

    def get_duracao_em_minutos(self):
        return self.duracao_em_minutos

    def get_total_de_avaliacoes(self):
        return self.total_de_avaliacoes

    # Setters para modificar os atributos da instância
    def set_nome(self, nome):
        self.nome = nome

    def set_ano_de_lancamento(self, ano_de_lancamento):
        self.ano_de_lancamento = ano_de_lancamento

    def set_incluindo_no_plano(self, incluindo_no_plano):
        self.incluindo_no_plano = incluindo_no_plano

    def set_duracao_em_minutos(self, duracao_em_minutos):
        self.duracao_em_minutos = duracao_em_minutos

    # Método para exibir a ficha técnica do filme
    def exibe_ficha_tecnica(self):
        print(f"Nome do filme: {self.nome}")
        print(f"Ano de lançamento: {self.ano_de_lancamento}")
        print(f"Duração do filme: {self.duracao_em_minutos} minutos")

    # Método para adicionar uma avaliação
    def avalia(self, nota):
        self.soma_das_avaliacoes += nota
        self.total_de_avaliacoes += 1

    # Método para calcular a média das avaliações
    def pega_media(self):
        if self.total_de_avaliacoes == 0:
            return 0
        return self.soma_das_avaliacoes / self.total_de_avaliacoes
