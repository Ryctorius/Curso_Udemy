x=1


def escopo():
    global x #altera o valor da variável do módulo
    x = 999

    def outra_funcao():
        x=55
        y=2
        print(x,y)
    outra_funcao()
    print(x)



print(x)

escopo()
print(x)
