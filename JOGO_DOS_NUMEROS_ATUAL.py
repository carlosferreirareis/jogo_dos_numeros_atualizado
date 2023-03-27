import math
import time
from tkinter import END

num_jogadores = 0

#Print('Olá Gamer...\nVamos lembrar das regras.\nGanha quem permanecer por último no Game.\nJogador deve jogar um número inédito em cada rodada.\nQuando joga um número que já foi jogado antes, é desclassificado e sai do jogo.\n')

while num_jogadores == 0:
    try:
        # Solicita o número de jogadores ao usuário e cria uma lista vazia para armazenar seus nomes
        num_jogadores = int(input("Digite o número de jogadores: "))      
        if num_jogadores < 2:
            num_jogadores = 0
            print("O número de jogadores deve ser maior que 1.")
    except:
        print("Por favor, digite um número INTEIRO válido.")

range_max = 50
jogadores = []
#***********************************GETPASS(PARA 'SUMIR' COM OS INPUTS************************************************
# Loop para solicitar os nomes dos jogadores e adicioná-los à lista jogadores
for i in range(num_jogadores):
    time.sleep(0.4)
    jogador = input(f"Digite o nome do jogador {i+1}: ")
    jogadores.append(jogador)
# Cria um dicionário com os nomes dos jogadores da lista jogadores e inicializa seus valores em 0
#comentariooooooooooooooooo
dict_jogadores = {idx: jogador for idx, jogador in enumerate(jogadores)}
numeros_jogados = [] #cria lista vazia                     #random para a primeira rodada

for i in range(range_max): # loop para a quantidade maxima de jogadas
    for n in dict_jogadores: #loop para jogador dentro de jogadores onde jogador é a posição do loop
        time.sleep(0.6)
        numerorodada = int(input(f'{dict_jogadores[n].capitalize()} chegou a sua vez de jogar, escolha um número INTEIRO entre 0 e {range_max}:'))
        if numerorodada < 0 or numerorodada > range_max:
            time.sleep(0.4)
            print(f'Você inseriu o caracter,{numerorodada}, que não é válido')
            continue
        if numerorodada in numeros_jogados:
            time.sleep(0.4)
            print(f'{dict_jogadores[n].capitalize()} o número que você escolheu já foi jogado, você foi Eliminado. :( ')
            jogadores.remove(dict_jogadores[n])                                                    #Quando elimina dois em seguida está quebrando em alguns casos, por que?
            num_jogadores = num_jogadores - 1
        if num_jogadores == 1:                                                                               
            time.sleep(2)
            print(f'\n{jogadores[0].capitalize()} Parabéns, VOCÊ GANHOOOOUUUUU!!!')
            break
        numeros_jogados.append(numerorodada)
    dict_jogadores = {idx: jogador for idx, jogador in enumerate(jogadores)}
    if num_jogadores == 1:
        break
    time.sleep(1)    
    print('Vamos iniciar a Próxima Rodada!!')


