nombre = input("Ingresá tu nombre: ")
edad= int(input("Ingresá tu edad: "))
veces = int(input("Cuántas veces querés repetir el mensaje?"))
print(f"{nombre}, tenés {edad} años. Vas a tener 100 dentro de {100-edad} años\n" * veces)
