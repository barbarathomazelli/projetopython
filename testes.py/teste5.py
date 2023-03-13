#Faça um Programa que peça um valor e mostre na 
#tela se o valor é positivo ou negativo.

#usando comando (float, numeros com . ex:2.5, 3.9 ou -4.8, -7.1,)
#ou seja, digitando dessa forma teremos o resultado negativo ou positivo.

num = float(input('Digite um valor'))

if num >= 0:
    print('Este numero é {} positivo'.format(num))

else:
    print('Este numero é {} negativo'.format(num))