#aula passada
nome = 'Felipe'
peso = 84
altura_metros = 1.70
imc = peso/(altura_metros**2)

print( nome , 'tem', altura_metros, 'de altura, pesa', peso, 'quilos e seu IMC é', imc )

#aula nova
frase_formatada = f'{nome} tem {altura_metros:.2f} de altura, pesa {peso} quilos e seu IMC é {imc:.3f}'
print(frase_formatada)
