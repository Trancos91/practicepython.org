import random
a = [random.randint(0,100) for _ in range(random.randint(15, 40))]
b = [random.randint(0,100) for _ in range(random.randint(15, 40))]
comunes = []
if len(a) > len(b):
    masLarga = a
    masCorta = b
else:
    masLarga = b
    masCorta = a
print(f"La lista más larga es {masLarga}")
print(f"La lista más corta es {masCorta}")
for x in masLarga:
    if x in masCorta and x not in comunes:
        comunes.append(x)
print(f"Los números que ambas listas tienen en común son {comunes}")
