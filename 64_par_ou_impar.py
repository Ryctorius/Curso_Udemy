def continuar():
    while True:
        resposta = input('deseja continuar? [s]-sim [n]-não  ').strip().lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print('Resposta incorreta, tente novamente!')
            continue

def par_impar(numero):
    try:
        numero = int(numero)
        resto = numero % 2
        if resto == 1:
            print(f'O numero {numero} é ÍMPAR!')
        else:
            print(f'O numero {numero} é PAR!')
    except(ValueError):
        print('O valor digitado não é um número')
    



resposta = True
while resposta == True:
    numero = input('Digite um número:')
    par_impar(numero)
    resposta = continuar()
