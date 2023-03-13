#Crie um programa que peça dois números para o usuário e a operação que ele 
#queira realizar e mostre o resultado da conta na tela

num1 = float(input('Digite primeiro numero:'))
num2 = float(input('Digite segundo numero:'))
op = input('Digite \n[+] = Adição \n[-] = Subtração \n[*] = Multiplicação \n[/] = Divisão \n')

if op not in '+,-,*,/':
    print('operação invalida')
else:
    if op == '+':
        conta = num1 + num2
    elif op == '-':
        conta = num1 - num2
    elif op  == '*':
        conta = num1 * num2
    elif op == '/':
        conta = num1 / num2
        print('{: .if}'.format(conta))
