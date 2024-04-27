a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([x for x in a if x<5], "son números menores a 5")
limite = int(input("Ingresá un número: "))
print([x for x in a if x<limite], "son números menor a", limite)
