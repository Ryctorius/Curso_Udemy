import os
while True:
    palavra_secreta = input('Digite a palavra secreta desejada:').strip()
    tamanho_palavra_secreta = len(palavra_secreta)
    palavra_formatada = str('*'*tamanho_palavra_secreta)
    contador_while = 0


    while palavra_formatada != palavra_secreta:
        letra_digitada = input('Digite UMA letra:').strip().lower()
        if len(letra_digitada) >=2:
            print('Digite apenas uma letra')
            continue 
        else:
            contador_for = 0
            for contador_for in range(tamanho_palavra_secreta):
                if palavra_secreta[contador_for] == letra_digitada and contador_for != 0 and contador_for != tamanho_palavra_secreta:
                    palavra_formatada = palavra_formatada[0:contador_for] + letra_digitada + palavra_formatada[contador_for+1 : tamanho_palavra_secreta]
                elif palavra_secreta[contador_for] == letra_digitada and contador_for == 0 :
                    palavra_formatada = letra_digitada + palavra_formatada[contador_for+1 : tamanho_palavra_secreta]
                elif palavra_secreta[contador_for] == letra_digitada and contador_for == tamanho_palavra_secreta:
                    palavra_formatada = palavra_formatada[0 : contador_for] + letra_digitada
            else:
                print(f'Palavra formatada: {palavra_formatada}')
        contador_while += 1
    os.system('clear')
    print(f'Você acertou com {contador_while} tentativas \n')
