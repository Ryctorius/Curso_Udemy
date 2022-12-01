numero = input('Digite um número inteiro e lhe direi se é par ou impar:')
# solução if numero.isdigit():
try:
    numero_int = int(numero)
    if (numero_int % 2) == 0:
        print(f'O {numero=} é par')
    else:
        print(f'O {numero=} é impar')
except:
    print(f'{numero} não é um número inteiro')


hora_completa = input('Digite a hora no formato hh:mm : ')
hora_hora = hora_completa[0:2]
# print(hora_hora)
hora_minutos = hora_completa[3:]
# print(hora_minutos)
hora_completa_com_ponto=hora_hora+'.'+hora_minutos
# print(hora_completa_com_ponto)
hora_float = float(hora_completa_com_ponto)

if hora_float < 11.59:
    print('Bom dia')
elif hora_float < 17.59:
    print('Boa tarde')
else:
    print('Boa noite')


nome = input('Digite seu primeiro nome:')
tamanho_nome = len(nome)
if tamanho_nome <=4:
    print('Seu nome é curto')
elif tamanho_nome <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')

