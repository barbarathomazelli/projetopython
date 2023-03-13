#Exercício #10 - Salário Líquido
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% 
#para o sindicato, faça um programa que nos dê:

#a) quanto pagou de Imposto de Renda.
#b) quanto pagou ao INSS.
#c) quanto pagou ao sindicato.
#d) salário líquido.

vh = float(input('digite quanto voce ganha por hora'))
ht = float(input('digite quantas horas voce trabalha no mes')) 
salario_bruto = vh * ht
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
total_descontos = ir + inss + sindicato
salario_liq = salario_bruto - total_descontos


print('Voce pagou r${:.2f} de imposto de renda'.format(ir))
print('Voce pagou r${:.2f} de inss'.format(inss))
print('Voce pagou r${:.2f} de sindicato'.format(sindicato))
print('Seu salario bruto é de  r${:.2f}'.format(salario_bruto))
print('Seu salario liquido é de r${:.2f}'.format(salario_liq))


