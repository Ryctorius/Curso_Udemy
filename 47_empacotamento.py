nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome2)

nomes = ['Maria', 'Helena', 'Luiz']
nome1, *resto = nomes
print(nome2, resto)

nomes = ['Maria', 'Helena', 'Luiz']
nome1, *_ = nomes
print(nome2, _)

nomes = ['Maria', 'Helena', 'Luiz']
_ ,nome2, *_ = nomes
print(nome2, _)