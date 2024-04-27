# Guessing game
import random

jugador = None
bot = random.randint(1, 9)
victorias = 0
print("Bienvenidx al juego de adivinanzas!")
print("El objetivo es adivinar un número al azar entre 1 y 9(inclusive).")
while True:
    jugador = input("Ingresá un número del 1 al 9(o ingresá 'exit' para salir): ").lower()
    if jugador == "exit":
        break
    jugador = int(jugador)
    if jugador == bot:
        victorias += 1
        print("Ganaste!")
        print("Jugamos de nuevo?")
        bot = random.randint(1, 9)
    elif jugador > bot:
        print("El número es muy grande!")
    elif jugador < bot:
        print("El número es muy chico!")
    else:
        print("La respuesta debe ser un número entre 1 y 9 o 'exit'.")
print(f"Gracias por jugar! Ganaste {victorias} veces.")
