#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Dependendo da letra mostre na tela:Feminino, Masculino ou Sexo Inválido.

sexo = input('Digite [F]- femenino [M]- masculino [H]-homoafetivo \n[T]-transexula [L]-lesbicas [B]-bissexual:').upper()

if sexo == 'M':
    print('sexo masculino')

#verificar(elif) se sexo é f.
elif sexo == 'F':
    print('sexo femenino')

elif sexo == 'H':
    print('homoafetivo')

    #se não for nenhum desses!

else:
    print('Outros')