nome = input('Digite o nome desejado:')
tamanho_nome = len(nome)
contador = 0
nome_novo = '*'
while contador < tamanho_nome:
    nome_novo += nome[contador]+'*'
    contador += 1
print(nome_novo)
