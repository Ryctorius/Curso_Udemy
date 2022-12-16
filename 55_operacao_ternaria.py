varial = 'Valor' if True else 'Outro valor'
print('Valor' if True else 'Outro valor')

digito = 1
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

novo_digito = digito if digito <= 9 else 0
print(novo_digito)

print('Valor' if False else 'Outro valor' if False else 'Fim')
