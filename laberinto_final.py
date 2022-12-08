laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

camino = ""
laberinto = []
laberinto.append([])
res = []
maxh = 0
maxv = 0
piso = []

for a in laberinto:
    maxv += 1
    maxh = 0
    for b in a:
        maxh += 1

