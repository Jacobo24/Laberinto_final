def laberinto(tamaño, limite):
    laberinto = []
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            if tuple([i, j]) in limite:
                fila.append('X')
            else:
                fila.append(' ')
        laberinto.append(fila)
    return laberinto

limite = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
lab = laberinto(5, limite)

for i in lab:
    print(''.join(i))