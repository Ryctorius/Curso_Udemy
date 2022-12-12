palavra_secreta = input('Digite a palavra secreta desejada:').strip()
palavra_formatada = str('*'*len(palavra_secreta))
contador_while = 0


while palavra_formatada != palavra_secreta:
    letra_digitada = input('Digite UMA letra:').strip().lower()
    if len(letra_digitada) >=2:
        print('Digite apenas uma letra')
        continue 
    else:
        contador_for = 0
        for letra in palavra_secreta:
            print(letra)
            if letra == letra_digitada:
                
           
        else:
            print(f'Palavra formatada: {palavra_formatada}')
    contador_while += 1
print(f'Você acertou com {contador_while} tentativas')