a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
comunes = []
if len(a) > len(b):
    masLarga = a
    masCorta = b
else:
    masLarga = b
    masCorta = a
print(f"La lista más larga es {masLarga}")
for x in masLarga:
    if x in masCorta and x not in comunes:
        comunes.append(x)
print(f"Los números que ambas listas tienen en común son {comunes}")
