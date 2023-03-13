#Faça um Programa que peça um número 
#inteiro e determine se ele é par ou ímpar.

num = int(input('Digite par'))


#condição é a seguinte:
#se o (operador de modo-- %) resto da divisão for igual a 0
if num % 2 == 0:
    #mostrar para o usuario quando digitar o numero  se é impar ou par
    print('O numero  {} é par '.format(num))
    
else:
        print('O numero  {} é impar '.format(num))