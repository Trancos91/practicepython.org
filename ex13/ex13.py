#!/usr/bin/env python3
n = int(input("Ingresá cuántos números querés obtener de la secuencia de Fibonacci: "))
def seq_fibonacci(n):
    secuencia = []
    x1 = 0
    x2 = 1
    for _ in range(n):
        secuencia.append(x1)
        x3 = x2 + x1
        x1 = x2
        x2 = x3
    return secuencia
print(seq_fibonacci(n))
