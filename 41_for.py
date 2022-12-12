for i in range(10):
    if i == 2:
        print('i é 2, pulando ...')
        continue
    if i == 8:
        print('i é 8, seu else não sera executado')
        break
    for j in range (1, 3):
        print (i, j)
else: #Só executa se o for executar por completo, em caso de break, o else do for não é executado
    print('For completo com sucesso!')
