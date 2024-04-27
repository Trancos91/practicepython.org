num = (int(input("Elegí un número: ")))
if num % 4 == 0:
    print(f"{num} es múltiplo de 4.")
elif num % 2 == 0:
    print(f"{num} es par.")
else:
    print(f"{num} es impar.")
numerador = (int(input("Elegí tu numerador: ")))
denominador = (int(input("Elegí tu denominador: ")))
if numerador % denominador == 0:
    print(f"{numerador} es divisible por {denominador}.")
else:
    print(f"{numerador} no es divisible por {denominador}.")
