import os
resposta = 'Inicio'
lista_de_compras = []

print('Seja bem vindo(a) ao aplicativo LISTA DE COMPRAS!!!\n')
while resposta != 's':
    resposta = input('Selecione uma opção: \n [i]nserir  [a]pagar  [l]istar [s]air: ').lower().strip()
    if resposta == 's':
        os.system('clear')
        print('\n Saindo da lista de compras. Obrigado por utilizar nosso aplicativo.')
        continue
    elif resposta == 'i':
        produto = input('Qual o produto você deseja inserir na sua lista de compras?\n').capitalize().strip()
        if produto in lista_de_compras:
            os.system('clear')
            print('Esse produto já consta na lista de compras.\n')
        else:
            lista_de_compras.append(produto)
        continue
    elif resposta == 'l':
        os.system('clear')
        for indice, nome_produto in enumerate(lista_de_compras):
            print(indice , '-' , nome_produto)
        if lista_de_compras == []:
            print('Não há nenhum item na lista de compras!\n')

    elif resposta == 'a':
        item_apagar = input('Digite o código ou o nome do item que deseja apagar: ').capitalize().strip()
        try:
            item_apagar_int = int(item_apagar)
            for indice, nome_produto in enumerate(lista_de_compras):
                if indice == item_apagar_int:
                    del lista_de_compras[indice]                 
        except :
            for indice, nome_produto in enumerate(lista_de_compras):
                if nome_produto == item_apagar:
                    del lista_de_compras[indice]
                  
    else:
        os.system('clear')
        print('Resposta inválida, tente novamente!')
        continue
