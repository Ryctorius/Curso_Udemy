# CPF TESTE: 746.824.890-70

cpf = '746.824.890-70'

primeiros_numeros_cpf = cpf[:-3]
# print(primeiros_numeros_cpf)
numeros_sem_ponto = primeiros_numeros_cpf.replace('.', '')
# print(numeros_sem_ponto)
contador = int(10)
acumulado = int(0)
for numeros in numeros_sem_ponto:
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


cpf_dez_digitos = numeros_sem_ponto + str(digito)
# print(cpf)

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
print(f'{segundo_digito=}')

segundo_digito = 0 if segundo_digito > 9 else segundo_digito

print(f'O segundo digito do cpf é igual a: {segundo_digito}')

