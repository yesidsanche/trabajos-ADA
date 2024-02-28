import os

numero = 0

while numero <= 50:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(numero)
    input("Presiona la tecla 'n' para continuar...")
    numero += 1

os.system('cls' if os.name == 'nt' else 'clear'),
