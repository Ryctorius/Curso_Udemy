def duplicar(numero):
    duplicado = numero *2
    return duplicado

def triplicar(numero):
    triplicado = numero *3
    return triplicado
    
def quadruplicar(numero):
    quadruplicado = numero *4
    return quadruplicado

def is_number(numero):
    try:
        numero = float(numero)
        return numero
    except(ValueError):
        print('O valor digitado não é um número')
        quit()
    
def continuar():
    while True:
        resposta = input('\n\nDeseja continuar? [s]-sim [n]-não  ').strip().lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print('Resposta incorreta, tente novamente!')
            continue

resposta = True
while resposta == True:
    numero = input('Digite um número:')
    numero_float = is_number(numero)
    numero_duplicado =duplicar(numero_float)
    numero_triplicado =triplicar(numero_float)
    numero_quadruplicado =quadruplicar(numero_float)
    
    print(f'O número {numero} duplicado é igual a {numero_duplicado}, triplicado é igual a {numero_triplicado} e quadruplicado é igual a {numero_quadruplicado}')
    resposta = continuar()
