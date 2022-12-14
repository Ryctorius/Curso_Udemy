lista_a = ['Luiz', 'Maria']
lista_b = lista_a
lista_a[0] = 'Qualquer coisa'
print(lista_b)



lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'
print(lista_b)