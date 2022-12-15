lista = ['Maria', 'Helena' , 'Luiz']
lista.append('joao')

# lista_enumerada = list(enumerate(lista, start= 10))

# print(lista_enumerada)

# for item in enumerate(lista):
#     indice, nome = item
#     print(item)


for indice, nome  in enumerate(lista):
    print(indice, nome, lista[indice])
