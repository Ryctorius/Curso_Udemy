lista = [123, True, 'Luiz Otávio', 1.2,[]]

print(lista[2], type(lista[2]))

lista[-3] = 'Maria'

print(lista[2], type(lista[2]))
print(lista)

lista = [10, 20, 30, 40, 50]
print(lista[2])
print(lista)
lista[2] = 300
print(lista[2])
print(lista)
del lista[2]
print(lista[2])
print(lista)

lista.pop() #remove o último item da lista
lista.append(60)
lista.append(70)
lista.append(80)
valor_removido =lista.pop()
lista.append(90)

print(lista)
print(valor_removido)

lista.pop(3)
print(lista)

lista = [10, 20, 30, 40, 50]
print(lista)
lista.append('Luiz')
print(lista)
nome = lista.pop()
print(lista)
lista.append(1223)
print(lista)
del lista[-1]
print(lista)
lista.clear()
print(lista)
lista.insert(0, 5) #recebe 2 argumentos, primeiro a posição depois o valor a ser inserido
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
lista_d = lista_a.extend(lista_b) #extend não retorna valor, ela mexe direto na origem
print(lista_d)
print(lista_a) #Demonstrando, mexeu direto na lista A, não retornou valor para ser acrescido na lista D
