# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar

numero_str = input('Vou dobrar o numero que voce digitar:')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('STR:', numero_float)
    print(f'O dobro de {numero_float} é {numero_float*2}')
except:
    print('Isso não é um número')
