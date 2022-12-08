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

def recorre_laberinto(laberinto):
    # Fila y columnas iniciales
    fila = 0
    columna = 0
    # Dimensiones del laberinto
    n = len(laberinto)
    # Lista de movimientos
    movimientos = ['Abajo']
    while (fila < n-1 and columna < n-1):
        if movimientos[-1] != 'Arriba' and fila + 1 < n and laberinto[fila + 1][columna] != 'X':
            fila += 1
            movimientos.append('Abajo')
        elif movimientos[-1] != 'Abajo' and fila - 1 > 0 and laberinto[fila - 1][columna] != 'X':
            fila -= 1
            movimientos.append('Arriba')
        elif movimientos[-1] != 'Izquierda' and columna + 1 < n and laberinto[fila][columna + 1] != 'X':
            columna += 1
            movimientos.append('Derecha')
        elif movimientos[-1] != 'Derecha' and columna - 1 > 0 and laberinto[fila][columna - 1] != 'X':
            columna -= 1
            movimientos.append('Izquierda')
        else:
            movimientos.append('No hay salida')
    return movimientos

# Mostrar por pantalla la lista de movimientos
print('Solución: ', recorre_laberinto(lab))