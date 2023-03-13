#Faça um Programa que leia três números inteiros 
#e mostre o maior e o menor deles.


# pedir para o usuario inserir(input) e (int) é numero inteiro.
num1 = int(input('Digite primeiro  numero'))
num2 = int(input('Digite segundo numero'))
num3 = int(input('Digite terceiro numero'))

#(var) maior 2 e 3
maior = num1
menor = num2

# temos aqui as seguintes condições:

# condição (if) - (var) maior 2 e 3
if num2 > maior:
    maior = num2

    if num3 > maior:
       maior = num3


       # condição (if)  - (var) menor 2 e 3
       if num2 < menor:
          menor = num2

    if num3 < menor:
       menor = num3

# mostrando ao usuario!
print ('O maior numero digitado foi {} e o menor {}'.format(maior,menor,))

#O programa vai mostrar ao usuario o numero m aior e o menor.