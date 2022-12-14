# Tupla é imutável, a diferença visual entre elas são os colchetes 
nomes = 'Maria', 'Helena', 'Luiz'


print(nomes)


nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
print(nomes)
nomes = list(nomes)
print(nomes)
