x, y, *resto = 1, 2, 3, 4, 5
print(x, y, resto)



# def soma(x,y):
#     return x+y



def soma(*args):
    # args = list(args)
    # print(args, type(args))
    total = 0
    for numero in args:
        total += numero
    return total

soma_numeros = soma(1,2,3,4,5,6)
print (soma_numeros)

# print(sum((1,2,3,4,5,6)))


numeros =(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numeros)
print(*numeros)
print(sum(numeros))
