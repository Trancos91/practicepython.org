from random import choice, randint
import string
from time import sleep

palabras = open("palabras.txt")
lista_palabras = []
for linea in palabras:
    linea = linea.strip()
    lista_palabras.append(linea)
 
caracteres_especiales = ["!", "$", "#", "@", "[", "]", "+", "-", ",", "."]

def seleccionar_complejidad() :
    x = input("Por favor ingresá un número del 1 al 5: ")
    if x.isnumeric():
        x = int(x)
        if x > 0 and x <= 5 :
            return int(x)
    print("Por favor ingresá un número válido.")
    return seleccionar_complejidad()

def seleccionar_numchar(frase) :
    x = input(frase)
    if x.isnumeric():
        return int(x)
    else:
        print("Por favor ingresá un número")
        return seleccionar_numchar(frase)

def definir_largo(minchar, maxchar):
    largo = minchar + randint(0, maxchar - minchar)
    return largo

def seleccionar_palabra():
    x = choice(lista_palabras)
    return x

def randomizar_mayusculas(frase) :
    frase_modificada = []
    for ch in frase:
            if ch.isalpha():
                uppercase = choice([True, False])
                if uppercase:
                    frase_modificada.append(ch.upper())
                else:
                    frase_modificada.append(ch)
    return "".join(frase_modificada)

def secuenciar_palabras(minchar, maxchar, con_simbolos, con_mayusc):
    contrasena = ""
    while len(contrasena) < minchar:
        elegir_palabra = True
        if con_simbolos:
            elegir_palabra = choice([True, False])
        if elegir_palabra:
            nuevo_texto = seleccionar_palabra()
        else:
            nuevo_texto = choice(caracteres_especiales)
        if len(contrasena + nuevo_texto) <= maxchar :
            contrasena += nuevo_texto
    if con_mayusc:
        contrasena = randomizar_mayusculas(contrasena)
    return contrasena

def secuenciar_caracteres(minchar, maxchar, con_simbolos) :
    contrasena = ""
    caracteres = string.ascii_letters
    if con_simbolos:
        for ch in caracteres_especiales:
            caracteres += ch
    while len(contrasena) < definir_largo(minchar, maxchar):
        contrasena += choice(caracteres)
    return contrasena

def generar_contrasena(complejidad, minchar, maxchar):
    nueva_contrasena = ""
    match complejidad :
        case 1 :
            nueva_contrasena= secuenciar_palabras(minchar, maxchar, con_simbolos=False, con_mayusc=False)
        case 2 :
            nueva_contrasena = secuenciar_palabras(minchar, maxchar, con_simbolos=True, con_mayusc=False)
        case 3 :
            nueva_contrasena = secuenciar_palabras(minchar, maxchar, con_simbolos=True, con_mayusc=True)
        case 4 :
            nueva_contrasena = secuenciar_caracteres(minchar, maxchar, con_simbolos=False)
        case 5 :
            nueva_contrasena = secuenciar_caracteres(minchar, maxchar, con_simbolos=True)
    return nueva_contrasena

def main():
    print("Bienvenido al generador de contraseñas :3")
    sleep(0.5)
    print("""Hay 5 niveles de complejidad:
    Nivel 1 son palabras sueltas.
    Nivel 2 son palabras sueltas con símbolos especiales.
    Nivel 3 son palabras sueltas con símbolos especiales y
    caracteres en mayúsculas al azar.
    Nivel 4 son caracteres al azar en mayúsculas y minúsculas.
    Nivel 5 son caracteres al azar en mayúsculas y minúsculas,
    y caracteres especiales.""")
    complejidad = seleccionar_complejidad()
    minchar = seleccionar_numchar("Por favor seleccioná el número mínimo de caracteres: ")
    maxchar = seleccionar_numchar("Por favor seleccioná el número máximo de caracteres: ")
    contrasena = generar_contrasena(complejidad, minchar, maxchar)
    sleep(1)
    print(f"Tu contraseña es: {contrasena}")
    sleep(1)
    guardar = input("Querés guardar la contraseña en un archivo de texto en esta misma carpeta? ")
    if guardar in ("yes", "ye", "y", "si", "s", "sí") :
        contrasenas = open("contrasenas.txt", "a")
        contrasenas.write(f"""Contraseña generada de complejidad {complejidad}, de entre {minchar} y {maxchar} caracteres:
        {contrasena}""")
        print("Tu contraseña fue guardada en el archivo de texto 'contrasenas' de la misma carpeta que este script.")
    print("Muchas gracias por utilizar el programa!")
    
if __name__ == "__main__" :
    main()
