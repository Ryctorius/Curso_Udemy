def multiplicador(*numeros):
    total = 1
    for contador in numeros:
        total *= contador
    return total

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

resposta = True
lista = []
while resposta == True:
    lista.append(int(input('Digite um número :')))
    resposta = continuar()

resultado = multiplicador(*lista)
print(resultado)

