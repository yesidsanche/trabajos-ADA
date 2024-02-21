import readchar

# Definir el laberinto como una lista de strings
laberinto = [
    "###################",
    "#       #         #",
    "#  #####    ##### #",
    "#           #     #",
    "#  #####    ##### #",
    "#                 #",
    "###################"
]

# Posición inicial del jugador
posicion_jugador = (1, 1)

# Función para imprimir el laberinto en la terminal


def imprimir_laberinto():
    for fila in laberinto:
        print(fila)


# Función para mover al jugador


def mover_jugador(direccion):
    global posicion_jugador

    x, y = posicion_jugador

    if direccion == 'w' and laberinto[y-1][x] != '#':
        posicion_jugador = (x, y-1)
    elif direccion == 's' and laberinto[y+1][x] != '#':
        posicion_jugador = (x, y+1)
    elif direccion == 'a' and laberinto[y][x-1] != '#':
        posicion_jugador = (x-1, y)
    elif direccion == 'd' and laberinto[y][x+1] != '#':
        posicion_jugador = (x+1, y)


# Loop principal del juego


while True:
    imprimir_laberinto()

    # Leer el siguiente movimiento del jugador
    tecla = readchar.readkey()

    # Limpiar la pantalla de la terminal
    print("\033[H\033[J")

    # Mover al jugador
    mover_jugador(tecla)

    # Verificar si el jugador llegó a la salida
    x, y = posicion_jugador
    if laberinto[y][x] == ' ':
        print("¡Felicidades! Has llegado a la salida.")
        break
