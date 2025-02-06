class LivroIndisponivelError(Exception):
    def __init__(self, titulo_livro, motivo):
        self.titulo_livro = titulo_livro
        self.motivo = motivo
        super().__init__(f"O livro '{self.titulo_livro}' não pode ser emprestado: {self.motivo}.")

class DevolucaoInvalidaError(Exception):
    def __init__(self, nome_usuario, titulo_livro):
        self.nome_usuario = nome_usuario
        self.titulo_livro = titulo_livro
        super().__init__(f"Usuário {self.nome_usuario} tentou devolver '{self.titulo_livro}', mas ele não pegou esse livro emprestado.")

class EmprestimoAtrasadoError(Exception):
    def __init__(self, nome_usuario, titulo_livro, dias_atraso):
        self.nome_usuario = nome_usuario
        self.titulo_livro = titulo_livro
        self.dias_atraso = dias_atraso
        self.multa = dias_atraso * 2.50
        super().__init__(f"Usuário {self.nome_usuario} atrasou a devolução de '{self.titulo_livro}' em {self.dias_atraso} dias. Multa de {self.multa:.2f} reais aplicada.")

class Biblioteca:
    def __init__(self):
        self.livros_disponiveis = {"Python para Iniciantes": True, "Machine Learning Básico": True, "Python Avançado": True}
        self.emprestimos = {}
        self.reservas = {}
    
    def emprestar_livro(self, usuario, titulo_livro):
        if not isinstance(titulo_livro, str):
            raise TypeError("O título do livro deve ser uma string.")
        if titulo_livro in self.reservas:
            raise LivroIndisponivelError(titulo_livro, "já está reservado para outro usuário")
        if titulo_livro in self.emprestimos:
            raise LivroIndisponivelError(titulo_livro, "já está emprestado para outro usuário")
        
        self.emprestimos[titulo_livro] = usuario
        self.livros_disponiveis[titulo_livro] = False
        print(f"{usuario} emprestou '{titulo_livro}'.")
    
    def devolver_livro(self, usuario, titulo_livro, dias_atraso=0):
        if titulo_livro not in self.emprestimos or self.emprestimos[titulo_livro] != usuario:
            raise DevolucaoInvalidaError(usuario, titulo_livro)
        
        del self.emprestimos[titulo_livro]
        self.livros_disponiveis[titulo_livro] = True
        
        if dias_atraso > 0:
            raise EmprestimoAtrasadoError(usuario, titulo_livro, dias_atraso)
        
        print(f"{usuario} devolveu '{titulo_livro}'.")
    
    def reservar_livro(self, usuario, titulo_livro):
        if titulo_livro in self.reservas:
            raise LivroIndisponivelError(titulo_livro, "já está reservado para outro usuário")
        
        self.reservas[titulo_livro] = usuario
        print(f"{usuario} reservou '{titulo_livro}'.")

#Testes
biblioteca = Biblioteca()

#Livro já emprestado
try:
    biblioteca.emprestar_livro("João", "Python para Iniciantes")
    biblioteca.emprestar_livro("Maria", "Python para Iniciantes")
except LivroIndisponivelError as e:
    print(e)
except Exception:
    print("Erro inesperado! Por favor, entre em contato com a administração da biblioteca.")

#Livro não foi emprestado por Carlos
try:
    biblioteca.devolver_livro("Carlos", "Python Avançado")
except DevolucaoInvalidaError as e:
    print(e)
except Exception:
    print("Erro inesperado! Por favor, entre em contato com a administração da biblioteca.")

#Livro já reservado
try:
    biblioteca.reservar_livro("Ana", "Python para Iniciantes")
    biblioteca.reservar_livro("Pedro", "Python para Iniciantes")
except LivroIndisponivelError as e:
    print(e)
except Exception:
    print("Erro inesperado! Por favor, entre em contato com a administração da biblioteca.")

#Passando um número ao invés do título
try:
    biblioteca.emprestar_livro("Lucas", 12345)
except TypeError as e:
    print(e)
except Exception:
    print("Erro inesperado! Por favor, entre em contato com a administração da biblioteca.")

#Devolução atrasada
try:
    biblioteca.devolver_livro("João", "Python para Iniciantes", dias_atraso=5) 
except EmprestimoAtrasadoError as e:
    print(e)
except Exception:
    print("Erro inesperado! Por favor, entre em contato com a administração da biblioteca.")
