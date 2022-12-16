from decimal import Decimal as amoeba

numero_1 = amoeba(0.1)
numero_2 = amoeba(0.7)
numero_3 = numero_1+numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(numero_3.__round__(3))
print(round(numero_3,3))
