#Bloco 1
texto = iter('Luiz') #  ._iter_() -> mesma função
print(texto)
print(texto.__next__())
print(texto.__next__())
print(next(texto))
print(next(texto))



# Bloco 2
texto = 'Luiz' #iterável
iterador = iter(texto) #iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break






# Bloco 3
for letra in texto:
    print(letra)
