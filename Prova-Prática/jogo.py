from personagens import Personagem, Vilao, Mocinho
from time import sleep

def criar_personagens(personagens):
    print("""\n>>>>>>>>>> Escolha o Personagem <<<<<<<<<<
1. Mocinho
2. Vilão
3. Voltar
""")
    opcao = input("Escolha uma opção: ")
    match opcao:
            case "1": #Aqui eu pego o nome, instâncio o personagem e coloco ele na lista personagens
                print("\n>>>>>>>>>> Mocinho selecionado <<<<<<<<<<")
                nome = str(input("Digite o nome do personagem: "))
                personagem = Mocinho(nome)
                personagens.append(personagem)
            case "2":
                print("\n>>>>>>>>>>> Vilão selecionado <<<<<<<<<<<")
                nome = str(input("Digite o nome do personagem: "))
                personagem = Vilao(nome)
                personagens.append(personagem)
            case "3":
                return

def mostrar_personagens(personagens):
    for personagem in personagens: #Vou percorrer a lista com o personagens mas vou separar Classe
        if(isinstance(personagem, Mocinho)): #Vejo se é uma instância de Mocinho
            print(f"""Mocinho | Nome: {personagem.nome} | Energia: {personagem.energia}
Histório de Batalha:""")
            for batalha in personagem.historico_batalhas:#Vai imprimir cada batalha desse personagem
                print(batalha)
        elif(isinstance(personagem, Vilao)): #Vejo se é uma instância de Vilao
            print(f"""Vilão | Nome: {personagem.nome} | Energia: {personagem.energia}
Histório de Batalha:""")
            for batalha in personagem.historico_batalhas:#Vai imprimir cada batalha desse personagem
                print(batalha)

def iniciar_duelo(personagens):
    pass

def realizar_torneio(personagens):
    pass

def alimentar_personagem(personagens):
    print("""\n>>>>>>>>>> Escolha o Personagem <<<<<<<<<<
1. Mocinho
2. Vilão
3. Voltar
""")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1": #Quando for mocinho
            mocinhos = [p for p in personagens if isinstance(p, Mocinho)] #Cria uma lista só com os Mocinhos
            if mocinhos: #Se a lista tiver vazia vai ser False e não vai executar
                print("\n>>>>>>>>>> Escolha o Mocinho <<<<<<<<<<")
                for i, mocinho in enumerate(mocinhos): #Vai listar os Mocinhos
                        print(f"{i+1}. {mocinho.nome}")
                escolha = int(input("Escolha o número do mocinho: "))
                personagem_selecionado = mocinhos[escolha - 1] #Pois o índice começa em zero
                personagem_selecionado.alimentar() #Aqui vai realizar a função Alimenatar no mocinho
            else: 
                print("Não tem mocinhos!")
        case "2": #Quando dor vilão
            viloes = [p for p in personagens if isinstance(p, Vilao)] #Cria uma lista só com os Viloes
            if viloes: #Se a lista tiver vazia vai ser False e não vai executar
                print("\n>>>>>>>>>> Escolha o Vilão <<<<<<<<<<")
                for i, vilao in enumerate(viloes): #Vai listar os Vilões
                        print(f"{i+1}. {vilao.nome}")
                escolha = int(input("Escolha o número do mocinho: "))
                personagem_selecionado = viloes[escolha - 1] #Pois o índice começa em zero
                personagem_selecionado.alimentar() #Aqui vai realizar a função Alimenatar no vilão
            else: 
                print("Não tem vilões!")
        case "3":
            return

def interagir_com_personagem(personagens):
    print("""\n>>>>>>>>>> Escolha o Personagem para Interagir <<<<<<<<<<
1. Mocinho
2. Vilão
3. Voltar
""")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1": #Quando for mocinho
            mocinhos = [p for p in personagens if isinstance(p, Mocinho)] #Cria uma lista só com os Mocinhos
            if mocinhos: #Se a lista tiver vazia vai ser False e não vai executar
                print("\n>>>>>>>>>> Escolha o Mocinho <<<<<<<<<<")
                for i, mocinho in enumerate(mocinhos): #Vai listar os Mocinhos
                        print(f"{i+1}. {mocinho.nome}")
                escolha = int(input("Escolha o número do mocinho: "))
                personagem_selecionado = mocinhos[escolha - 1] #Pois o índice começa em zero
                #Escolhendo o personagem para interagir
                print("\n>>>>>>>>>> Escolha o Personagem <<<<<<<<<<")
                personagens_excluindo_selecionado = [p for p in personagens if p != personagem_selecionado] #Assim seleciona um personagem sem incluir o personagem selecioando
                for i, p in enumerate(personagens_excluindo_selecionado):
                    print(f"{i+1}. {p.nome}")
                interacao_escolha = int(input("Escolha o número do personagem: "))
                outro_personagem = personagens_excluindo_selecionado[interacao_escolha - 1]
                personagem_selecionado.interagir(outro_personagem)  #Aqui tem interação entre um morcinho e um personagem qualquer
            else:
                print("Não tem mocinhos!")
        
        case "2": #Quando dor vilão
            viloes = [p for p in personagens if isinstance(p, Vilao)] #Cria uma lista só com os Viloes
            if viloes: #Se a lista tiver vazia vai ser False e não vai executar
                print("\n>>>>>>>>>> Escolha o Vilão <<<<<<<<<<")
                for i, vilao in enumerate(viloes): #Vai listar os Vilões
                        print(f"{i+1}. {vilao.nome}")
                escolha = int(input("Escolha o número do mocinho: "))
                personagem_selecionado = viloes[escolha - 1] #Pois o índice começa em zero
                #Escolhendo o personagem para interagir
                print("\n>>>>>>>>>> Escolha o Personagem <<<<<<<<<<")
                personagens_excluindo_selecionado = [p for p in personagens if p != personagem_selecionado] #Assim seleciona um personagem sem incluir o personagem selecioando
                for i, p in enumerate(personagens_excluindo_selecionado):
                    print(f"{i+1}. {p.nome}")
                interacao_escolha = int(input("Escolha o número do personagem: "))
                outro_personagem = personagens_excluindo_selecionado[interacao_escolha - 1]
                personagem_selecionado.interagir(outro_personagem)  #Aqui tem interação entre um vilao e um personagem qualquer
            else:
                print("Não tem vilões!")
        
        case "3":
            return


def menu():
    personagens = []  #Vai armazenar todos os personagens
    
    while True:
        print("\n>>>>>>>>>>>> Menu Principal <<<<<<<<<<<<")
        print("1. Criar personagens (mocinhos e vilões)")
        print("2. Mostrar personagens criados")
        print("3. Iniciar um duelo entre um mocinho e um vilão")
        print("4. Realizar torneios entre múltiplos personagens")
        print("5. Alimentar um mocinho ou vilão")
        print("6. Interagir (conversar ou desafiar outro personagem)")
        print("7. Sair do jogo")
        
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                criar_personagens(personagens)
            case "2":
                mostrar_personagens(personagens)
            case "3":
                iniciar_duelo(personagens)
            case "4":
                realizar_torneio(personagens)
            case "5":
                alimentar_personagem(personagens)
            case "6":
                interagir_com_personagem(personagens)
            case "7":
                print("Saindo do jogo...")
                sleep(1)
                print("Em...")
                sleep(1)
                print("3...")
                sleep(1)
                print("2...")
                sleep(1)
                print("1...")
                sleep(1)
                print("            JOGO ENCERRADO!            ")
                break
            case _:
                print("Opção inválida, escolha uma opção válida(1-6).")

#Execução
menu()