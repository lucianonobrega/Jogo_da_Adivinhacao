from random import randint
from time import sleep
#Criação de variáveis para serem usadas nos loopings, com o intúito de pará-los.
a = b = d = 0
tentativas = 0
#Inicialização do jogo.
while a == 0:
    iniciar = str(input("Deseja iniciar o jogo?[s/n]: ")).lower()
    #Se responder 's' o jogo começa.
    if iniciar == "s":
        print("iniciando...")
        sleep(2)
        #Tela de apresentação.
        print("-" * 23)
        print("| Jogo da Adivinhação |")
        print("-" * 23)
        sleep(2)
        while b == 0:
            #Escolha de um número de 0 até 100 pela cpu, utilizando o módulo random.
            cpu = randint(0,100)
            print("CPU: Estou pensando em um número de 0 até 100.\nConsegue adivinhar? ;)")
            sleep(2)
            #Faz com que o looping c funcione.
            c = 0
            while c == 0:
                #Vai tentar executar tudo o que está identado (dentro).
                try:
                    #Palpite do jogador, escolhendo um número de 0 até 100.
                    jogador = int(input("Palpite:"))
                    #Condicional para manter o jogador escolhendo apenas números de 0 até 100.
                    if jogador >= 0 and jogador <= 100:
                        if jogador == cpu:
                            tentativas += 1
                            print(f"Parabéns! Você acertou!\nNúmero de tentativas: {tentativas}.")
                            sleep(2)
                            while d == 0:
                                #Possibilita encerrar o código ou manter o jogador jogando quantas vezes quiser.
                                continuar = str(input("Deseja continuar o jogo?[s/n]: ")).lower()
                                # Se responder 's' o jogo continua.
                                if continuar == "s":
                                    print("CPU:Tudo bem! Vamos jogar mais uma!")
                                    tentativas = 0
                                    #c = 1 faz com que o looping do while c seja quebrado, fazendo com que o while b seja o primeiro.
                                    c = 1
                                    sleep(1)
                                    break
                                # Se responder 'n' o jogo encerra.
                                elif continuar == "n":
                                    print("Encerrando...")
                                    sleep(2)
                                    a = b = c = d = 1
                                # Se digitar errado, uma mensagem aparecerá mostrando quais opções são válidas.
                                else:
                                    print("Opção inválida. Digite apenas 's' para sim e 'n' para não.")
                                    sleep(2)
                        elif jogador > cpu:
                            tentativas += 1
                            print(f"O número {jogador} é maior do que o que estou pensando!")
                            sleep(1)
                        elif jogador < cpu:
                            tentativas += 1
                            print(f"O número {jogador} é menor do que o que estou pensando!")
                            sleep(1)
                    #Alerta caso o jogador faça uma jogada fora do alcance de 0 até 100.
                    else:
                        tentativas += 1
                        print(f"O número {jogador} está fora do alcance de 0 até 100!!!")
                        sleep(1)
                #Se não conseguir executar tudo que está identado, vai mostrar a mensagem abaixo.
                except:
                    print("O dado fornecido não é um número inteiro!")
                    sleep(1)
    #Se responder 'n' o jogo encerra.
    elif iniciar == "n":
        print("Encerrando...")
        sleep(2)
        break
    #Se digitar errado, uma mensagem aparecerá mostrando quais opções são válidas.
    else:
        print("Opção inválida. Digite apenas 's' para sim e 'n' para não.")
        sleep(2)