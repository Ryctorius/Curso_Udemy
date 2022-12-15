# inserir apagar listar
resposta = 'Inicio'
lista_de_compras = list([])


while resposta != 's':
    resposta = input('Selecione uma opção: \n [i]nserir  [a]pagar  [l]istar [s]air: ').lower().strip()
    if resposta == 's':
        print('Saindo da lista de compras. Obrigado por utilizar nosso aplicativo.')
        continue
    elif resposta == 'i':
        produto = input('Qual o produto você deseja inserir na sua lista de compras?').capitalize().strip()
        if produto in lista_de_compras:
            print('Esse produto já consta na lista de compras')
        else:
            lista_de_compras.append(produto)
        continue
    elif resposta == 'l':
        for indice, nome_produto in enumerate(lista_de_compras):
            print(indice , '-' , nome_produto)

#    -----------------AJUSTAR AQUI -------------------
    # elif resposta == 'a':
    #     item_apagar = input('Digite o código ou o nome do item que deseja apagar: ').capitalize().strip()
    #     try:
    #         item_apagar_int = int(item_apagar)
    #         for indice, nome_produto in enumerate(lista_de_compras):
    #             if indice == item_apagar_int:
    #                 del nome_produto[indice], indice
    #             print(indice, '-', nome_produto)
    #     except:
    #         for indice, nome_produto in enumerate(lista_de_compras):
    #             if nome_produto == item_apagar:
    #                 del nome_produto[indice], indice
    #             print(indice, '-' , nome_produto)
#    -----------------AJUSTAR AQUI -------------------

    else:
        print('Resposta inválida, tente novamente!')
        continue