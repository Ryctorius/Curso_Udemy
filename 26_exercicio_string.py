nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

if nome != '' and idade != '':
   
    tamanho_nome = len(nome)
    nome_invertido = nome[-1:-(tamanho_nome+1):-1]
       
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' 'in nome:
        print('Seu nome contém espaços')
        tamanho_nome=tamanho_nome-1
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {tamanho_nome} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')


else:
    print('Desculpe, você deixou campos vazios')