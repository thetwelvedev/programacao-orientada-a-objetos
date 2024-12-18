from personagens import Personagem, Vilao, Mocinho
from time import sleep

def criar_personagens():
    pass

def mostrar_personagens():
    pass

def iniciar_duelo():
    pass

def realizar_torneio(personagens):
    pass

def alimentar_personagem():
    pass

def interagir_com_personagem():
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