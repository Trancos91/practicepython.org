oracion = input("Ingresá una oración de varias palabras: ")
oracionfragmentada = oracion.split()
invertida = " ".join(oracionfragmentada[::-1]).lower().capitalize()
print(f"La oración invertida es: '{invertida}'.")
