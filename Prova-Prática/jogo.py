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
Histório de Batalha:
<Adicionar>""")
        elif(isinstance(personagem, Vilao)): #Vejo se é uma instância de Vilao
            print(f"""Vilão | Nome: {personagem.nome} | Energia: {personagem.energia}
Histório de Batalha:
<Adicionar>""")

def iniciar_duelo(personagens):
    pass

def realizar_torneio(personagens):
    pass

def alimentar_personagem(personagens):
    pass

def interagir_com_personagem(personagens):
    pass

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