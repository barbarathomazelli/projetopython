#Crie um Programa que peça 2 notas de prova de um aluno e calcule a sua média semestral.

nota_1 = float(input('Digite a primeira nota:'))
nota_2 = float(input('Digite a segunda nota:'))
nota_3 = float(input('Digite a terceira nota:'))
nota_4 = float(input('Digite a quarta nota:'))

#Para mostrar o numero de casas decimais 
# #usamos o round e informamos 1 nesse caso!Observe no final da linha abaixo!
media = round((nota_1 + nota_2 + nota_3 + nota_4)/ 4,1)
print('A media do aluno é {}'.format(media))


