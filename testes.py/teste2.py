#Jogo de advinhar!
#Escreva um programa que faça o computador pensar aleatoriamente em um número
#inteiro entre 0 e 10 e peça para o usuário chutar qual foi o número escolhido 
#pelo computador.

#Função randint serve para gerar um numero aleatorio
#modo random importa (import) função (randint) que gera um 
#numero inteiro aleatorio.
#var é computador (randint)vai gerar um numero de 0 a 10.
#var jogador que mostra ao usuario (pensei em um numero inteiro entre 0 a 10).
#\n é para pular linha.
# criaou uma condição if e else que são as var igual a var.
#(print)é para mostrar na tela .

from random import randint

computador  =  randint(0,10)
jogador = int(input('pense em um numero de 0 a 10,... \n'))

if computador  ==  jogador:
    print('Você Ganhou')
else:
    print('Vocẽ Errou! numero é{}')