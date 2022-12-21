def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao ('Luiz')
saudacao('Felipe')
saudacao('João')
saudacao()
saudacao('Yasmin')


def soma (x, y, z):
    print(f'{x=} {y=} {z=}', 'x+y+z = ', x+y+z)


soma(1, 2, 3)
soma(y=6, z=4, x=5)



def soma (x, y, z= None):
    if z is not None:
        print(f'{x=} {y=} {z=}', 'x+y+z = ', x+y+z)
    else:
        print(f'{x=} {y=} ', 'x+y = ', x+y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(9, 0, 7)
