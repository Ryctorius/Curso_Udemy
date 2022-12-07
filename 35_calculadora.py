continuar = 's'
while continuar == 's':
    primeiro_numero = input('Digite o primeiro termo: ')
    segundo_numero = input('Digite o segundo termo: ')
    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
    except:
        print('Você digitou algum numero invalido, tente novamente')
        continue
    operador = input('Digite o operador desejado: + - x /  ')
    if operador == '+':
        calculo = primeiro_numero_float + segundo_numero_float
        print(f'O resultado do cálculo {primeiro_numero} {operador} {segundo_numero} é {calculo}')
    elif operador == '-':
        calculo = primeiro_numero_float - segundo_numero_float  
        print(f'O resultado do cálculo {primeiro_numero} {operador} {segundo_numero} é {calculo}')
    elif operador == 'x':
        calculo = primeiro_numero_float * segundo_numero_float   
        print(f'O resultado do cálculo {primeiro_numero} {operador} {segundo_numero} é {calculo}')
    elif operador == '/':
        calculo = primeiro_numero_float / segundo_numero_float
        print(f'O resultado do cálculo {primeiro_numero} {operador} {segundo_numero} é {calculo}')
    else:
        print('Operador inválido, tente novamente.')
    continuar = input('Deseja continuar?s/n  ').lower().strip()
print('Calculadora desligada')
