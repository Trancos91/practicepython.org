numero = int(input("Ingresá un número para ver sus divisores: "))
divisores = []
for x in range(1, numero):
    if numero % x == 0:
        divisores.append(x)
for x in divisores:
    if x == 1:
        print(x, end="")
    elif x == divisores[len(divisores) - 1]:
        print(f" y {x} son divisores de {numero}.")
    else:
        print(f", {x}", end="")
    
