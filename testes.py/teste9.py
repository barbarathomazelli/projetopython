#Faça um Programa que pergunte em que turno o usuário estuda. 
#Peça para digitar M-matutino, V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", 
#"Boa Tarde! ", "Boa Noite!" 
#ou "Valor Inválido!", conforme o caso.


print('[M] = matutino')
print('[V] = vespertino')
print('[N] = noturno')

turno = input('Digite a letra correspondente ao periodo que voce estuda:').lower()

if turno == 'm':
   print('Bom dia!')

elif turno == 't':
    print('Boa tarde!')

elif turno == 'n':
    print('Boa noite!')

else:
    print('Inválido')

