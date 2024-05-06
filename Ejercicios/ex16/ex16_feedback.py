#!/usr/bin/env python3
import string
from random import choice, randint
from time import sleep

class Generador_Contraseñas:
    
    def __init__(self) -> None:
        self.lista_palabras = []
        with open("palabras.txt") as palabras:
            for linea in palabras:
                self.lista_palabras.append(linea.strip())
        self.caracteres_especiales = ["!", "$", "#", "@", "[", "]", "+", "-", ",", "."] 
        
    def procesar_palabras(self, lista_palabras):
        pass
        
    def seleccionar_numchar(self, msj, min=None, max=None) :
        """Pregunta al usuario con el msj recibido, regresa un número
        entre los valores min y max"""
        while True:
            x = input(msj)
            if x.isnumeric():
                x = int(x)
                if min is None and max is None:
                    return x
                elif (min is not None and max is not None
                        and x >= min and x <= max):
                    return int(x)
                else:
                    print("Por favor ingresá un número válido.")

    def definir_largo(self, minchar, maxchar):
        return minchar + randint(0, maxchar - minchar)

    def seleccionar_palabra(self):
        return choice(self.lista_palabras)

    def randomizar_mayusculas(self, frase) :
        frase_modificada = []
        for ch in frase:
            uppercase = choice([True, False])
            frase_modificada.append(ch.upper() if ch.isalpha and uppercase else ch)
#       Dejo el código viejo porque tiene la correción del bug, pero
#       incorporo tu línea más concisa
#            if ch.isalpha():
#                uppercase = choice([True, False])
#                if uppercase:
#                    frase_modificada.append(ch.upper())
#                else:
#                    frase_modificada.append(ch)
#            else:
#                frase_modificada.append(ch)
        return "".join(frase_modificada)

    def secuenciar_palabras(self, minchar, maxchar, con_simbolos, con_mayusc):
        contraseña = ""
        while len(contraseña) < minchar:
            elegir_palabra = choice([True, False]) if con_simbolos else True
            nuevo_texto = (self.seleccionar_palabra() if elegir_palabra 
                else choice(self.caracteres_especiales))
            if len(contraseña + nuevo_texto) <= maxchar :
                contraseña += nuevo_texto
        if con_mayusc: contraseña = self.randomizar_mayusculas(contraseña)
        return contraseña

    def secuenciar_caracteres(self, minchar, maxchar, con_simbolos) :
        contraseña = ""
        caracteres = list(string.ascii_letters)
        if con_simbolos:
            caracteres += self.caracteres_especiales
        largo = self.definir_largo(minchar, maxchar)
        while len(contraseña) < largo:
            contraseña += choice(caracteres)
        return contraseña

    def generar_contraseña(self, complejidad, minchar, maxchar):
        match complejidad :
            case 1 :
                nueva_contraseña= self.secuenciar_palabras(minchar, maxchar, con_simbolos=False, con_mayusc=False)
            case 2 :
                return self.secuenciar_palabras(minchar, maxchar, con_simbolos=True, con_mayusc=False)
            case 3 :
                return self.secuenciar_palabras(minchar, maxchar, con_simbolos=True, con_mayusc=True)
            case 4 :
                return self.secuenciar_caracteres(minchar, maxchar, con_simbolos=False)
            case 5 :
                return self.secuenciar_caracteres(minchar, maxchar, con_simbolos=True)

def main():
    generador = Generador_Contraseñas()
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
    complejidad = generador.seleccionar_numchar(
        "Por favor ingresá un número entre 1 y 5: ",
        1, 5)
    minchar = generador.seleccionar_numchar("Por favor seleccioná el número mínimo de caracteres: ")
    maxchar = generador.seleccionar_numchar("Por favor seleccioná el número máximo de caracteres: ")
    contraseña = generador.generar_contraseña(complejidad, minchar, maxchar)
    sleep(1)
    print(f"Tu contraseña es: {contraseña}")
    sleep(1)
    guardar = input("Querés guardar la contraseña en un archivo de texto en esta misma carpeta? ")
    if guardar in ("yes", "ye", "y", "si", "s", "sí") :
        with open("contraseñas.txt", "a") as contraseñas:
            contraseñas.write(f"""Contraseña generada de complejidad {complejidad}, de entre {minchar} y {maxchar} caracteres:
            {contraseña}""")
            print("Tu contraseña fue guardada en el archivo de texto 'contraseñas' de la misma carpeta que este script.")
    print("Muchas gracias por utilizar el programa!")
    
if __name__ == "__main__" :
    main()
