import random


cpf_gerado = ''

for c in range(0,9):
    numero = str(random.randint(0, 9))
    cpf_gerado += numero

print(cpf_gerado)

contador = int(10)
acumulado = int(0)
for numeros in cpf_gerado:
    # print(numeros)
    numeros_int = int(numeros)
    multiplicando = numeros_int * contador
    acumulado += multiplicando
    # print(f'{numeros_int=}')
    # print(f'{multiplicando=}')
    # print(f'{acumulado=}')
    contador -=1

digito = (acumulado * 10) %11

digito = 0 if digito > 9 else digito

print(f'O primeiro digito do cpf é igual a: {digito}')


cpf_dez_digitos = cpf_gerado + str(digito)


contador = int(11)
acumulado = int(0)
for numeros in cpf_dez_digitos:
    # print(numeros)
    numeros_int = int(numeros)
    multiplicando = numeros_int * contador
    acumulado += multiplicando
    # print(f'{numeros_int=}')
    # print(f'{multiplicando=}')
    # print(f'{acumulado=}')
    contador -=1

segundo_digito = (acumulado * 10) %11
# print(f'{segundo_digito=}')

segundo_digito = 0 if segundo_digito > 9 else segundo_digito

print(f'O segundo digito do cpf é igual a: {segundo_digito}')

cpf_completo = cpf_dez_digitos+str(segundo_digito)

cpf_com_pontos = cpf_completo[:3]+'.'+cpf_completo[3:6]+'.'+cpf_completo[6:9]+'-'+ cpf_completo[9:]

print(f'CPF:{cpf_com_pontos}')
