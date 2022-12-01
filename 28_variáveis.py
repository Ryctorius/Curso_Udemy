""" DICAS PARA ESTRUTURAR CÓDIGO """


# ADOTAR LETRA MAIÚSCULA PARA CONSTANTES
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade = 60
local_carro =99

# Variáveis bem descritas para devs conseguirem saber do que a variavel se trata de imediato
vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_local_radar_1 = local_carro >= (LOCAL_1-RADAR_RANGE) and local_carro <=(LOCAL_1+RADAR_RANGE)

# variáveis para diminuir condicionais dos if's
carro_multado_radar_1 = carro_passou_local_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print("Velocidade do carro acima da permitida")

if carro_passou_local_radar_1:
    print("Carro passou no local do radar")

if  carro_multado_radar_1:
    print('Carro multado em radar 1')
