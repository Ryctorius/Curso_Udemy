a ='AAAAAA'
b ='BBBBBB'
c =1.1
string = 'a={0} a={0} a={0} a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c) #Número nas chaves representa a ordem dos ARGUMENTOS 0,1,2,3,...

print(formato)

#o parametro pode ser nomeado
#o valor de c é um argumento, já o nome3 é um parâmetro

string = 'a={nome1} a={nome1} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c) #Número nas chaves representa a ordem dos ARGUMENTOS 0,1,2,3,...

print(formato)
