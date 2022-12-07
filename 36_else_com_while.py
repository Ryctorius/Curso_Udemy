string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print (letra)
    i +=1
    
#executa apos o while acabar de executar, não rodando caso interrupção do while com break
else: 
    print('O else foi executado')
print('Fora do while')
