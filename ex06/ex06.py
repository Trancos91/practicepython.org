oracion = input("Ingresá una palabra: ")
# palabra = oracion.replace(" ","").lower() # Recibe oraciones con mayúsculas y minúsculas, sin signos de puntuación.
palabra = ''.join(x for x in oracion if x.isalpha()).lower() # Se le asigna un string vacío, luego se itera sobre oracion y
print(palabra)                                       # agregan sólo los caracteres ya no alfanuméricos, sino alfabéticos (antes usaba isalnum).
mitadPalabra = len(palabra) // 2
if palabra [:mitadPalabra] == palabra [:(mitadPalabra*-1)-1:-1]:
    print(f"{oracion} es un palíndromo! :D")
else:
    print(f"{oracion} no es un palíndromo :c")
