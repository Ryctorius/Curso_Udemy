while True:
    frase = str(input('Digite a frase e lhe direi qual a letra que mais se repete e quantas vezes:')).lower()
    total_de_letras = len(frase)
    contador = 0
    while contador < total_de_letras:
        reserva = frase[contador]
        if contador == 0:
            letra_repetida = frase[contador]
            quantidade = frase.count(letra_repetida)
        elif reserva != ' ':
            if quantidade < frase.count(reserva):
                quantidade = frase.count(reserva)
                letra_repetida = reserva
            
        contador += 1   
    
        # quantidade = frase.count('b')


    print(f'A letra que mais apareceu foi a letra "{letra_repetida}" e apareceu {quantidade} vezes.')
