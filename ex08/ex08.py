import time
import random
arma = ["piedra", "papel", "tijera"]
jugador = ""
espera = 3
input("Juguemos piedra, papel o tijeras! Apretá cualquier tecla para comenzar.")
while jugador not in arma :
    jugador = input("Elegí piedra, papel o tijera: ")
    jugador = ''.join(x for x in jugador if x.isalpha()).lower()
    if jugador == "tijeras" :
        jugador = "tijera"
bot = arma[random.randint(0,2)]
x = 0
while x <= espera:
    for y in ["|", "/", "-", "\\"]:
        print(f"\rEl bot está eligiendo... {y}", end="") 
        time.sleep(0.2)
        x += 0.2
print(f"\nEl bot eligió {bot}!")
if jugador == bot:
    print("Empate! :o")
else:
    match jugador:
        case "piedra" :
            if bot == arma[2]:
                print("Ganaste!")
            else:
                print("Perdiste :c")
        case "papel" :
            if bot == arma[0]:
                print("Ganaste!")
            else:
                print("Perdiste :c")
        case "tijera" :
            if bot == arma[1]:
                print("Ganaste!")
            else:
                print("Perdiste :c")
