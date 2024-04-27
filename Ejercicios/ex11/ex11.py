#!/usr/bin/env python3
def check_prime(a):
    for x in range(2, a):
        if a % x == 0:
            return False
    else:
        return True
def get_input(msj="Ingresá texto: "):
    y = input(msj)
    return y
prompt = get_input("Ingresá un número para ver si es primo o escribí 'exit' para salir: ")
while True:
    if prompt.lower() == "exit":
        break
    num = int(prompt)
    if check_prime(num):
        print(f"{num} es un número primo! :D")
    else:
        print(f"{num} no es un número primo :(")
    prompt = get_input("Ingresá otro número, o escribí 'exit' para salir: ")
