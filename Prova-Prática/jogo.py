from personagens import Personagem, Vilao, Mocinho
from time import sleep
from random import shuffle

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
            print(f"""\nMocinho | Nome: {personagem.nome} | Energia: {personagem.energia}
Histório de Batalha:""")
            for batalha in personagem.historico_batalhas:#Vai imprimir cada batalha desse personagem
                print(batalha)
        elif(isinstance(personagem, Vilao)): #Vejo se é uma instância de Vilao
            print(f"""\nVilão | Nome: {personagem.nome} | Energia: {personagem.energia}
Histório de Batalha:""")
            for batalha in personagem.historico_batalhas:#Vai imprimir cada batalha desse personagem
                print(batalha)

def iniciar_duelo(personagens):
    #Separei a lista em duas, uma para cada classe
    mocinhos = [p for p in personagens if isinstance(p, Mocinho)]
    viloes = [p for p in personagens if isinstance(p, Vilao)]

    print("\n>>>>> Escolhendo Personagens para o Duelo <<<<<\n")
    if mocinhos and viloes: #Para haver a luta é necessário ter pelo menos um vilão e um mocinho, logo se uma das listas acima tiver vazia não haverá duelo
        print("\n>>>>>>>>>> Escolha o Mocinho <<<<<<<<<<") #Aqui assim como em outras funções vai selecionar um dos mocinhos na lista através do indice
        for i, mocinho in enumerate(mocinhos):
            print(f"{i+1}. {mocinho.nome}")

        mocinho_escolhido = int(input("Escolha o número do Mocinho: ")) 
        mocinho = mocinhos[mocinho_escolhido - 1]

        print("\n>>>>>>>>>> Escolha o Vilão <<<<<<<<<<") #Aqui assim como em outras funções vai selecionar um dos vilões na lista através do indice
        for i, vilao in enumerate(viloes):
            print(f"{i+1}. {vilao.nome}")

        vilao_escolhido = int(input("Escolha o número do Vilão: ")) 
        vilao = viloes[vilao_escolhido - 1]

        mocinho.lutar(vilao) #Realiza o duelo de fato
        sleep(2) 
        print("\n>>>>>>>>>> Resultado do Duelo <<<<<<<<<<")
        print(f"{mocinho.nome} | Energia: {mocinho.energia}")
        print(f"{vilao.nome} | Energia: {vilao.energia}")
    else:
        print("Não tem persongens suficientes para o duelo.")

def realizar_torneio(personagens):
    participantes = personagens[:] #Faz uma copia da lista pois logo abaixo vamos embaralhar ela e com essa copia não afeta a lista original
    shuffle(participantes)  #Como o próprio nome já diz ela embaralha a lista

    print("\n>>>>>>>>>>>> Torneio Iniciado <<<<<<<<<<<<")
    while len(participantes) > 1: #Para ter o torneio tem que ter pelo menos 2 personagens
        vencedores = [] #Armazena o vencedor por rodada

        for i in range(0, len(participantes), 2): #Vai indo de 2 em dois pois sempre são pares nas lutas
            personagem1 = participantes[i]
            personagem2 = participantes[i + 1]
            print(f"\nBatalha entre {personagem1.nome} e {personagem2.nome}")
            personagem1.lutar(personagem2)
            if personagem1.energia > personagem2.energia:
                vencedores.append(personagem1)  # Adiciona o vencedor
                print(f"Vencedor: {personagem1.nome}")
            else:
                vencedores.append(personagem2)
                print(f"Vencedor: {personagem2.nome}")
        
        #Caso o número de participantes seja ímpar, o último participante avança
        if len(participantes) % 2 != 0:
            vencedor_por_wo = participantes[-1]
            vencedores.append(vencedor_por_wo)
            print(f"\n{vencedor_por_wo.nome} avançou para a próxima rodada por WO!")

        participantes = vencedores  #Atualiza a lista com só com os vencedores

    vencedor = participantes[0]  #Quando restar apenas um, ele é o campeão
    print(f"\nVencedor do Torneio: {vencedor.nome} com energia {vencedor.energia}")
    print("Histórico completo das batalhas:")
    for batalha in vencedor.historico_batalhas:
        print(batalha)

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
                escolha = int(input("Escolha o número do vilão: "))
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